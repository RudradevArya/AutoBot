# AutoBot :: GeeksForGeeks POTD Solution Automator

This script automates the process of saving, committing, and pushing your GeeksForGeeks problem of the day solution to a GitHub repository. It uses a simple GUI to take user inputs for code, file extension, custom file name, and commit message.

## Features

* Save code to a specified or default directory.
* Create custom or default commit messages.
* Commit and push changes to a GitHub repository using GitPython.
* Simple GUI for user interaction.

## Requirements

* Python 3.x
* GitPython
* Tkinter
* PyInstaller (for creating the executable)

## Installation

1. **Clone the repository** (if you have it hosted on GitHub):

``` sh
git clone https://github.com/<your-github-username>/<your-repo-name>.git
cd <your-repo-name>
```

2. **Install the required Python packages**:

``` sh
pip install gitpython
```

## Usage

1. **Run the script**:

``` sh
python AutoBot.py
```

2. **Interact with the GUI**:
    * Enter your code, file extension, custom file name, and repository path.
    * Choose between using a custom commit message or a default commit message.
    * Choose between saving the file to a custom folder path or the default folder path.

## Creating an Executable

To create an executable file from the Python script, follow these steps:

1. **Install PyInstaller**:

``` sh
pip install pyinstaller
```

2. **Create the executable**:

``` sh
python -m PyInstaller --onefile --windowed --hidden-import=git AutoBot.py
```

3. The executable will be created in the `dist` directory.

## Example Command

For convenience, you can use the following command to create the executable:

``` sh
python -m PyInstaller --onefile --windowed --hidden-import=git Auto.py
```