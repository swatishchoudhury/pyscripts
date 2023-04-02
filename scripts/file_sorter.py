"""
File Sorter - A Python script that sorts files into subdirectories based on their file type.

Open the messy folder and run the script.
Optional: You can customize it according to your preference in file_type dictionary.

Usage:
python file_sorter.py

This script is open source and available on GitHub at https://github.com/swatishchoudhury/pyscripts.
"""

import os
import shutil
import sys

disclaimer = """This script sorts files into subdirectories based on their file type.
Although it is secure and non-destructive, it is possible that it may accidentally move
files or cause data loss. By typing "y," you acknowledge that you have reviewed the script
and your file directory and assume full responsibility for any data loss or unexpected results.
It is strongly recommended that you back up your files before using this script.

Do you really want to continue? Send y to continue, any other key to exit:  """

answer = input(disclaimer)
if answer != "y":
    sys.exit()

# Add or Remove file types and directories as per your preferences
file_types = {
    ".png": "Images",
    ".jpg": "Images",
    ".jpeg": "Images",
    ".gif": "Images",
    ".webp": "Images",
    ".svg": "Images",
    ".tif": "Images",
    ".tiff": "Images",
    ".mp4": "Videos",
    ".mkv": "Videos",
    ".mov": "Videos",
    ".mp3": "Audios",
    ".m4a": "Audios",
    ".flac": "Audios",
    ".wav": "Audios",
    ".txt": "Texts",
    ".pdf": "PDFs",
    ".rtf": "Word Docs",
    ".doc": "Word Docs",
    ".docx": "Word Docs",
    ".pages": "Word Docs",
    ".odt": "Word Docs",
    ".xls": "Spreadsheets",
    ".xlsx": "Spreadsheets",
    ".csv": "Spreadsheets",
    ".key": "Presentation Files",
    ".ppt": "Presentation Files",
    ".pptx": "Presentation Files",
    ".odp": "Presentation Files",
    ".zip": "Compressed Files",
    ".rar": "Compressed Files",
    ".exe": "Softwares",
    ".msi": "Softwares",
    ".epub": "EBooks",
}

src_dir = os.path.dirname(os.path.abspath(__file__))

moved_extensions = set()

for file_name in os.listdir(src_dir):
    file_path = os.path.join(src_dir, file_name)

    if os.path.isfile(file_path):
        _, file_ext = os.path.splitext(file_path)
        file_ext = file_ext.lower()

        if file_ext in file_types and file_ext not in moved_extensions:
            dir_name = file_types[file_ext]
            dir_path = os.path.join(src_dir, dir_name)
            os.makedirs(dir_path, exist_ok=True)
            dst_file_path = os.path.join(dir_path, file_name)
            counter = 1

            while os.path.exists(dst_file_path):
                new_file_name = (
                    f"{os.path.splitext(file_name)[0]} ({counter}){file_ext}"
                )
                dst_file_path = os.path.join(dir_path, new_file_name)
                counter += 1
            shutil.move(file_path, dst_file_path)
