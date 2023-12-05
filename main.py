import os
import shutil

# Define the source directory where the downloaded files are located
source_directory = "/path/to/downloads"

# Define the destination directories for different file types
destination_directories = {
    "MP3": "/path/to/music/folder",
    "PDF": "/path/to/documents/folder",
    "TXT": "/path/to/documents/folder",
    "CSV": "/path/to/documents/folder",
    "ZIP": "/path/to/zip/folder",
    "EXE": "/path/to/apps/folder",
    "SVG": "/path/to/svg/folder",
    "GIF": "/path/to/videos/folder",
    "DOC": "/path/to/documents/folder",
    "XLS": "/path/to/documents/folder",
    # Add more file extensions and corresponding destination directories here
}

# Iterate through the files in the source directory
for filename in os.listdir(source_directory):
    file_path = os.path.join(source_directory, filename)
    
    # Check if the item is a file
    if os.path.isfile(file_path):
        # Get the file extension
        file_extension = os.path.splitext(filename)[1][1:].lower()
        
        # Determine the destination directory based on the file extension
        if file_extension in destination_directories:
            destination_directory = destination_directories[file_extension]
        else:
            destination_directory = "/path/to/other/folder"
        
        # Move the file to the appropriate destination directory
        shutil.move(file_path, destination_directory)
