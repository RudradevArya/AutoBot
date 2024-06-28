import os
from git import Repo, RemoteProgress
from datetime import datetime
import tkinter as tk
from tkinter import simpledialog, messagebox, filedialog

class Progress(RemoteProgress):
    def update(self, op_code, cur_count, max_count=None, message=''):
        if message:
            print(message)

def save_code_to_file(code, file_path):
    with open(file_path, 'w') as file:
        file.write(code)

def commit_and_push(repo_path, file_path, commit_message):
    repo = Repo(repo_path)
    if repo.is_dirty(untracked_files=True):
        repo.git.add(file_path)
        repo.index.commit(commit_message)
        if 'origin' not in [remote.name for remote in repo.remotes]:
            # Add remote if it doesn't exist
            repo.create_remote('origin', 'https://github.com/RudradevArya/GfG-POTD.git')
        origin = repo.remote(name='origin')
        # origin.push()
        # origin.push(progress=Progress())
         # Set the upstream branch if not already set
        if repo.head.is_detached or repo.active_branch.tracking_branch() is None:
            repo.git.push('--set-upstream', origin, repo.head.ref)
        else:
            origin.push(progress=Progress())

    # repo.git.add(file_path)
    # repo.index.commit(commit_message)
    # origin = repo.remote(name='origin')
    # origin.push()

def main():
    # Create a simple dialog to get user input
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    def get_input(prompt):
        return simpledialog.askstring("Input", prompt)

    code = get_input("Please enter your code:")
    extension = get_input("Please enter the file extension:")
    custom_name = get_input("Please enter the custom file name:")

    # code = simpledialog.askstring("Input", "Please enter your code:")
    # extension = simpledialog.askstring("Input", "Please enter the file extension:")
    # custom_name = simpledialog.askstring("Input", "Please enter the custom file name:")
    # repo_path = simpledialog.askstring("Input", "Please enter the path to your local git repository:")

    # Current date in dd-mm-yy format
    current_date = datetime.now().strftime('%d-%m-%y')

    def default_commit_message():
        return f"{current_date} GfG POTD solution"

    def get_commit_message():
        commit_message = simpledialog.askstring("Input", "Please enter the commit message:")
        if not commit_message:
            commit_message = default_commit_message()
        return commit_message
    def select_default_location():
        return os.path.expanduser("~/Desktop/GeeksForGeeksSolutions")

    def open_commit_message_dialog(repo_path):
        commit_message = get_commit_message()
        # File name and path
        file_name = f"{current_date}_{custom_name}.{extension}"
        folder_path = os.path.expanduser(repo_path)
        os.makedirs(folder_path, exist_ok=True)
        file_path = os.path.join(folder_path, file_name)
        
        # Save the code to a file
        save_code_to_file(code, file_path)
        
        # Commit and push the changes
        commit_and_push(folder_path, file_path, commit_message)
        
        messagebox.showinfo("Success", "Code committed and pushed successfully!")
        root.quit()

    def custom_location_action():
        repo_path = get_input("Please enter the path to your local git repository:")
        open_commit_message_dialog(repo_path)

    def default_location_action():
        repo_path = select_default_location()
        open_commit_message_dialog(repo_path)

    root.deiconify()
    root.geometry("400x200")
    label = tk.Label(root, text="Choose file location option:")
    label.pack(pady=10)

    button_custom = tk.Button(root, text="Custom Folder Path", command=custom_location_action)
    button_custom.pack(pady=5)

    button_default = tk.Button(root, text="Default Folder Path", command=default_location_action)
    button_default.pack(pady=5)

    root.mainloop()
    # commit_message = get_commit_message()
    
    # # File name and path
    # file_name = f"{current_date}_{custom_name}.{extension}"
    # folder_path = os.path.expanduser(repo_path)
    # # folder_path = os.path.expanduser("Z:\GfG\POTD")
    # os.makedirs(folder_path, exist_ok=True)
    # file_path = os.path.join(folder_path, file_name)

    # Save the code to a file
    # save_code_to_file(code, file_path)

    # # Path to your local git repository
    # # repo_path = folder_path  # Assuming your local repo is the same as the folder_path

    # # Commit and push the changes
    # commit_message = "Add solution of the day"
    # commit_and_push(repo_path, file_path, commit_message)

if __name__ == "__main__":
    main()
