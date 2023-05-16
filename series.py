import os
import shutil
from tqdm import tqdm

# Set the directory path where the TV shows are stored
directory = os.getcwd()

# Count the total number of subtitle files
total_files = 0
for show_folder in os.listdir(directory):
    if os.path.isdir(os.path.join(directory, show_folder)):
        subs_folder = os.path.join(directory, show_folder, 'Subs')
        if os.path.isdir(subs_folder):
            total_files += sum(1 for episode_folder in os.listdir(subs_folder) if os.path.isdir(os.path.join(subs_folder, episode_folder)))

# Loop through each TV show folder
files_processed = 0
for show_folder in os.listdir(directory):
    # Check if the current item in the directory is a folder
    if os.path.isdir(os.path.join(directory, show_folder)):
        # Check if the Subs folder exists in the TV show folder
        subs_folder = os.path.join(directory, show_folder, 'Subs')
        if os.path.isdir(subs_folder):
            # Initialize the progress bar
            with tqdm(total=sum(1 for episode_folder in os.listdir(subs_folder) if os.path.isdir(os.path.join(subs_folder, episode_folder))), desc=show_folder) as pbar:
                # Loop through each episode folder in the Subs folder
                for episode_folder in os.listdir(subs_folder):
                    # Check if the current item in the directory is a folder
                    if os.path.isdir(os.path.join(subs_folder, episode_folder)):
                        # Loop through each subtitle file in the episode folder
                        for subtitle_file in os.listdir(os.path.join(subs_folder, episode_folder)):
                            # Check if the current item in the directory is a file and is a subtitle file
                            if os.path.isfile(os.path.join(subs_folder, episode_folder, subtitle_file)) and subtitle_file.endswith(('.srt')):
                                # Get the extension of the subtitle file
                                subtitle_ext = os.path.splitext(subtitle_file)[1]
                                # Construct the new subtitle file name
                                new_subtitle_name = episode_folder + '.en-US' + subtitle_ext
                                # Move the subtitle file to the parent folder of the episode and rename it with the new name
                                shutil.move(os.path.join(subs_folder, episode_folder, subtitle_file), os.path.join(os.path.join(subs_folder, os.pardir), new_subtitle_name))
                                files_processed += 1
                                # Update the progress bar
                                pbar.update(1)
                                # Calculate and print the progress percentage
                                progress = (files_processed / total_files) * 100
                                print(f'Progress: {progress:.2f}%')
            # Delete the Subs folder
            shutil.rmtree(subs_folder)
