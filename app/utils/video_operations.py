from app.utils.db_operations import *
from app.utils.files_operations import *
from datetime import datetime
import os

# there are functions for all videos manipulating in app


def move_in_videos_collection(collection: list, offset: int):
    """
        Moves through a collection of videos based on the offset.

        Parameters:
        - collection (list): The list of videos.
        - offset (int): The current offset in the collection.

        Returns:
        - tuple: A tuple containing the next two items in the collection,
                 a flag indicating the first item, and a flag indicating the last item.
    """

    next_item_1 = None
    next_item_2 = None

    first_item_flag = False
    last_item_flag = False
    try:
        index_first = offset + 0
        if index_first == 0:
            first_item_flag = True
        index_second = offset + 1
        next_item_1 = collection[index_first]
        next_item_2 = collection[index_second]
    except Exception:
        last_item_flag = True

    return next_item_1, next_item_2, first_item_flag, last_item_flag


def change_offset_in_collection(offset: int, collection_count: int, direction_up: bool = True):
    """
        Calculate the offset in a collection of items based on the direction.

        Parameters:
        - offset (int): The current offset in the collection.
        - collection_count (int): The total count of items in the collection.
        - direction_up (bool): Flag indicating the direction of the change. Default is True (up).

        Returns:
        - int: The updated offset in the collection.
    """

    if direction_up:
        if offset > 0:
            offset -= 2
    else:
        if offset < collection_count - 2:
            offset += 2
    return offset


def edit_video(data: dict, database: str, with_replace: bool, replace_from_path: str, replace_to_path: str):
    """
        Edits a video entry in the database and optionally replaces a file.

        Parameters:
        - data (dict): The video data to be updated.
        - database (str): The path to the database.
        - with_replace (bool): Flag indicating whether to replace a file.
        - replace_from_path (str): The original file path.
        - replace_to_path (str): The new file path.

        Raises:
        - EditVideoError: If an error occurs during the editing process.

        Returns:
        - None
    """

    try:
        update_video_db(database, data)
        if with_replace:
            os.rename(replace_from_path, replace_to_path)
    except Exception as err:
        raise EditVideoError(err)


def delete_video(video: dict, database: str, full_delete: bool):
    """
        Deletes a video entry from the database and optionally deletes the video file.

        Parameters:
        - video (dict): The video information.
        - database (str): The path to the database.
        - full_delete (bool): Flag indicating whether to fully delete the video.

        Raises:
        - DeleteVideoError: If an error occurs during the deletion process.

        Returns:
        - None
    """
    try:
        path_to_video_file = video['video_path']
        video_id = video['id']
        delete_video_db(database, video_id)

        if full_delete:
            if os.path.exists(path_to_video_file):
                os.remove(path_to_video_file)

    except Exception as err:
        raise DeleteVideoError(err)


def add_video(database: str, data: dict, path_to_save: str):
    """
        Adds a video to the database and saves the video icon to a specified path.

        Parameters:
        - database (str): The path to the database.
        - data (dict): The video data to be added.
        - path_to_save (str): The path to save the video.

        Raises:
        - AddingDownloadVideoDatabaseError: If an error occurs during the video addition process.

        Returns:
        - None
    """

    try:
        last_id = int(create_video_db(database, data))

        icon_name = str(last_id)
        temp_icon = data["video_icon"]
        icon_extension = get_file_extension(temp_icon)
        new_icon = get_full_path(f"{path_to_save}/{icon_name}.{icon_extension}")

        os.rename(temp_icon, new_icon)

        data["video_icon"] = new_icon
        data["id"] = last_id

        update_video_db(database, data)
    except Exception as err:
        raise AddingDownloadVideoDatabaseError(err)


