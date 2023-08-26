"""
This module defines the functions that deal with file handling.
"""
import os
import glob
import shutil


def video_recordings(path: str, video_formats=['mp4', 'mkv', 'avi', 'mpg']) -> list[str]:
    """
    Generates a list of video files present in the given path.

    :param path: path to the folder where you need to check for video recordings.
    :type path: str
    :param video_formats: supported formats; default = ['mp4', 'mkv', 'avi', 'mpg']
    :type video_formats: list[str], optional

    :return: the list of video files present in the given folder    
    :rtype: list[str]
    """
    video_files = []
    for format_pattern in video_formats:
        video_files.extend(glob.glob(os.path.join(path, f'*.{format_pattern}')))
    return video_files
    

def construct_path(base_path: str, sub_dirs: list[str]) -> str:
    """
    Given a base path and a list of directory names, this function creates a path 
    by concatenating the base path and the directory names in a way that's independent of 
    which OS you're running the app from.
    
    :param base_path: the base path from which to begin to the path construction.
    :type base_path: str
    :param sub_dirs: a list of directory names; the path created will reflect the order of the directories listed here.
    :type sub_dirs: list[str]

    :return: the constructed path
    :rtype: str
    """
    return os.path.join(base_path, *sub_dirs)


def organize_recorded_files(src_path: str, dest_path: str) -> int:
    """
    Defines the main organization logic for the app. The file organization is done as follows:
        - Move the recordings from a given source folder to the given destination
        - Determine the order in which the recordings were created
        - Rename the files with natural numbers in that order continuing on from the largest numbered file previously stored in that folder.

    :param src_path: path to the source folder
    :type src_path: str
    :param dest_path: path to the destination folder
    :type dest_path: str

    :return: number of files transferred
    :rtype: int
    """
    # Create the destination folder if does not already exist. 
    os.makedirs(dest_path, exist_ok=True)

    # Get a list of recorded files in the source directory.
    current_session_files = video_recordings(src_path)

    # Sort the recorded files based on their creation time.
    current_session_files.sort(key=os.path.getctime)

    # Get the highest file number already present in the destination directory.
    prev_files = video_recordings(dest_path)
    highest_number = len(prev_files)

    # Move and rename the recorded files to the destination directory.
    for i, file_path in enumerate(current_session_files):
        # Rename the file with the next available number.
        new_file_name = str(highest_number + (i+1)) + os.path.splitext(file_path)[1]
        new_file_path = os.path.join(dest_path, new_file_name)
        shutil.move(file_path, new_file_path)

    return len(current_session_files)
