"""
Video Compressor - A Python script that compresses video files in a directory and its subdirectories using ffmpeg.

This script searches through a specified directory for video files and compresses them using ffmpeg, saving the compressed files in a subdirectory. The compression settings can be adjusted within the script.

Usage:
python compress_videos.py

Prerequisite:
- ffmpeg: Make sure ffmpeg is installed on your system. You can download it from https://ffmpeg.org/download.html

Note: You can customize the video compression settings by modifying the command list in the compress_video function.

This script is open source and available on GitHub at https://github.com/swatishchoudhury/pyscripts.

"""

import os
import subprocess
from pathlib import Path


def compress_video(input_path, output_path):
    command = [
        "ffmpeg",
        "-i",
        str(input_path),
        "-c:v",
        "libx264",
        "-crf",
        "25",  # crf - quality vs file size trade-off. lower the value, better the quality range(0, 51)
        "-preset",
        "medium",  # preset - encoding speed vs compression efficiency
        "-c:a",
        "aac",
        "-b:a",
        "128k",
        str(output_path),
    ]

    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while compressing {input_path}: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


def process_directory(directory):
    video_extensions = (".mp4", ".mkv", ".mts")  # Add more video file extension here
    compressed_folder = Path(directory) / f"compressed_{Path(directory).name}"
    compressed_folder.mkdir(exist_ok=True)

    for root, _, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(video_extensions):
                input_path = Path(root) / file
                relative_path = input_path.relative_to(directory)
                output_path = compressed_folder / relative_path

                output_path.parent.mkdir(parents=True, exist_ok=True)

                print(f"Compressing: {input_path}")
                compress_video(input_path, output_path)
                print(f"Compressed video saved: {output_path}")


if __name__ == "__main__":
    try:
        current_directory = os.getcwd()
        process_directory(current_directory)
        print("Video compression completed.")
    except Exception as e:
        print(f"An error occurred: {e}")