def check_new_data_for_edit_video(new_video_data: dict):
    """
        Checks new data for editing a video.

        Parameters:
        - new_video_data (dict): The new data for the video.

        Returns:
        - bool: True if all checks pass, False otherwise.

        Raises:
        - CheckingDataForVideoError: If an error occurs during the data checking process.

        Returns:
        - None
    """

    try:
        first_check = check_directory_for_existence(new_video_data['video_path'])
        third_check = check_directory_for_existence(new_video_data['video_path'])
        second_check = check_file_name(new_video_data['video_name'])

        if not first_check or not second_check or not third_check:
            return False
        else:
            return True
    except Exception as err:
        raise CheckingDataForVideoError(err)


def check_data_for_downloading_video(data: dict):
    """
        Checks data for downloading a video.

        Parameters:
        - data (dict): The data related to the video.

        Returns:
        - bool: True if the data is valid for downloading, False otherwise.
    """

    path = data['path']
    if path == "default":
        return True
    first_check = check_directory_for_existence(path)

    if first_check:
        return True
    else:
        return False


def prepare_data_for_downloading(data: dict, path_to_download: str):
    """
        Prepares data for downloading a video.

        Parameters:
        - data (dict): The video data.
        - path_to_download (str): The default download path.

        Returns:
        - tuple: A tuple containing the updated path and format.
    """

    format = data['format']
    path = data['path']
    if path == "default":
        path = get_full_path(path_to_download)
    return path, format


def prepare_new_data_for_downloaded_video(video_file_path: str, preview_file_path: str):
    """
        Prepares new data for a downloaded video.

        Parameters:
        - video_file_path (str): The path to the video file.
        - preview_file_path (str): The path to the video preview file.

        Returns:
        - dict: The prepared video data.

        Raises:
        - PreparingDownloadedVideoDataError: If an error occurs during the data preparation process.
    """

    try:
        creation_time = os.path.getctime(video_file_path)
        date = datetime.fromtimestamp(creation_time).strftime('%d.%m.%Y')
        name = get_file_name(absolute_path=video_file_path)
        format = get_file_extension(absolute_path=video_file_path, with_dot=False)
        icon = get_full_path(preview_file_path)
        icon = normalize_path(icon)
        full_path = normalize_path(video_file_path)

        video_data = {
            "video_name": name,
            "video_desc": "empty",
            "video_format": format,
            "video_date": date,
            "video_path": full_path,
            "video_icon": icon
        }
        return video_data
    except Exception as err:
        raise PreparingDownloadedVideoDataError(err)


def prepare_new_data_for_editing_video(video_for_edit: dict, new_data: dict):
    """
        Prepares new data for editing a video.

        Parameters:
        - video_for_edit (dict): The video data to be edited.
        - new_data (dict): The new data for the video.

        Returns:
        - bool: Flag indicating whether the video path needs to be replaced.
    """

    id = video_for_edit['id']
    date = video_for_edit['video_date']
    format = video_for_edit['video_format']

    new_path = new_data['video_path']
    new_name = new_data['video_name']
    new_desc = new_data['video_desc']
    new_icon = new_data['video_icon']

    new_full_path = f"{new_path}/{new_name}.{format}"
    old_full_path = video_for_edit['video_path']

    replace_flag = True if new_full_path != old_full_path else False

    new_data['id'] = id
    new_data['video_format'] = format
    new_data['video_date'] = date
    new_data['video_icon'] = new_icon
    new_data['video_path'] = new_full_path
    new_data['video_name'] = new_name
    new_data['video_desc'] = new_desc

    return replace_flag


def get_nonexistence_videos_in_db(database: str):
    """
        Retrieves videos that do not exist in the specified database.

        Parameters:
        - database (str): The database name.

        Returns:
        - list: List of videos to be removed.
    """
    videos_to_remove = []
    video_records = read_videos_db(database)

    if not video_records is None:

        for video in video_records:
            video_path = video['video_path']
            icon_path = video['video_icon']
            if os.path.exists(video_path):
                if not os.path.exists(icon_path):
                    videos_to_remove.append(video)
            else:
                videos_to_remove.append(video)
    return videos_to_remove