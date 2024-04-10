import os
import shutil

def organize_files(folder_path):
    # Dictionary to store file extensions and their corresponding folders
    extensions = {
        "Documents": [".pdf", ".doc", ".docx", ".txt", ".xlsx", ".pptx"],
        "Images": [".jpg", ".jpeg", ".png", ".gif"],
        "Videos": [".mp4", ".mov", ".avi"],
        "Audios": [".mp3", ".wav"],
        "Archives": [".zip", ".rar", ".tar", ".gz"],
        "Scripts": [".py", ".sh", ".bat"],
        "Others": []  # Default folder for other file types
    }

    # Create folders if they don't exist already
    for folder in extensions.keys():
        folder_path_new = os.path.join(folder_path, folder)
        os.makedirs(folder_path_new, exist_ok=True)

    # Iterate through each file in the directory
    for file in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, file)):
            # Get file extension
            _, extension = os.path.splitext(file)

            # Move file to corresponding folder based on extension
            moved = False
            for folder, ext_list in extensions.items():
                if extension.lower() in ext_list:
                    # Move the file
                    shutil.move(
                        os.path.join(folder_path, file),
                        os.path.join(folder_path, folder, file)
                    )
                    moved = True
                    break

            # If file doesn't belong to any category, move it to 'Others' folder
            if not moved:
                # Move the file
                shutil.move(
                    os.path.join(folder_path, file),
                    os.path.join(folder_path, "Others", file)
                )

if __name__ == "__main__":
    folder_path = input("Enter the path of the folder to organize: ")
    organize_files(folder_path)
    print("Files organized successfully!")