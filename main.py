from saku_mon.coding_test_generator import CodingTestGenerator
from dotenv import load_dotenv
import os
import argparse

if __name__ == "__main__":
    load_dotenv(dotenv_path=".env")
    
    parser = argparse.ArgumentParser(description="Generate coding tests from a given GitHub repository.")
    parser.add_argument("--force-clone", action="store_true", help="Remove existing local repository if it exists.")
    args = parser.parse_args()
    
    repo_path = os.getenv("REPO_PATH") or input("Enter the GitHub repo owner/repo_name: ")
    generator = CodingTestGenerator(repo_path)
    generator.run(force_clone=args.force_clone)