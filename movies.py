import os
import shutil
from tqdm import tqdm

# Set the directory path where the movies are stored
directory = os.getcwd()

# Count the total number of subtitle files
total_files = sum(1 for movie_folder in os.listdir(directory) if os.path.isdir(os.path.join(directory, movie_folder)) and os.path.isdir(os.path.join(directory, movie_folder, 'Subs')))
files_processed = 0

# Loop through each movie folder
for movie_folder in os.listdir(directory):
    # Check if the current item in the directory is a folder
    if os.path.isdir(os.path.join(directory, movie_folder)):
        # Check if the Subs folder exists in the movie folder
        subs_folder = os.path.join(directory, movie_folder, 'Subs')
        if os.path.isdir(subs_folder):
            # Initialize the progress bar
            with tqdm(total=len(os.listdir(subs_folder)), desc=movie_folder) as pbar:
                # Loop through each subtitle file in the Subs folder
                for subtitle_file in os.listdir(subs_folder):
                    # Get the extension of the subtitle file
                    subtitle_ext = os.path.splitext(subtitle_file)[1]
                    # Construct the new subtitle file name
                    new_subtitle_name = movie_folder + '.en-US' + subtitle_ext
                    # Move the subtitle file to the same folder as the movie and rename it with the new name
                    shutil.move(os.path.join(subs_folder, subtitle_file), os.path.join(directory, movie_folder, new_subtitle_name))
                    # Update the progress bar
                    pbar.update(1)
                    files_processed += 1
                    # Calculate and print the progress percentage
                    progress = (files_processed / total_files) * 100
                    print(f'Progress: {progress:.2f}%')
                # Delete the Subs folder
                os.rmdir(subs_folder)
