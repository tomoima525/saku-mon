# saku-mon (作問:さくもん)

A tool for generating coding tests from github repositories.
Saku-mon is a Japanese word that means "to make a question".

# Setup

- Install [poetry](https://python-poetry.org/docs/#installation) (Python package manager) for managing dependencies.
- Run `poetry install` to install dependencies.
- Run `poetry shell` to activate the virtual environment.
- Setup `.env` file for Open AI key and GitHub API key (see `.env.example` for reference).
  - GITHB_API_KEY is only required if you want to access private repositories. Make sure that the key has the necessary permissions. (see [Creating a fine-grained personal access token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens#creating-a-fine-grained-personal-access-token))

# Usage

- Run `python main.py` to generate coding tests from a given github repository.
  - `--force-clone` flag can be used to force clone the repository(Remove the local repository).

Example output:

```bash
$ python main.py
Enter the GitHub repo owner/repo_name: knot-inc/english-analysis-exps
GitHub user: tomoima525
Cloning repository ...
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 2411k    0 2411k    0     0  2815k      0 --:--:-- --:--:-- --:--:-- 2813k
Repository cloned to /Users/tomoima525/workspace/python/saku-mon/repo/english-analysis-exps
Checking project type for /Users/tomoima525/workspace/python/saku-mon/repo/english-analysis-exps
 as True
Project type: python
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
- Support for private repositories using API key.
- Support for various programming languages.
- Support for adding extra constraints to the generated questions.

# License

MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
