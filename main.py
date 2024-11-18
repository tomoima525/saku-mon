from saku_mon.coding_test_generator import CodingTestGenerator
from dotenv import load_dotenv
import os

if __name__ == "__main__":
    load_dotenv()
    repo_url = os.getenv("REPO_URL") or input("Enter the GitHub repository URL: ")
    generator = CodingTestGenerator(repo_url)
    generator.run()