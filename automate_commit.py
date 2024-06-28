import os
from git import Repo

def save_code_to_file(code, file_path):
    with open(file_path, 'w') as file:
        file.write(code)

def commit_and_push(repo_path, file_path, commit_message):
    repo = Repo(repo_path)
    repo.git.add(file_path)
    repo.index.commit(commit_message)
    origin = repo.remote(name='origin')
    origin.push()

def main():
    # The code from Geeks for Geeks IDE
    code = '''# Your code here'''

    # Path to the folder on your desktop
    folder_path = os.path.expanduser("Z:\GfG")
    os.makedirs(folder_path, exist_ok=True)

    # File name and path
    file_name = "solution_of_the_day.py"
    file_path = os.path.join(folder_path, file_name)

    # Save the code to a file
    save_code_to_file(code, file_path)

    # Path to your local git repository
    repo_path = folder_path  # Assuming your local repo is the same as the folder_path

    # Commit and push the changes
    commit_message = "Add solution of the day"
    commit_and_push(repo_path, file_path, commit_message)

if __name__ == "__main__":
    main()
