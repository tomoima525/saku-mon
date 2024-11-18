import os
from git import Repo
import shutil
from saku_mon.llm_client import OpenAIClient
from saku_mon.output_structures import CodingTestIdea


# enum for project type
from enum import Enum
class ProjectType(Enum):
    TYPESCRIPT = "typescript" 
    PYTHON = "python" 
# dictionary for project type (typescript, python, java)
extensions_to_extract = {
    "typescript": [".js", ".ts", ".jsx", ".tsx", ".md"],
    "python": [".py", ".ipynb", ".md"],
}

class CodingTestGenerator:
    def __init__(self, repo_url):
        self.repo_url = repo_url
        self.project_root = os.path.abspath(os.path.join(os.getcwd()))
        self.output_file = f"{self.project_root}/output/repo_contents.txt"
        os.makedirs(os.path.dirname(self.output_file), exist_ok=True)
        self.llm_client = OpenAIClient()

    def clone_repo(self):
        repo_name = self.repo_url.split("/")[-1].replace(".git", "")
        self.clone_dir = f"{self.project_root}/repo/{repo_name}"
        if os.path.exists(self.clone_dir):
            # shutil.rmtree(self.clone_dir)
            print(f"Repository already cloned to {self.clone_dir}")
            return
        Repo.clone_from(self.repo_url, self.clone_dir)
        print(f"Repository cloned to {self.clone_dir}")
    
    def get_project_type(self):
        """
        Check the cloned repository and return the file extensions to extract.
        """
        if os.path.exists(f"{self.clone_dir}/package.json"):
            return ProjectType.TYPESCRIPT
        # if requirements.txt or pyproject.toml or setup.py exists, it is a python project 
        elif os.path.exists(f"{self.clone_dir}/pyproject.toml") or os.path.exists(f"{self.clone_dir}/setup.py") or os.path.exists(f"{self.clone_dir}/requirements.txt"):
            return ProjectType.PYTHON
        else:
            return None

    def extract_files_to_single_file(self, file_extensions=['.py', '.ipynb', '.md']):
        """
        Extract all files in the cloned repository into a single file.

        Parameters:
        file_extensions (list): List of file extensions to extract.
        """
        if os.path.exists(self.output_file):
            os.remove(self.output_file)
        with open(self.output_file, 'w') as outfile:
            for root, _, files in os.walk(self.clone_dir):
                for file in files:
                    file_path = os.path.join(root, file)
                    if os.path.splitext(file_path)[1] in file_extensions:
                      with open(file_path, 'r', errors='ignore') as infile:
                          outfile.write(f"{'-'*100}\n")
                          outfile.write(f"{file_path}:\n")
                          outfile.write(f"{'-'*100}\n")
                          outfile.write(infile.read())
                          outfile.write("\n\n")

    def generate_coding_test_ideas(self):
        with open(self.output_file, 'r') as file:
            contents = file.read()
        prompt = (
            "Read the following codes and generate up-to 4 coding test ideas."
            "Ideas should be an array of strings.\n\n"
            f"### Codes ###\n{contents}\n\nCoding test ideas:")

        result = self.llm_client.generate_completion(prompt, response_format=CodingTestIdea)
        ideas = result.ideas
        return ideas

    def select_coding_test_idea(self, ideas):
        print("Select a coding test idea:")
        for i, idea in enumerate(ideas, 1):
            print(f"{i}. {idea}")
        choice = int(input("Enter the number of your choice: "))
        return ideas[choice - 1]

    def generate_files(self, selected_idea, project_type="python"):
        os.makedirs(f"{self.project_root}/output/initial", exist_ok=True)
        os.makedirs(f"{self.project_root}/output/solution", exist_ok=True)

        print(f"Generating a coding test for the selected idea: {selected_idea}")
        # Generate instructions using LLM
        instructions_prompt = f"Generate detailed instructions for the following coding test idea using {project_type}:\n\n{selected_idea}\n\nInstructions:"
        instructions = self.llm_client.generate_completion(instructions_prompt)

        with open(f"{self.project_root}/output/instructions.md", 'w') as f:
            f.write(f"# Coding Test: {selected_idea}\n\n")
            f.write(instructions)

        print("Instructions generated")
        print("Generating initial codebase...")
        # Generate initial codebase using LLM
        initial_code_prompt = (
            f"Generate the initial codebase for the following coding test instruction using {project_type}."
            f"<Instructions>\n{instructions}"
            "\n\nInitial codebase:"
        )
        initial_code = self.llm_client.generate_completion(initial_code_prompt)
        with open(f"{self.project_root}/output/initial/initial_code.md", 'w') as f:
            f.write(initial_code)
        print("Initial codebase generated")
        print("Generating example solution...")

        # Generate example solution using LLM
        solution_prompt = (
            f"Generate an example solution for the following coding test instruction and initial code using {project_type}."
            f"<Instruction>\n{instructions}\n"
            f"<Initial code>\n{initial_code}\n"
            "\n\nExample solution:")
        solution_code = self.llm_client.generate_completion(solution_prompt)

        with open(f"{self.project_root}/output/solution/solution_code.md", 'w') as f:
            f.write(solution_code)
        print("Example solution generated!")

    def run(self):
        self.clone_repo()
        project_type = self.get_project_type()
        print(f"Project type: {project_type.value if project_type else 'Unknown'}")
        file_extensions = extensions_to_extract[project_type.value] if project_type else None
        self.extract_files_to_single_file(file_extensions=file_extensions)
        coding_test_ideas = self.generate_coding_test_ideas()
        if not coding_test_ideas:
            print("No coding test ideas could be generated from the repository contents.")
            return
        selected_idea = self.select_coding_test_idea(coding_test_ideas)
        self.generate_files(selected_idea, project_type=project_type.value)