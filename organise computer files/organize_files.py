import os
import shutil

# Define the file extensions and their target folders
file_types = {
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"],
    "Videos": [".mp4", ".mkv", ".mov", ".avi"],
    "Music": [".mp3", ".wav", ".aac"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Code": [".py", ".java", ".html", ".css", ".js", ".cpp"],
    "Others": []  # For files with extensions not explicitly mentioned
}

# Set the directory to organize (e.g., Desktop or Downloads)
directory_to_organize = os.path.expanduser("~/Documents")  # Change this path as needed

# Create folders for each file type
def create_folders(base_path, folders):
    for folder in folders:
        folder_path = os.path.join(base_path, folder)
        if not os.path.exists(folder_path):
            os.mkdir(folder_path)

# Move files into their respective folders
def organize_files(base_path, file_types):
    for file_name in os.listdir(base_path):
        file_path = os.path.join(base_path, file_name)
        # Skip directories
        if os.path.isdir(file_path):
            continue

        # Determine file type and move it
        moved = False
        for folder, extensions in file_types.items():
            if any(file_name.lower().endswith(ext) for ext in extensions):
                shutil.move(file_path, os.path.join(base_path, folder, file_name))
                moved = True
                break

        # Move to "Others" if no matching extension found
        if not moved:
            shutil.move(file_path, os.path.join(base_path, "Others", file_name))

# Main function
def main():
    print(f"Organizing files in: {directory_to_organize}")
    create_folders(directory_to_organize, file_types.keys())
    organize_files(directory_to_organize, file_types)
    print("File organization complete!")

if __name__ == "__main__":
    main()
