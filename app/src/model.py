import copy
import threading
import subprocess
from app.utils.video_operations import *
from app.utils.pytube_operations import *
from app.utils.files_operations import *

class Model:

    def __init__(self):
        # attributes for keeping app file resources
        self.db_filename = None
        self.download_app_folder = None
        self.temp_data_folder = None
        self.download_icons_folder = None
        self.temp_preview_filename = None
        self.ffmpeg_installer_filename = None
        self.ffmpeg_checker_filename = None

        self.controller = None
        # attributes for keeping video pages information
        self.videos_collection = None
        self.videos_collection_count = 0
        self.first_video = None
        self.second_video = None
        self.selected_video = None
        self.offset_collection = 0
        # attributes for keeping pytube information
        self.pytube_instance = None
        self.pytube_info = {
            'suit_video_stream': None,
            'suit_audio_stream': None,
            'video_streams_all': None,
            'video_streams': None,
            'thumbnail_url': None,
            'video_name': None,
            'resolutions': None,
            'formats': None,
            'fps': None,
        }
        # attributes for keeping info for constructing video temp files
        self.downloading_video_data = {
            'user_format': None,
            'video_icon': None,
        }
        # attributes for keeping info for ffmpeg temp files
        self.ffmpeg_videos = {
            'temp_vid_filename': None,
            'temp_aud_filename': None,
            'temp_out_filename': None,
        }

    def set_work_directories(self, resources):
        self.download_icons_folder = resources["video_icons_folder"]
        self.temp_data_folder = resources["temp_data_folder"]
        self.download_app_folder = resources["download_folder"]

    def set_work_filenames(self, resources):
        self.db_filename = resources["db_filename"]
        self.ffmpeg_installer_filename = resources["ffmpeg_installer_filename"]
        self.ffmpeg_checker_filename = resources["ffmpeg_checker_filename"]
        self.temp_preview_filename = resources["temp_preview_filename"]

    def set_model_feedback(self, controller):
        self.controller = controller

    def set_videos_from_db(self, collection):
        self.videos_collection = collection

    def set_videos_count(self, count):
        self.videos_collection_count = count

    def set_video_as_current(self, video):
        try:
            self.selected_video = copy.deepcopy(video)
            return True
        except Exception as err:
            return False

    def get_first_video_data(self):
        try:
            data = {
                "id": self.first_video['id'],
                "video_name": self.first_video['video_name'],
                "video_desc": self.first_video['video_desc'],
                "video_format": self.first_video['video_format'],
                "video_date": self.first_video['video_date'],
                "video_path": self.first_video['video_path'],
                "video_icon": self.first_video['video_icon']
            }
            return data
        except Exception as err:
            return None

    def get_second_video_data(self):
        try:
            data = {
                "id": self.second_video['id'],
                "video_name": self.second_video['video_name'],
                "video_desc": self.second_video['video_desc'],
                "video_format": self.second_video['video_format'],
                "video_date": self.second_video['video_date'],
                "video_path": self.second_video['video_path'],
                "video_icon": self.second_video['video_icon']
            }
            return data
        except Exception as err:
            return None

    def get_current_video_data(self):
        try:
            data = {
                "id": self.selected_video['id'],
                "video_name": self.selected_video['video_name'],
                "video_desc": self.selected_video['video_desc'],
                "video_format": self.selected_video['video_format'],
                "video_date": self.selected_video['video_date'],
                "video_path": self.selected_video['video_path'],
                "video_icon": self.selected_video['video_icon']
            }
            return data
        except Exception as err:
            return None

    def get_videos_count(self):
        return self.videos_collection_count

    def get_downloading_video_data(self):
        try:
            data = {
                "video_name": self.pytube_info['video_name'],
                "video_icon": self.temp_preview_filename,
                "resolutions": self.pytube_info['resolutions'],
                "formats": self.pytube_info['formats'],
                "fps": self.pytube_info['fps']
            }
            return data
        except Exception as err:
            return None

    def model_prepare_resources(self, app_paths: dict, app_filenames: dict):
        """
            Construct resources for the application.

                Parameters:
                - app_paths (dict): Paths for the application resources.
                - app_filenames (dict): Filenames for the application resources.

                Returns:
                - None
        """

        try:
            make_directories_if_not_exist(paths_dict=app_paths)

            self.set_work_directories(resources=app_paths)
            self.set_work_filenames(resources=app_filenames)

            if not check_file_exist(path_to_file=self.db_filename):
                create_database(database=self.db_filename)

            clear_directory(directory=self.temp_data_folder)

        except (AppDirectoriesConstructingError, ClearingDirectoryError, DatabaseOperationError) as err:
            self.controller.model_critical_error(error_code=1)

    def model_reset_downloaded_info(self):
        """
            Resets downloaded video attributes in the model.

            Returns:
            - None
        """

        try:
            self.pytube_instance = None

            for key in self.pytube_info:
                self.pytube_info[key] = None

            for key in self.downloading_video_data:
                self.downloading_video_data[key] = None

            for key in self.ffmpeg_videos:
                self.ffmpeg_videos[key] = None
        except Exception as err:
            pass

    def model_change_videos_page(self):
        """
            Changes the current page in the video collection.

            Returns:
            - None
        """

        try:
            first_page, last_page = False, False
            self.first_video, self.second_video, first_page, last_page = move_in_videos_collection(
                collection=self.videos_collection,
                offset=self.offset_collection)

        except Exception as err:
            pass

    def model_next_videos_page(self):
        """
            Moves to the next page in the video collection.

                Returns:
                - None
        """

        try:
            self.offset_collection = change_offset_in_collection(offset=self.offset_collection,
                                                                 collection_count=self.videos_collection_count,
                                                                 direction_up=True)

        except Exception as err:
            pass

    def model_prev_videos_page(self):
        """
            Moves to the previous page in the video collection.

                Returns:
                - None
        """

        try:
            self.offset_collection = change_offset_in_collection(offset=self.offset_collection,
                                                                 collection_count=self.videos_collection_count,
                                                                 direction_up=False)

        except Exception as err:
            pass

    def model_delete_video(self, video: dict, full_delete: bool):
        """
            Deletes a video based on the provided data.

            Parameters:
            - video (dict): The video data to be deleted including:
                - 'video_name': The name of the video.
                - 'video_desc': The description of the video.
                - 'video_path': The path of the video.
                - 'video_icon': The icon path of the video.
            - full_delete (bool): Flag indicating if the video should be fully deleted.

            Returns:
            - bool: True if the video is successfully deleted, False otherwise.
        """

        try:
            delete_video(video=video, database=self.db_filename, full_delete=full_delete)
            return True
        except DeleteVideoError as err:
            self.controller.model_delete_video_error(err.title)
            return False

    def model_edit_video(self, data: dict):
        """
            Edits a video based on the provided data.

            Parameters:
            - data: The new data for the video edit including:
                - 'video_name': The name of the video.
                - 'video_desc': The description of the video.
                - 'video_path': The path of the video.
                - 'video_icon': The icon path of the video.

            Exceptions:
            - EditVideoError : If there is an error editing data in database.

            Returns:
            - None
        """

        try:

            need_to_remove = prepare_new_data_for_editing_video(video_for_edit=self.selected_video, new_data=data)

            edit_video(data=data, database=self.db_filename, with_replace=need_to_remove,
                       replace_from_path=self.selected_video['video_path'],
                       replace_to_path=data['video_path'])

        except EditVideoError as err:
            self.controller.model_edit_video_error(err.title)

    def model_check_data_for_editing(self, video_data: dict):
        """
            Checks the provided video data for editing.

            Parameters:
            - video_data (dict): The data of the video to be edited including:
                - 'video_name': The name of the video.
                - 'video_desc': The description of the video.
                - 'video_path': The path of the video.
                - 'video_icon': The icon path of the video.

            Exceptions:
            - CheckingDataForVideoError: If there is an error checking data.

            Returns:
            - bool: True if the data is valid for editing, False otherwise.
        """

        try:
            status = check_new_data_for_edit_video(new_video_data=video_data)
            return status
        except CheckingDataForVideoError:
            return False

    def model_update_video_collection(self):
        """
            Updates the video collection information.

            Exceptions:
            - DatabaseOperationError : If there is an error fetching data from database.

            Returns:
            - None
        """

        try:
            videos = get_nonexistence_videos_in_db(database=self.db_filename)
            for video in videos:
                self.model_delete_video(video, full_delete=False)
            check_directory_for_existence(path=self.download_app_folder)
            founded_videos_in_db = read_videos_db(database=self.db_filename)
            self.set_videos_from_db(collection=founded_videos_in_db)
            self.set_videos_count(count=len(self.videos_collection))

        except DatabaseOperationError as err:
            self.controller.model_critical_error(error_code=4)

        self.first_video = None
        self.second_video = None
        self.selected_video = None
        self.offset_collection = 0

    def model_search_video(self, url: str):
        """
            Searches for a video using the provided URL and sets up the Pytube instance for download.

            Parameters:
            - url (str): The URL of the video to search for.

            Returns:
            - bool: True if the video is found and Pytube instance is set up, False otherwise.
        """

        try:
            self.pytube_instance = get_youtube_video_if_exist(link=url,
                                                              progress_func=self.on_progress_download_stream,
                                                              complete_func=self.on_complete_download_stream)
            if self.pytube_instance != None:
                return True
            else:
                return False
        except FindingVideoError as e:
            self.model_reset_downloaded_info()
            return False

    def model_track_download_progress(self, info: str):
        """
            Translate download progress to the controller.

            Parameters:
            - info (str): Information about the download progress.

            Returns:
            - None
        """
        self.controller.controller_notify_user(msg=info)

    def on_progress_download_stream(self, stream, chunk, bytes_remaining):
        """
            callback function for indicate process of stream downloading.

            Parameters:
            - stream: The stream being downloaded.
            - chunk: The downloaded chunk size.
            - bytes_remaining: Number of bytes remaining to download.

            Returns:
            - None
        """

        total_size = stream.filesize
        bytes_downloaded = total_size - bytes_remaining
        percentage = (bytes_downloaded / total_size) * 100
        message = f"Downloading {stream.type}. ({percentage:.2f}%)"
        self.model_track_download_progress(message)

    def on_complete_download_stream(self, stream):
        """
            callback function for indicate completion of downloading stream.

            Parameters:
            - stream: The downloaded stream object.

            Returns:
            - None
        """

        message = f"Downloaded {stream.type} stream ..."
        if stream.type == "audio":
            message = f"Downloaded {stream.type}... Processing ..."
        self.model_track_download_progress(message)

    def model_select_suit_stream(self):
        """
            Select suitable video and audio streams based on format compatibility for downloading.

            Returns:
            - None
        """

        try:

            video_stream = self.pytube_info['video_streams'].first()

            extension = self.downloading_video_data['user_format']

            audio_stream = (self.pytube_instance.streams
                            .filter(only_audio=True, file_extension=extension)
                            .order_by('abr')
                            .desc()
                            .first())

            self.pytube_info['suit_video_stream'] = video_stream
            self.pytube_info['suit_audio_stream'] = audio_stream
        except Exception as err:
            pass

    def model_update_video_streams_by_filter(self, res=None, fmt=None, fps=None):
        """
            Update video streams based on the provided filters: resolution, format, and frames per second.

                Parameters:
                - res (str): Resolution filter.
                - fmt (str): Format filter.
                - fps (str): Frames per second filter.

                Returns:
                - None
        """
        streams_compilation = self.pytube_info['video_streams_all']

        self.pytube_info['resolutions'] = get_list_of_all_resolutions(streams=streams_compilation)
        if res:
            streams_compilation = streams_compilation.filter(res=res)
            self.pytube_info['formats'] = get_list_of_all_formats(streams_compilation)
        if fmt:
            streams_compilation = streams_compilation.filter(file_extension=fmt)
            self.pytube_info['fps'] = get_list_of_all_fps(streams_compilation)
        if fps:
            streams_compilation = streams_compilation.filter(fps=int(fps))

        self.pytube_info['video_streams'] = streams_compilation.order_by('resolution').desc()

    def model_prepare_before_downloading(self, data: dict):
        """
            Prepare data before downloading a video.

            Parameters:
            - data (dict): Data required for downloading the videoincluding:
                - 'user_path': path for saving video.
                - 'user_format': format of the downloading video.

            Returns:
            - bool: True if data is prepared successfully, False otherwise.
        """
        if not check_data_for_downloading_video(data=data):
            return False
        else:
            path, extension = prepare_data_for_downloading(data=data, path_to_download=self.download_app_folder)
            self.downloading_video_data['user_path'] = path
            self.downloading_video_data['user_format'] = extension
            return True

    def model_check_ffmpeg_installed(self):
        """
            Starts a new thread to check the status of FFmpeg installation.

            Returns:
            - None
        """

        thread = threading.Thread(target=self.model_check_ffmpeg_thread)
        thread.start()

    def model_download_youtube_video_data(self):
        """
            Starts a new thread to download common data for a YouTube video.

            Returns:
            - None
        """

        thread = threading.Thread(target=self.model_download_common_data_thread)
        thread.start()

    def model_start_download_youtube_video(self):
        """
            Starts a new thread to start downloading a YouTube video.

            Returns:
            - None
        """

        thread = threading.Thread(target=self.model_start_download_video_thread)
        thread.start()

    def model_check_ffmpeg_thread(self):
        """
            Launch .bat installation and checking ffmpeg files in separate thread.
            Reports the status to the controller based on the installation process.

            Exceptions:
            - Any Exception: If there is an unexpected error during the FFmpeg check.

            Returns:
            - None
        """

        try:
            installer = self.ffmpeg_installer_filename
            checker = self.ffmpeg_checker_filename

            self.controller.model_ffmpeg_report_handler(status_code=1)

            checker_process = subprocess.Popen(checker, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            output, error = checker_process.communicate()

            if checker_process.returncode == 0:
                checker_process.kill()

                self.controller.model_ffmpeg_report_handler(status_code=2)

            elif checker_process.returncode == 1:
                checker_process.kill()

                self.controller.model_ffmpeg_report_handler(status_code=3)

                install_process = subprocess.Popen(['cmd', '/k', installer], creationflags=subprocess.CREATE_NEW_CONSOLE)
                output, error = install_process.communicate()
                install_process.kill()

                self.controller.model_ffmpeg_report_handler(status_code=4)

        except Exception as err:
            self.controller.model_critical_error(error_code=3)

    def model_start_download_video_thread(self):
        """
            Starts the download of video and audio streams in separate threads, concatenates them.

            Exceptions:
            - FfmpegError: If there is an error during FFmpeg operations.
            - DownloadStreamError: If there is an error during stream download.
            - PreparingDownloadedVideoDataError: If there is an error preparing downloaded video data.
            - AddingDownloadVideoDatabaseError: If there is an error adding the video to the database.

            Returns:
            - None
        """
        try:
            temp_video_file = download_stream(path_for_save=self.temp_data_folder,
                                              file_name='vid',
                                              stream=self.pytube_info['suit_video_stream'])

            temp_audio_file = download_stream(path_for_save=self.temp_data_folder,
                                              file_name='aud',
                                              stream=self.pytube_info['suit_audio_stream'])

            self.ffmpeg_videos['temp_vid_filename'] = temp_video_file
            self.ffmpeg_videos['temp_aud_filename'] = temp_audio_file

            vido_file = concat_audio_video_files(video_file=temp_video_file,
                                                 audio_file=temp_audio_file,
                                                 output_temp_video_path=self.temp_data_folder,
                                                 output_temp_name='concat',
                                                 output_path=self.downloading_video_data['user_path'])

            data = prepare_new_data_for_downloaded_video(video_file_path=vido_file,
                                                         preview_file_path=self.temp_preview_filename)

            add_video(database=self.db_filename, data=data, path_to_save=self.download_icons_folder)

            clear_directory(directory=self.temp_data_folder)

            self.controller.model_successfully_downloaded_video_handler("message")
        except (FfmpegError, DownloadStreamError, PreparingDownloadedVideoDataError) as err:
            clear_directory(directory=self.temp_data_folder)
            self.model_reset_downloaded_info()
            self.controller.model_downloading_youtube_video_error(name_err=err.title)
        except AddingDownloadVideoDatabaseError as err:
            clear_directory(directory=self.temp_data_folder)
            self.controller.model_critical_error(error_code=5)

    def model_download_common_data_thread(self):
        """
            Download common data for a YouTube video in a separate thread.

            Exceptions:
            - CommonDataFetchError: If there is an error fetching common data.
            - DownloadPreviewError: If there is an error downloading the preview.
            - DownloadStreamError: If there is an error downloading video streams.

            Returns:
            - None
        """
        try:
            name, thumbnail = get_common_info_youtube_video(pytube_obj=self.pytube_instance)
            self.pytube_info['video_name'] = name
            self.pytube_info['thumbnail_url'] = thumbnail
            self.pytube_info['video_streams_all'] = get_all_video_streams(all_streams=self.pytube_instance.streams)
            if not preview_download(thumbnail_url=thumbnail, filename_for_save=self.temp_preview_filename):
                self.model_reset_downloaded_info()
                raise DownloadPreviewError
            self.controller.model_downloaded_youtube_video_info_handler()
        except (CommonDataFetchError, DownloadPreviewError, DownloadStreamError) as err:
            clear_directory(directory=self.temp_data_folder)
            self.controller.model_downloading_youtube_video_info_error(name_err=err.title)
            self.model_reset_downloaded_info()

