#### How It Works:

**File Type Mapping**: 
You define the file types (file_types) and their corresponding extensions.

**Directory to Organize**: 
Specify the directory you want to organize, such as ~/Downloads or ~/Desktop.

**Folder Creation**: 
The script creates subfolders for each file type in the specified directory.

**File Movement**:
Files are moved into their respective folders based on their extensions. Files with unknown extensions are moved into an "Others" folder.


**_The os and shutil modules are essential Python libraries that facilitate file and directory management. Here's an explanation of each and how they are used in the organize_files.py script._**

**1. os Module** <br>
The os module provides a way to interact with the operating system, including file and directory operations. It allows platform-independent file management.

Key Functions Used in organize_files.py:

_os.path.join():_ <br>
**Combines directory and file paths in a platform-independent way.** <br>
Example in the script: <br>
folder_path = os.path.join(base_path, folder) <br>
This ensures the correct path structure (e.g., C:\folder on Windows or /folder on macOS/Linux).

_os.path.exists():_ <br>
**Checks if a specified path (file or directory) exists.**<br>
Example in the script:<br>
if not os.path.exists(folder_path): <br>
    os.mkdir(folder_path)

_os.listdir():_ <br>
**Lists all files and directories in a given directory.** <br>
Example in the script: <br>
for file_name in os.listdir(base_path): <br>
This loops through all files and directories in the specified directory (base_path). <br>

_os.path.isdir():_ <br>
**Checks if a path is a directory.** <br>
Example in the script: <br>
if os.path.isdir(file_path): <br>
    continue <br>
This skips directories during the file organization process. <br>

_os.mkdir():_ <br>
**Creates a new directory.** <br>
Example in the script: <br>

_os.mkdir(folder_path)_ <br>
**This creates a folder for each file type if it doesn’t already exist**.


**2. shutil Module** <br>
The shutil module provides high-level file operations such as copying, moving, and deleting files or directories.

Key Functions Used in organize_files.py: 

_shutil.move():_ <br>
Moves a file or directory to a new location.

Example in the script: <br>
shutil.move(file_path, os.path.join(base_path, folder, file_name)) <br>
This moves files into their respective folders based on their extensions.

If the destination directory doesn’t exist, the operation fails. That’s why the script ensures folders are created using os.mkdir() before moving files.

How They Work Together in organize_files.py: <br>

Directory Traversal: <br>
os.listdir() lists all items in the directory (base_path). <br>
Each item is checked with os.path.isdir() to differentiate between files and folders. <br>

Folder Creation: <br>
The script uses os.path.exists() and os.mkdir() to create folders for file types if they don't already exist. <br>

File Movement: <br>
The script uses shutil.move() to relocate files into appropriate folders based on their extensions. <br>
Path Management: <br>

The script uses os.path.join() to construct paths in a cross-platform way, ensuring compatibility with macOS, Windows, and Linux. <br>
Benefits of Using os and shutil: <br>
Cross-platform compatibility: Handles file paths, creation, and movement regardless of the operating system. <br>
Ease of file operations: Simplifies common file operations like moving, copying, and deleting files. <br>
Error handling: Functions like os.path.exists() prevent issues like trying to recreate existing directories. <br>
