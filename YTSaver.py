from app.src.controller import *
from app.src.model import *
from app.src.view import *
import sys


def construct_resources():
    """
        Construct paths and filenames for various resources based on the current working directory.

        Returns:
        - paths_for_install (dict): A dictionary containing app folders paths for constructing including:
            - 'download_folder'
            - 'app_folder'
            - 'app_data_folder'
            - 'database_folder'
            - 'video_icons_folder'
            - 'app_icons_folder'
            - 'temp_data_folder'
            - 'utils_folder'

        - filenames_for_install (dict): A dictionary containing filenames for installation including:
            - 'ffmpeg_installer_filename'
            - 'ffmpeg_checker_filename'
            - 'db_filename'
            - 'temp_preview_filename'
            - 'app_icon_filename'
    """

    # getting current work directory
    if getattr(sys, 'frozen', False):
        base_dir = os.path.dirname(sys.executable)
    else:
        base_dir = os.path.dirname(os.path.abspath(__file__))

    paths_for_install = {
        "download_folder": os.path.join(base_dir, 'download'),
        "app_folder": os.path.join(base_dir, 'app'),
        "app_data_folder": os.path.join(base_dir, 'app', 'appData'),
        "database_folder": os.path.join(base_dir, 'app', 'appData', 'database'),
        "video_icons_folder": os.path.join(base_dir, 'app', 'appData', 'videoIcons'),
        "app_icons_folder": os.path.join(base_dir, 'app', 'appData', 'appIcons'),
        "temp_data_folder": os.path.join(base_dir, 'app', 'appData', 'temp'),
        "utils_folder": os.path.join(base_dir, 'app', 'appData', 'utility'),
    }

    filenames_for_install = {
        "ffmpeg_installer_filename": os.path.join(base_dir, 'app', 'appData', 'utility', 'FFmpegInstaller.bat'),
        "ffmpeg_checker_filename": os.path.join(base_dir, 'app', 'appData', 'utility', 'FFmpegChecker.bat'),
        "db_filename": os.path.join(base_dir, 'app', 'appData', 'database', 'database.db'),
        "temp_preview_filename": os.path.join(base_dir, 'app', 'appData', 'temp', 'preview.jpg'),
        "app_icon_filename": os.path.join(base_dir, 'app', 'appData', 'appIcons', 'YTS.ico'),
    }

    return paths_for_install, filenames_for_install

if __name__ == "__main__":
    paths, files = construct_resources()
    controller = Controller(Model(), View(), paths, files)

