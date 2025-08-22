import os

# Base folder
base_folder = r"C:\first data work"

# Folders to clean
folders = ["train-db", "test-db"]

# Loop through each folder
for folder in folders:
    folder_path = os.path.join(base_folder, folder)
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.lower().endswith(".mp3"):
                file_path = os.path.join(root, file)
                os.remove(file_path)
                print(f"Deleted: {file_path}")
