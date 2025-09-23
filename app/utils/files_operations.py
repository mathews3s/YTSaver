from app.utils.app_exceptions import *
import shutil
import os
import uuid
import re
import ffmpeg

# there are functions for files manipulating in app


def clear_directory(directory: str):
    """
        Clears all files and subdirectories in the specified directory.

        Parameters:
        - directory (str): The path to the directory to be cleared.

        Raises:
        - ClearingDirectoryError: If an error occurs while clearing the directory.

        Returns:
        -None
    """

    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as err:
            raise ClearingDirectoryError(err)


def make_directories_if_not_exist(paths_dict: dict):
    """
        Creates directories if they do not exist based on the paths provided in the dictionary.

        Parameters:
        - paths_dict (dict): A dictionary where keys are folder names and values are folder paths.

        Raises:
        - AppDirectoriesConstructingError: If an error occurs while creating directories.

        Returns:
        -None
    """

    for folder_name, folder_path in paths_dict.items():
        try:
            os.makedirs(folder_path, exist_ok=True)
        except Exception as err:
            raise AppDirectoriesConstructingError(err)


def get_file_extension(absolute_path: str, with_dot: bool = True):
    """
        Extracts the file extension.

        Parameters:
        - absolute_path (str): The absolute path of the file.
        - with_dot (bool): If True, includes the dot in the returned extension. Default is True.

        Returns:
        - str: The file extension with or without the dot based on the 'with_dot' parameter.
    """

    if with_dot:
        return os.path.splitext(absolute_path)[1]
    else:
        return os.path.splitext(absolute_path)[1][1:]


def get_file_name(absolute_path: str):
    """
        Extracts the file name (without extension) from the provided absolute path.

        Parameters:
        - absolute_path (str): The absolute path of the file.

        Returns:
        - str: The file name without the extension.
    """
    return os.path.splitext(os.path.basename(absolute_path))[0]


def normalize_path(path: str):
    """
        Normalizes the path by replacing backslashes with forward slashes.

        Parameters:
        - path (str): The path to be normalized.

        Returns:
        - str: The normalized path with backslashes replaced by forward slashes.
    """

    standardized_path = path.replace("\\", "/")
    return standardized_path


def generate_unique_filename():
    """
        Generates a unique filename using uuid4.

        Returns:
        - str: A unique filename generated using uuid4.
    """

    unique_filename = str(uuid.uuid4())
    return unique_filename


def check_directory_for_existence(path: str):
    """
        Checks the existence of a directory at the specified path.
        If the directory does not exist, it creates the directory.

        Parameters:
        - path (str): The path of the directory to check.

        Returns:
        - bool: True if the directory exists, False otherwise.
    """

    if not os.path.exists(path):
        os.makedirs(path)
        return False
    else:
        return True


def check_file_exist(path_to_file: str):
    """
        Checks the existence of a file at the specified path.

        Parameters:
        - path (str): The path of the filey to check.

        Returns:
        - bool: True if the file exists, False otherwise.
    """

    if not os.path.exists(path_to_file):
        return False
    else:
        return True


def get_full_path(path: str):
    """
        Returns the absolute path of the specified path.

        Parameters:
        - path (str): The path to get the absolute path for.

        Returns:
        - str: The absolute path of the specified path.
    """

    return os.path.abspath(path)


def check_file_name(path: str):
    """
        Checks if the provided file name is valid.

        Parameters:
        - path (str): The file name to be checked.

        Returns:
        - bool: True if the file name is valid, False otherwise.
    """

    pattern = r'^[\w\sа-яА-ЯёЁ\-_.]+$'
    if re.match(pattern, path):
        return True
    else:
        return False


def concat_audio_video_files(video_file: str, audio_file: str, output_temp_video_path: str,
                             output_temp_name: str, output_path: str):
    """
        Concatenates audio file with video file and saves the output video.

        Parameters:
        - video_file (str): Path to the temp video file.
        - audio_file (str): Path to the temp audio file.
        - output_temp_video_path (str): Path where temporary video files are saved.
        - output_temp_name (str): Name of the temporary video file.
        - output_path (str): Path where the final output video will be saved.

        Returns:
        - str: Path to the final output video file.

        Raises:
        - FfmpegError: If an error occurs during the ffmpeg operation.
    """

    try:
        input_video = ffmpeg.input(video_file)
        input_audio = ffmpeg.input(audio_file)

        output_format = get_file_extension(video_file)
        output_temp_video_name = output_temp_name + output_format
        output_temp_video = os.path.join(output_temp_video_path, output_temp_video_name)

        ffmpeg.output(input_video, input_audio, output_temp_video, codec='copy').overwrite_output().run(quiet=True)

        auto_name = generate_unique_filename() + output_format
        output_video = os.path.join(output_path, auto_name)

        os.rename(output_temp_video, output_video)

        return output_video

    except Exception as err:
        raise FfmpegError(err)
