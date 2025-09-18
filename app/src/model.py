import sqlite3 as db
import copy
import os
import time
import re
from datetime import datetime
from pytubefix import YouTube
import ffmpeg
import threading
import requests
from pytubefix.request import stream
from appExceptions import *
import uuid


temp_preview_filename = f"../../app/appData/temp/preview.jpg"
path_to_icons = f"../appData/videoIcons"

def normalize_path(path):
    standardized_path = path.replace("\\", "/")
    return standardized_path

def generate_unique_filename():
    unique_filename = str(uuid.uuid4())
    return unique_filename


def check_directory_for_existence(path: str):
    if not os.path.exists(path):
        os.makedirs(path)
        return False
    else:
        return True


def get_full_path(path:str):
    return os.path.abspath(path)


def check_file_name(filename):
    pattern = r'^[\w\sа-яА-ЯёЁ\-_.]+$'
    if re.match(pattern, filename):
        return True
    else:
        return False





class Model:

    def __init__(self):
        self.db = "../appData/database.db"
        self.download_directory = "../../download"
        self.path_to_icons = "../appData/videoIcons"

        self.controller = None

        self.videos_collection = None
        self.videos_collection_count = 0
        self.first_video = None
        self.second_video = None
        self.selected_video = None
        self.offset_collection = 0

        self.pytube_instance = None
        self.download_url = None
        self.pytube_info = {
            'suit_video_stream': None,
            'suit_audio_stream': None,
            'thumbnail_url': None,
            'video_name': None,
            'video_streams': None,
            'resolutions': None,
            'formats': None,
            'fps': None,
        }
        self.downloaded_video = {
            'user_format': None,
            'video_icon': None,
            'auto_name': None,
            'full_path': None,
        }

        self.ffmpeg_videos = {
            'temp_vid_filename': None,
            'temp_aud_filename': None,
            'temp_out_filename': None,
        }

    def reset_model_pytube(self):
        try:
            self.pytube_instance = None

            for key in self.pytube_info:
                self.pytube_info[key] = None

            for key in self.downloaded_video:
                self.downloaded_video[key] = None

            for key in self.ffmpeg_videos:
                self.ffmpeg_videos[key] = None
        except Exception as err:
            pass


    def set_feedback(self, instance):
        self.controller = instance

    def set_videos_from_db(self, collection):
        self.videos_collection = collection

    def set_videos_count(self, count):
        self.videos_collection_count = count

    def set_video_as_current(self, video):
        self.selected_video = copy.deepcopy(video)

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



    def synchronize_app_videos_data_with_db(self):
        try:
            self.clear_nonexistence_videos_in_db()
            check_directory_for_existence(path=self.download_directory)
            self.set_videos_from_db(collection=self.read_videos_db())
            self.set_videos_count(count=len(self.videos_collection))

        except DatabaseOperationError as err:
            self.controller.model_critical_error(code=1)

        self.first_video = None
        self.second_video = None
        self.selected_video = None
        self.offset_collection = 0

    def clear_nonexistence_videos_in_db(self):
        """
            INFO: Checking for the existing of video attributes (video file, icon) in records,
            given from db;

            GETS: -

            RETURNS:  -
            """
        videos_to_remove = []
        video_records = self.read_videos_db()

        if not video_records is None:

            for video in video_records:
                video_path = video['video_path']
                icon_path = video['video_icon']
                if os.path.exists(video_path):
                    if not os.path.exists(icon_path):
                        videos_to_remove.append(video)
                else:
                    videos_to_remove.append(video)

            for video in videos_to_remove:
                self.delete_video_model(video, full_delete=False)


    def move_in_videos_collection(self):
        item1 = None
        item2 = None
        try:
            index_first = self.offset_collection + 0
            index_second = self.offset_collection + 1
            item1 = self.videos_collection[index_first]
            item2 = self.videos_collection[index_second]
        except Exception:
            pass

        if (item2 is None) and (not item1 is None):
            self.first_video = item1
            self.second_video = None
        elif (not item1 is None) and (not item2 is None):
            self.first_video = item1
            self.second_video = item2
        else:
            self.first_video = item1
            self.second_video = item2

    def videos_offset_up(self):
        if self.offset_collection > 0:
            self.offset_collection -= 2

    def videos_offset_down(self):
        if self.offset_collection < self.videos_collection_count - 2:
            self.offset_collection += 2
            print(self.offset_collection)






    def check_new_data_for_video(self, new_video_data):
        first_check = check_directory_for_existence(new_video_data['video_path'])
        second_check = check_file_name(new_video_data['video_name'])

        if not first_check:
            self.controller.notification_for_user(code="CHANGE DIRECTORY")
            return False
        elif not second_check:
            self.controller.notification_for_user(code="CHANGE NAME")
            return False
        else:
            return True

    def delete_video_model(self, data, full_delete: bool):
        try:
            self.delete_video(data, full_delete)
        except DeleteVideoError as err:
            self.controller.delete_error(err.title)

    def update_video(self, data, with_replace: bool):
        try:
            self.update_video_db(data)
            if with_replace:
                os.rename(self.selected_video['video_path'], data['video_path'])
        except Exception as err:
            raise EditVideoError(err)

    def delete_video(self, data, full_delete: bool):
        try:
            video_path = data['video_path']
            video_id = data['id']
            self.delete_videos_db(video_id)

            if full_delete:
                if os.path.exists(video_path):
                    os.remove(video_path)
        except Exception as err:
            raise DeleteVideoError(err)

    def edit_video(self, data):
        try:
            id = self.selected_video['id']
            date = self.selected_video['video_date']
            format = self.selected_video['video_format']

            new_path = data['video_path']
            new_name = data['video_name']
            new_desc = data['video_desc']
            new_icon = data['video_icon']

            new_full_path = f"{new_path}/{new_name}.{format}"
            old_full_path = self.selected_video['video_path']
            replace_flag = True if new_full_path != old_full_path else False

            data['id'] = id
            data['video_format'] = format
            data['video_date'] = date
            data['video_icon'] = new_icon
            data['video_path'] = new_full_path
            data['video_name'] = new_name
            data['video_desc'] = new_desc

            self.update_video(data, with_replace=replace_flag)
        except EditVideoError as err:
            self.controller.edit_error(err.title)




































    def try_to_find(self, url):
        try:
            self.pytube_instance = YouTube(
                url,
                on_progress_callback=self.on_progress_download_stream,
                on_complete_callback=self.on_complete_download_stream)
            return True
        except Exception as e:
            self.reset_model_pytube()
            return False

    def fetch_resolutions(self, streams):

        resolutions = []
        for stream in streams:
            resolution = stream.resolution
            if resolution and resolution not in resolutions:
                resolutions.append(resolution)
        return resolutions

    def fetch_formats(self, streams):

        formats = []
        for stream in streams:
            format = stream.subtype
            if format and format not in formats:
                formats.append(format)
        return formats

    def fetch_fps(self, streams):

        result = []
        for stream in streams:
            fps = stream.fps
            if fps and fps not in result:
                result.append(fps)
        return result




    def select_suit_stream(self):
        try:

            video_stream = self.pytube_info['video_streams'].first()

            extension = self.downloaded_video['user_format']
            audio_stream = (self.pytube_instance.streams
                                                     .filter(only_audio=True,file_extension=extension)
                                                     .order_by('abr')
                                                     .desc()
                                                     .first())

            self.pytube_info['suit_video_stream'] = video_stream
            self.pytube_info['suit_audio_stream'] = audio_stream
        except Exception as err:
            pass


    def get_additional_download_data(self):
        return {
            'resolutions': self.pytube_info['resolutions'],
            'formats': self.pytube_info['formats'],
            'fps': self.pytube_info['fps']
        }

    def video_streams_download(self):
        try:
            self.pytube_info['video_streams'] = self.pytube_instance.streams.filter(progressive=False, only_video=True)
        except Exception as err:
            raise VideoStreamsDownloadError(err)


    def update_video_streams_by_filter(self, res=None, fmt=None, fps=None):
        streams = self.pytube_instance.streams.filter(progressive=False, only_video=True)
        self.pytube_info['resolutions'] = self.fetch_resolutions(streams)

        if res:
            streams = streams.filter(res=res)
            self.pytube_info['formats'] = self.fetch_formats(streams)
        if fmt:
            streams = streams.filter(file_extension=fmt)
            self.pytube_info['fps'] = self.fetch_fps(streams)
        if fps:
            streams = streams.filter(fps=int(fps))

        self.pytube_info['video_streams'] = streams.order_by('resolution').desc()

    def prepare_data_for_downloading_video(self, data):
        path = data['path']
        format = data['format']
        if path == "default":
            path = get_full_path(self.download_directory)

        first_check = check_directory_for_existence(path)
        if first_check:
            self.downloaded_video['user_path'] = path
            self.downloaded_video['user_format'] = format
            self.downloaded_video['auto_name'] = generate_unique_filename()

            return True
        else:
            return False



    ''' GOOD '''
    def start_download_video_thread(self):
        try:
            self.download_video_stream()
            self.download_audio_stream()
            self.concat_audio_video_streams()
            data = self.prepare_data_for_downloaded_video()
            self.append_after_download(data)
            self.controller.download_end("message")
        except (FfmpegError, DownloadAudioStreamError, DownloadVideoStreamError) as err:
            self.delete_temp_files()
            self.reset_model_pytube()
            self.controller.download_error(name_err=err.title)
        except PreparingDownloadedVideoDataError as err:
            self.reset_model_pytube()
            self.controller.download_error(name_err=err.title)
        except AddingDownloadVideoDatabaseError as err:
            self.controller.model_critical_error(code="DB PROBLEM")

    def delete_temp_files(self):
        try:
            os.remove(self.ffmpeg_videos['temp_vid_filename'])
            os.remove(self.ffmpeg_videos['temp_aud_filename'])
            os.remove(self.ffmpeg_videos['temp_out_filename'])
        except Exception as e:
            pass


    ''' GOOD '''
    def download_video_stream(self):
        try:
            output_path = '../../app/appData/temp/'
            file_path = self.pytube_info['suit_video_stream']\
                .download(output_path=output_path)
            file_extension = os.path.splitext(file_path)[1]
            new_file_name = 'vid' + file_extension
            new_file_path = os.path.join(output_path, new_file_name)

            os.rename(file_path, new_file_path)
            self.ffmpeg_videos['temp_vid_filename'] = new_file_path

        except Exception as err:
            raise DownloadVideoStreamError(err)

    ''' GOOD '''
    def download_audio_stream(self):
        try:
            output_path = '../../app/appData/temp/'
            file_path = self.pytube_info['suit_audio_stream']\
                .download(output_path=output_path)

            file_extension = os.path.splitext(file_path)[1]
            new_file_name = 'aud' + file_extension
            new_file_path = os.path.join(output_path, new_file_name)

            os.rename(file_path, new_file_path)
            self.ffmpeg_videos['temp_aud_filename'] = new_file_path

        except Exception as err:
            raise DownloadAudioStreamError(err)

    ''' GOOD '''
    def concat_audio_video_streams(self):
        try:

            input_video = ffmpeg.input(self.ffmpeg_videos['temp_vid_filename'])
            input_audio = ffmpeg.input(self.ffmpeg_videos['temp_aud_filename'])

            output_format = os.path.splitext(self.ffmpeg_videos['temp_vid_filename'])[1]
            output_path = '../../app/appData/temp/'
            output_file_name = 'concat' + output_format
            output_video = os.path.join(output_path, output_file_name)
            self.ffmpeg_videos['temp_out_filename'] = output_video

            ffmpeg.output(input_video, input_audio, output_video, codec='copy').overwrite_output().run(
                quiet=True)

            output_path = self.downloaded_video['user_path']
            file_path = output_video
            file_extension = os.path.splitext(file_path)[1]
            new_file_name = self.downloaded_video['auto_name'] + file_extension
            new_file_path = os.path.join(output_path, new_file_name)
            os.rename(file_path, new_file_path)

            self.downloaded_video['full_path'] = new_file_path

            os.remove(self.ffmpeg_videos['temp_vid_filename'])
            os.remove(self.ffmpeg_videos['temp_aud_filename'])


        except Exception as err:
            raise FfmpegError(err)

    ''' GOOD '''
    def prepare_data_for_downloaded_video(self):
        try:
            full_path = self.downloaded_video['full_path']
            creation_time = os.path.getctime(full_path)
            date = datetime.fromtimestamp(creation_time).strftime('%d.%m.%Y')
            name = self.downloaded_video['auto_name']
            format = self.downloaded_video['user_format']
            icon = get_full_path(temp_preview_filename)

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

    ''' GOOD '''
    def append_after_download(self, data):
        try:
            last_id = int(self.create_video_db(data))
            name = str(last_id)
            temp_icon_path = f"../../app/appData/temp/preview.jpg"
            formated_icon_path = get_full_path(f"../../app/appData/videoIcons/{name}.jpg")
            os.rename(temp_icon_path, formated_icon_path)
            data["video_icon"] = formated_icon_path
            data["id"] = last_id
            self.update_video_db(data)
        except Exception as err:
            raise AddingDownloadVideoDatabaseError(err)



    def on_progress_download_stream(self, stream, chunk, bytes_remaining):
        total_size = stream.filesize
        bytes_downloaded = total_size - bytes_remaining
        percentage = (bytes_downloaded / total_size) * 100
        message = f"Downloading {stream.type}. ({percentage:.2f}%)"
        self.controller.download_going(message)

    def on_complete_download_stream(self, stream, file_path):
        message = f"Downloaded {stream.type}"
        if stream.type == "audio":
            message = f"Downloaded {stream.type}. Processing ..."
        self.controller.download_going(message)






    ''' GOOD '''
    def preview_download(self):
        try:
            response = requests.get(self.pytube_info['thumbnail_url'])

            if response.status_code == 200:
                file_name = temp_preview_filename
                with open(file_name, 'wb') as f:
                    f.write(response.content)


            else:
                self.controller.common_data_downloaded(False)
        except Exception as err:
            raise DownloadPreviewError(err)

    ''' GOOD '''
    def common_data_download(self):
        try:
            self.pytube_info['video_name'] = self.pytube_instance.title
            self.pytube_info['thumbnail_url'] = self.pytube_instance.thumbnail_url
        except Exception as err:
            self.pytube_info['video_name'] = None
            self.pytube_info['thumbnail_url'] = None
            raise CommonDataFetchError(err)

    ''' GOOD '''
    def start_download_common_data_thread(self):
        try:
            self.common_data_download()
            self.video_streams_download()
            self.preview_download()
            self.controller.common_data_downloaded()
        except (CommonDataFetchError, DownloadPreviewError, VideoStreamsDownloadError)  as err:
            self.controller.common_data_download_error(name_err=err.title)
            self.reset_model_pytube()


    ''' GOOD '''
    def start_download_common_data(self):
        thread = threading.Thread(target=self.start_download_common_data_thread)
        thread.start()

    ''' GOOD '''
    def start_download_video(self):
        thread = threading.Thread(target=self.start_download_video_thread)
        thread.start()



    def get_download_video_data(self):
        try:
            self.update_video_streams_by_filter()
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
























    ''' CRUD operations with DB '''

    def read_videos_db(self):
            try:
                with db.connect(self.db) as connection:
                    cursor = connection.cursor()
                    cursor.execute('''
                        SELECT 
                        id, video_name, video_desc, video_format, video_date,
                        video_path, video_icon
                        FROM 
                        video
                        ORDER BY video_name''')
                    columns = [column[0] for column in cursor.description]
                    records = [
                        dict(zip(columns, record))
                        for record in cursor.fetchall()
                    ]
                    return records
            except Exception as e:
                raise DatabaseOperationError(message="Error", operation="on read", trouble=e)

    def delete_videos_db(self, id):
            try:
                with db.connect(self.db) as connection:
                    cursor = connection.cursor()
                    cursor.execute('''
                            DELETE FROM video
                            WHERE id = ?
                        ''', (id,))
                    connection.commit()
            except Exception as e:
                raise DatabaseOperationError(message="Error", operation="on delete", trouble=e)

    def create_video_db(self, video):
            try:
                with db.connect(self.db) as connection:
                    cursor = connection.cursor()
                    cursor.execute('''
                        INSERT INTO video (
                            video_name, 
                            video_desc,
                            video_format, 
                            video_date,
                            video_path, 
                            video_icon)
                            VALUES (?, ?, ?, ?, ?, ?)''',
                                   (
                                       video['video_name'],
                                       video['video_desc'],
                                       video['video_format'],
                                       video['video_date'],
                                       video['video_path'],
                                       video['video_icon']))
                    last_id = cursor.lastrowid
                    connection.commit()
                    return last_id
            except Exception as e:
                raise DatabaseOperationError(message="Error", operation="on insert", trouble=e)

    def update_video_db(self, video):
            try:
                with db.connect(self.db) as connection:
                    cursor = connection.cursor()
                    cursor.execute('''
                                        UPDATE video 
                                        SET video_name = ?,
                                            video_desc = ?,
                                            video_format = ?, 
                                            video_date = ?,
                                            video_path = ?, 
                                            video_icon = ?
                                        WHERE id = ?''',
                                   (video['video_name'],
                                    video['video_desc'],
                                    video['video_format'],
                                    video['video_date'],
                                    video['video_path'],
                                    video['video_icon'],
                                    video['id']))
                    connection.commit()
            except Exception as e:
                raise DatabaseOperationError(message="Error", operation="on update", trouble=e)


