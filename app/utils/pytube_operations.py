from pytubefix import YouTube
import requests
from app.utils.app_exceptions import *
from app.utils.files_operations import *

def get_youtube_video_if_exist(link, progress_func, complete_func):
    try:
        pytube_obj = YouTube(link, on_progress_callback=progress_func, on_complete_callback=complete_func)
        return pytube_obj
    except Exception as err:
        raise VideoStreamsDownloadError(err)


def get_common_info_youtube_video(pytube_obj):
    try:
        return pytube_obj.title, pytube_obj.thumbnail_url
    except Exception as err:
        raise CommonDataFetchError(err)

def get_list_of_all_resolutions(streams):
    resolutions = []
    for stream in streams:
        resolution = stream.resolution
        if resolution and resolution not in resolutions:
            resolutions.append(resolution)
    return resolutions

def get_list_of_all_formats(streams):
    formats = []
    for stream in streams:
        format = stream.subtype
        if format and format not in formats:
            formats.append(format)
    return formats

def get_list_of_all_fps(streams):
    result = []
    for stream in streams:
        fps = stream.fps
        if fps and fps not in result:
            result.append(fps)
    return result

def get_all_video_streams(all_streams):
    video_streams = all_streams.filter(progressive=False, only_video=True)
    return video_streams


def download_stream(path_for_save, file_name, stream):
    try:
        downloaded_file_path = stream.download(output_path=path_for_save)

        file_extension = get_file_extension(absolute_path=downloaded_file_path)
        new_file_name = file_name + file_extension
        new_file_path = os.path.join(path_for_save, new_file_name)
        os.rename(downloaded_file_path, new_file_path)

        return new_file_path
    except Exception as err:
        raise DownloadVideoStreamError(err)

def preview_download(thumbnail_url, filename_for_save):
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