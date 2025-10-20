# import os
# import shutil

# path = input("Enter the path of the folder to organize: ")
# files = os.listdir(path)

# for file in files:
#     filename, file_extension = os.path.splitext(file)
#     file_extension = file_extension[1:]  # Remove the dot from extension

#     if os.path.exists(path+"/"+file_extension):
#         shutil.move(path+"/"+file, path+"/"+file_extension+"/"+file)

#     else:
#         os.makedirs(path+"/"+file_extension)
#         shutil.move(path+"/"+file, path+"/"+file_extension+"/"+file)

import os
import shutil

def organize_folder(path):
    # Get all files in the directory
    files = os.listdir(path)

    for file in files:
        file_path = os.path.join(path, file)

        # Skip directories
        if os.path.isdir(file_path):
            continue

        # Split file name and extension
        filename, file_extension = os.path.splitext(file)
        file_extension = file_extension[1:]  # Remove the dot

        # Skip files without extensions
        if not file_extension:
            continue

        # Create the target folder if it doesn’t exist
        target_folder = os.path.join(path, file_extension)
        os.makedirs(target_folder, exist_ok=True)

        # Move the file
        shutil.move(file_path, os.path.join(target_folder, file))
        print(f"Moved: {file} → {target_folder}")

if __name__ == "__main__":
    folder_path = input("Enter the path of the folder to organize: ").strip()

    if os.path.exists(folder_path):
        organize_folder(folder_path)
        print("\n✅ All files have been organized successfully!")
    else:
        print("❌ Folder not found! Please check your path and try again.")


        