# lets create a git automatic tool using os module
import os
import subprocess

os.system("git status")
a = input("Do you want to add all changes? (y/n): \n")
os.system("git add .")
message = input("Enter commit message: \n")
os.system(f'git commit -m "{message}"')
branch = input("Enter branch name to push to (default is 'main'): \n")


class GitAutomatedTool:
    def __init__(self, branch="main"):
        self.branch = branch if branch else "main"

    def push_changes(self):
        os.system(f"git push origin {self.branch}")
        print(f"Changes pushed to branch {self.branch}")


GitAutomatedTool_instance = GitAutomatedTool(branch)
