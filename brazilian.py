import os
from tqdm import tqdm

# get the current working directory (cwd)
directory = os.getcwd()

# Count the total number of files to process
total_files = 0
for movie_folder in os.listdir(directory):
    if os.path.isdir(os.path.join(directory, movie_folder)):
        total_files += sum(1 for filename in os.listdir(os.path.join(directory, movie_folder)) if ".pt-BR.srt" in filename)

# Loop through each movie folder in the directory
files_processed = 0
for movie_folder in os.listdir(directory):
    # Check if the current item in the directory is a folder
    if os.path.isdir(os.path.join(directory, movie_folder)):
        # Loop through each file in the movie folder
        for filename in tqdm(os.listdir(os.path.join(directory, movie_folder)), desc=movie_folder):
            # Check if the filename contains ".pt-BR.srt"
            if ".pt-BR.srt" in filename:
                # Get the new name for the file
                new_name = movie_folder + ".pt-BR.srt"
                # Rename the file
                os.rename(
                    os.path.join(directory, movie_folder, filename),
                    os.path.join(directory, movie_folder, new_name)
                )
                files_processed += 1
                # Calculate and print the progress percentage
                progress = (files_processed / total_files) * 100
                print(f'Progress: {progress:.2f}%')