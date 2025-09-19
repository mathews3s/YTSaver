import copy
import threading
from video_operations import *
from pytube_operations import *

temp_preview_filename = f"../../app/appData/temp/preview.jpg"
db_filename = "../appData/database.db"
save_icons_app_folder = f"../appData/videoIcons"
temp_data_app_folder = '../../app/appData/temp/'
download_app_folder = "../../download"


class Model:

    def __init__(self):
        self.db = db_filename
        self.download_directory = download_app_folder

        self.controller = None

        self.videos_collection = None
        self.videos_collection_count = 0
        self.first_video = None
        self.second_video = None
        self.selected_video = None
        self.offset_collection = 0

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
        self.downloading_video_data = {
            'user_format': None,
            'video_icon': None,
        }
        self.ffmpeg_videos = {
            'temp_vid_filename': None,
            'temp_aud_filename': None,
            'temp_out_filename': None,
        }

    def model_check_resources(self):
        try:
            if not check_file_exist(self.db):
                create_database(self.db)
            check_directory_for_existence(path=download_app_folder)
            check_directory_for_existence(path=temp_data_app_folder)
            check_directory_for_existence(path=save_icons_app_folder)
            clear_directory(directory=temp_data_app_folder)

        except DatabaseOperationError as err:
            self.controller.model_critical_error(error_code=1)

    def reset_model_pytube(self):
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

    def model_set_feedback(self, controller):
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

    def model_change_videos_page(self):
        try:
            self.first_video, self.second_video = move_in_videos_collection(collection=self.videos_collection,
                                                                            offset=self.offset_collection)

        except Exception as err:
            pass

    def model_next_videos_page(self):
        try:
            self.offset_collection = change_offset_in_collection(offset=self.offset_collection,
                                                                 collection_count=self.videos_collection_count,
                                                                 direction_up=True)


        except Exception as err:
            pass

    def model_prev_videos_page(self):
        try:
            self.offset_collection = change_offset_in_collection(offset=self.offset_collection,
                                                                 collection_count=self.videos_collection_count,
                                                                 direction_up=False)


        except Exception as err:
            pass

    def delete_video_model(self, video, full_delete: bool):
        try:
            delete_video(video=video, database=self.db, full_delete=full_delete)
            return True
        except DeleteVideoError as err:
            self.controller.model_delete_video_error(err.title)
            return False
            

    def edit_video_model(self, data):
        try:

            need_to_remove = prepare_new_data_for_editing_video(video_for_edit=self.selected_video, data=data)

            edit_video(data=data, database=self.db, with_replace=need_to_remove,
                       replace_from_path=self.selected_video['video_path'],
                       replace_to_path=data['video_path'])

        except EditVideoError as err:
            self.controller.model_edit_video_error(err.title)

    def model_check_data_for_editing(self, video_data):
        try:
            status = check_new_data_for_edit_video(new_video_data=video_data)
            return status
        except CheckingDataForVideoError:
            return False

    def model_update_video_collection(self):
        try:
            videos = get_nonexistence_videos_in_db(database=self.db)
            for video in videos:
                self.delete_video_model(video, full_delete=False)
            check_directory_for_existence(path=download_app_folder)
            founded_videos_in_db = read_videos_db(database=self.db)
            self.set_videos_from_db(collection=founded_videos_in_db)
            self.set_videos_count(count=len(self.videos_collection))

        except DatabaseOperationError as err:
            self.controller.model_critical_error(error_code=2)

        self.first_video = None
        self.second_video = None
        self.selected_video = None
        self.offset_collection = 0

    def model_search_video(self, url):
        try:
            self.pytube_instance = get_youtube_video_if_exist(link=url,
                                                              progress_func=self.on_progress_download_stream,
                                                              complete_func=self.on_complete_download_stream)
            if self.pytube_instance != None:
                return True
            else:
                return False
        except Exception as e:
            self.reset_model_pytube()
            return False

    def model_track_download_progress(self, info):
        self.controller.controller_notify_user(msg=info)

    def on_progress_download_stream(self, stream, chunk, bytes_remaining):
        total_size = stream.filesize
        bytes_downloaded = total_size - bytes_remaining
        percentage = (bytes_downloaded / total_size) * 100
        message = f"Downloading {stream.type}. ({percentage:.2f}%)"
        self.model_track_download_progress(message)

    def on_complete_download_stream(self, stream, file_path):
        message = f"Downloaded {stream.type} stream ..."
        if stream.type == "audio":
            message = f"Downloaded {stream.type}... Processing ..."
        self.model_track_download_progress(message)

    def select_suit_stream(self):
        try:

            video_stream = self.pytube_info['video_streams'].first()

            extension = self.downloading_video_data['user_format']

            audio_stream = (self.pytube_instance.streams
                                                     .filter(only_audio=True,file_extension=extension)
                                                     .order_by('abr')
                                                     .desc()
                                                     .first())

            self.pytube_info['suit_video_stream'] = video_stream
            self.pytube_info['suit_audio_stream'] = audio_stream
        except Exception as err:
            pass

    def update_video_streams_by_filter(self, res=None, fmt=None, fps=None):
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

    def model_prepare_before_downloading(self, data):

        if not check_data_for_downloading_video(data=data):
            return False
        else:
            path, extension = prepare_data_for_downloading(data=data, path_to_download=download_app_folder)
            self.downloading_video_data['user_path'] = path
            self.downloading_video_data['user_format'] = extension
            return True

    def start_download_video_thread(self):
        try:
            temp_video_file = download_stream(path_for_save='../../app/appData/temp/',
                                                    file_name='vid',
                                                    stream=self.pytube_info['suit_video_stream'])

            temp_audio_file = download_stream(path_for_save='../../app/appData/temp/',
                                                    file_name='aud',
                                                    stream=self.pytube_info['suit_audio_stream'])

            self.ffmpeg_videos['temp_vid_filename'] = temp_video_file
            self.ffmpeg_videos['temp_aud_filename'] = temp_audio_file

            vido_file = concat_audio_video_files(video_file=temp_video_file,
                                                 audio_file=temp_audio_file,
                                                 output_temp_video_path='../../app/appData/temp/',
                                                 output_temp_name='concat',
                                                 output_path=self.downloading_video_data['user_path'])

            data = prepare_new_data_for_downloaded_video(vido_file, temp_preview_filename)

            add_video(database=self.db, data=data, path_to_save=save_icons_app_folder)


            clear_directory(directory=temp_data_app_folder)

            self.controller.model_successfully_downloaded_video_handler("message")
        except (FfmpegError, DownloadAudioStreamError,
                DownloadVideoStreamError, PreparingDownloadedVideoDataError) as err:
            clear_directory(directory=temp_data_app_folder)
            self.reset_model_pytube()
            self.controller.model_downloading_youtube_video_error(name_err=err.title)
        except AddingDownloadVideoDatabaseError as err:
            clear_directory(directory=temp_data_app_folder)
            self.controller.model_critical_error(error_code=3)

    def model_download_common_data_thread(self):
        try:
            name, thumbnail = get_common_info_youtube_video(pytube_obj=self.pytube_instance)
            self.pytube_info['video_name'] = name
            self.pytube_info['thumbnail_url'] = thumbnail
            self.pytube_info['video_streams_all'] = get_all_video_streams(all_streams=self.pytube_instance.streams)
            if not preview_download(thumbnail_url=thumbnail, filename_for_save=temp_preview_filename):
                self.reset_model_pytube()
                raise DownloadPreviewError
            self.controller.model_downloaded_youtube_video_info_handler()
        except (CommonDataFetchError, DownloadPreviewError, VideoStreamsDownloadError) as err:
            self.controller.model_downloading_youtube_video_info_error(name_err=err.title)
            self.reset_model_pytube()

    def model_download_youtube_video(self):
        thread = threading.Thread(target=self.model_download_common_data_thread)
        thread.start()

    def start_download_video(self):
        thread = threading.Thread(target=self.start_download_video_thread)
        thread.start()

    def get_download_video_data(self):
        try:
            data = {
                "video_name": self.pytube_info['video_name'],
                "video_icon": temp_preview_filename,
                "resolutions": self.pytube_info['resolutions'],
                "formats": self.pytube_info['formats'],
                "fps": self.pytube_info['fps']
            }
            return data
        except Exception as err:
           return None


