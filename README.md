# saku-mon (作問:さくもん)

A tool for generating coding tests from github repositories.
Saku-mon is a Japanese word that means "to make a question".

# Setup

- Install [poetry](https://python-poetry.org/docs/#installation) (Python package manager) for managing dependencies.
- Run `poetry install` to install dependencies.
- Run `poetry shell` to activate the virtual environment.
- Setup `.env` file for Open AI key (see `.env.example` for reference).

# Usage

- Run `python main.py` to generate coding tests from a given github repository.

Example output:

```bash
$ python main.py
Repository already cloned to /Users/tomoima525/workspace/python/saku-mon/repo/elastic-ip-lambda
Project type: typescript
Select a coding test idea:
1. Implement a script to automate the process of setting up a NAT instance with Elastic IP in a VPC environment, ensuring the script handles subnet configurations and routing tables appropriately.
2. Create a function that verifies the setup of a static IP for AWS Lambda using a NAT instance by checking the routing and security group settings, and ensures the Lambda function can access external services like a REST API.
3. Develop an application that transitions an existing AWS VPC architecture from using a NAT Gateway to a NAT instance, including updating route tables and security policies, and validate the migration with test cases.
4. Write a script to deploy an AWS Lambda function within a private subnet that can make outgoing requests via a NAT instance, then test the function's ability to access the internet using its assigned static IP.
Enter the number of your choice: 2
Generating a coding test for the selected idea: Create a function that verifies the setup of a static IP for AWS Lambda using a NAT instance by checking the routing and security group settings, and ensures the Lambda function can access external services like a REST API.
Instructions generated
Generating initial codebase
Initial codebase generated
Generating example solution...
```

# How it works?

- Saku-mon Agent retrieves the code from the given github repository. Then it will review the codebase and suggest coding questions.
- Based on your choice, the tool will generate coding questions using the LLM model.
- The generated questions will be saved in the `output` directory.

# Future Works

- Support for other LLM models like llama, claude, etc.
- Support for private repositories.
- Support for various programming languages.
- Support for adding extra constraints to the generated questions.
