import os
import shutil

# get the current working directory (cwd)
dir_path = os.getcwd()

for filename in os.listdir(dir_path):
    # Get the full path of the file
    filepath = os.path.join(dir_path, filename)

    # Check if the file is a regular file (not a directory)
    if os.path.isfile(filepath):
        # Get the file's basename (without the extension)
        basename = os.path.splitext(filename)[0]

        # Create a new directory with the same basename (without "pt-BR")
        new_dirname = basename.replace("pt-BR", "")
        new_dirpath = os.path.join(dir_path, new_dirname)
        os.makedirs(new_dirpath, exist_ok=True)

        # Move the file to the new directory
        shutil.move(filepath, os.path.join(new_dirpath, filename))
