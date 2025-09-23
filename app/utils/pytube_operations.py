from app.utils.app_exceptions import *
from app.utils.files_operations import *
from pytubefix import YouTube
import requests

# there are functions for pytube manipulating in app


def get_youtube_video_if_exist(link: str, progress_func, complete_func):
    """
        Retrieves a YouTube video if it exists.

        Parameters:
        - link (str): The URL of the YouTube video.
        - progress_func: The function to call during download progress.
        - complete_func: The function to call when the download is complete.

        Returns:
        - YouTube: The pytube video object.

        Raises:
        - FindingVideoError: If an error occurs while finding the video.
    """

    try:
        pytube_obj = YouTube(link, on_progress_callback=progress_func, on_complete_callback=complete_func)
        return pytube_obj
    except Exception as err:
        raise FindingVideoError(err)


def get_common_info_youtube_video(pytube_obj):
    """
        Retrieves common information about a YouTube video.

        Parameters:
        - pytube_obj: The pytube video object.

        Returns:
        - tuple: A tuple containing the title and thumbnail URL of the video.

        Raises:
        - CommonDataFetchError: If an error occurs while fetching common data.
    """

    try:
        return pytube_obj.title, pytube_obj.thumbnail_url
    except Exception as err:
        raise CommonDataFetchError(err)


def get_list_of_all_resolutions(streams):
    """
        Extracts a list of all unique resolutions from a list of video streams.

        Parameters:
        - streams: List of video streams.

        Returns:
        - list: A list of unique resolutions available in the video streams.
    """

    resolutions = []
    for stream in streams:
        resolution = stream.resolution
        if resolution and resolution not in resolutions:
            resolutions.append(resolution)
    return resolutions


def get_list_of_all_formats(streams):
    """
        Extracts a list of all unique formats from a list of video streams.

        Parameters:
        - streams: List of video streams.

        Returns:
        - list: A list of unique formats available in the video streams.
    """

    formats = []
    for stream in streams:
        format = stream.subtype
        if format and format not in formats:
            formats.append(format)
    return formats


def get_list_of_all_fps(streams):
    """
        Extracts a list of all unique frame rates (fps) from a list of video streams.

        Parameters:
        - streams: List of video streams.

        Returns:
        - list: A list of unique frame rates (fps) available in the video streams.
    """

    result = []
    for stream in streams:
        fps = stream.fps
        if fps and fps not in result:
            result.append(fps)
    return result


def get_all_video_streams(all_streams):
    """
        Filters and retrieves only video streams from a list of all streams.

        Parameters:
        - all_streams: List of all available streams.

        Returns:
        - list: A list of video streams.
    """

    video_streams = all_streams.filter(progressive=False, only_video=True)
    return video_streams


def download_stream(path_for_save: str, file_name: str, stream):
    """
        Downloads a video stream and saves it to the specified path.

        Parameters:
        - path_for_save (str): Path where the video will be saved.
        - file_name (str): Name of the downloaded file.
        - stream: Video stream object to download.

        Returns:
        - str: Path to the downloaded file.

        Raises:
        - DownloadStreamError: If an error occurs during the download process.
    """

    try:
        downloaded_file_path = stream.download(output_path=path_for_save)

        file_extension = get_file_extension(absolute_path=downloaded_file_path)
        new_file_name = file_name + file_extension
        new_file_path = os.path.join(path_for_save, new_file_name)
        os.rename(downloaded_file_path, new_file_path)

        return new_file_path
    except Exception as err:
        raise DownloadStreamError(err)


def preview_download(thumbnail_url: str, filename_for_save: str):
    """
        Downloads a preview thumbnail from a URL and saves it to a file.

        Parameters:
        - thumbnail_url (str): URL of the thumbnail image.
        - filename_for_save (str): Name of the file to save the thumbnail.

        Returns:
        - bool: True if download with code 200 and save are successful, False otherwise.

        Raises:
        - DownloadPreviewError: If an error occurs during the download and save process.
    """

    try:
        response = requests.get(thumbnail_url)

        if response.status_code == 200:
            file_name = filename_for_save
            with open(file_name, 'wb') as f:
                f.write(response.content)
                return True
        else:
            return False
    except Exception as err:
        raise DownloadPreviewError(err)