from app.src.controller import *
from app.src.model import *
from app.src.view import *
import sys


def construct_paths_for_resources():
    if getattr(sys, 'frozen', False):
        # Запущено как упакованный `.exe`
        base_dir = sys._MEIPASS
    else:
        # В режиме разработки или при запуске через интерпретатор
        base_dir = os.path.dirname(os.path.abspath(__file__))

    paths_for_install = {
        "download_app_folder": os.path.join(base_dir, 'download'),
        "app_folder": os.path.join(base_dir, 'app'),
        "app_data_folder": os.path.join(base_dir, 'app', 'appData'),
        "db_filename": os.path.join(base_dir, 'app', 'appData', 'database.db'),
        "save_icons_app_folder": os.path.join(base_dir, 'app', 'appData', 'videoIcons'),
        "temp_data_app_folder": os.path.join(base_dir, 'app', 'appData', 'temp'),
        "temp_preview_filename": os.path.join(base_dir, 'app', 'appData', 'temp', 'preview.jpg'),

    }


    return paths_for_install

if __name__ == "__main__":
    paths = construct_paths_for_resources()
    controller = Controller(Model(), View(), paths)

