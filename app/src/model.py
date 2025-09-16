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

test_url = "https://www.youtube.com/watch?v=K6rKRdayW78"
path_to_icons = "../appData/videoIcons"

class Model:

    def __init__(self):
        self.db = "../appData/database.db"
        self.download_directory = "../../download"
        self.path_to_icons = "../appData/videoIcons"
        self.controller = None

        self.founded_videos = None
        self.videos_count = None
        self.video_1 = None
        self.video_2 = None
        self.current_video = None
        self.offset_collection = 0

        self.pytube_instance = None
        self.download_url = None
        self.video_for_downloading = {
            'filtered_streams': None,
            'suit_video_stream': None,
            'suit_audio_stream': None,
            'video_name': None,
            'resolutions': None,
            'formats': None,
            'fps': None,
            'user_format': None,
            'thumbnail_url': None,
            'video_icon': None
        }

    def set_feedback(self, cntrl):
        self.controller = cntrl

    def get_first_video_info(self):
        video_info = {
            "id": self.video_1['id'],
            "video_name": self.video_1['video_name'],
            "video_desc": self.video_1['video_desc'],
            "video_format": self.video_1['video_format'],
            "video_date": self.video_1['video_date'],
            "video_path": self.video_1['video_path'],
            "video_icon": self.video_1['video_icon']
        }
        return video_info

    def get_second_video_info(self):
        try:
            video_info = {
                "id": self.video_2['id'],
                "video_name": self.video_2['video_name'],
                "video_desc": self.video_2['video_desc'],
                "video_format": self.video_2['video_format'],
                "video_date": self.video_2['video_date'],
                "video_path": self.video_2['video_path'],
                "video_icon": self.video_2['video_icon']
            }
            return video_info
        except Exception as e:
            return None

    def get_current_video_info(self, en_full_path=None):
        try:
            if not en_full_path:
                formated_path = os.path.dirname(self.current_video['video_path'])
            else:
                formated_path = self.current_video['video_path']
            video_info = {
                "id": self.current_video['id'],
                "video_name": self.current_video['video_name'],
                "video_desc": self.current_video['video_desc'],
                "video_format": self.current_video['video_format'],
                "video_date": self.current_video['video_date'],
                "video_path": formated_path,
                "video_icon": self.current_video['video_icon']
            }
            return video_info
        except:
            return None


    def get_videos_count(self):
        return self.videos_count


    def update_storages(self):
        # проверяю записи в бд на их существование в NTFS
        self.check_videos_in_db()
        video_in_db = self.fetch_videos_db()
        # проверяю баз. дир на наличие файлов
        if self.check_directory_exists(self.download_directory):
            # self.check_default_directory()
            pass

        self.set_videos_from_db()
        self.update_videos_count()

        self.video_1 = None
        self.video_2 = None
        self.current_video = None
        self.offset_collection = 0



    def check_default_directory(self):

        video_in_db = self.fetch_videos_db()
        name_list_from_db = {video['video_name'] for video in video_in_db}

        videos_in_directory = self.find_videos_in_directory(self.download_directory)

        for video in videos_in_directory:
            if video['video_name'] not in name_list_from_db:
                self.insert_video_into_db(video)

    def check_directory_exists(self, path):
        if not os.path.exists(path):
            os.makedirs(path)
            return False
        else:
            return True

    def check_file_name(self, filename):
        pattern = r'^[\w\sа-яА-ЯёЁ\-_.]+$'

        if re.match(pattern, filename):
            return True
        else:
            return False

    def find_videos_in_directory(self, dir):
        video_extensions = ('.mp4', '.avi', '.mov', '.mkv', '.wmv', '.flv')
        videos = []

        for root, dirs, files in os.walk(dir):
            for file in files:
                if file.lower().endswith(video_extensions):
                    full_path = os.path.abspath(os.path.join(root, file))
                    video_format = os.path.splitext(file)[1][1:]
                    creation_time = os.path.getctime(full_path)
                    formatted_date = datetime.fromtimestamp(creation_time).strftime('%d.%m.%Y')
                    formated_name = file.split('.')[0]

                    videos.append({
                        'video_name': formated_name,
                        'video_path': full_path,
                        'video_date': formatted_date,
                        'video_format': video_format,
                        'video_desc' : "nf",
                        'video_icon': "nf"
                    })

        return videos

    def check_videos_in_db(self):
        """
            INFO: Checking for the existing of video attributes (video file, icon) in records,
            given from db;

            GETS: -

            RETURNS:  -
            """
        videos_to_remove = []
        videos = self.fetch_videos_db()

        for video in videos:
            video_path = video['video_path']
            icon_path = video['video_icon']
            id = video['id']

            if os.path.exists(video_path):
                if not os.path.exists(icon_path):
                    videos_to_remove.append(video)
            else:
                videos_to_remove.append(video)

        for video in videos_to_remove:
            self.delete_video(video, False)



    def set_videos_from_db(self):
        self.founded_videos = self.fetch_videos_db()


    def update_videos_count(self):
        self.videos_count = len(self.founded_videos)



    def set_video_as_current(self, video):
        self.current_video = copy.deepcopy(video)
        print(f"current is {self.current_video['video_name']}")

    def switch_current_videos(self):
        item1 = None
        item2 = None
        try:
            item1 = self.founded_videos[0 + self.offset_collection]
            item2 = self.founded_videos[1 + self.offset_collection]
        except Exception as e:
            print("Произошла ошибка во время выбора", e)

        if (item2 is None) and (not item1 is None):
            self.video_1 = item1
            self.video_2 = None
        elif (not item1 is None) and (not item2 is None):
            self.video_1 = item1
            self.video_2 = item2
        else:
            self.video_1 = item1
            self.video_2 = item2

    def videos_offset_up(self):
        if self.offset_collection > 0:
            self.offset_collection -= 2

    def videos_offset_down(self):
        if self.offset_collection < self.videos_count - 2:
            self.offset_collection += 2
            print(self.offset_collection)


    def delete_video(self, video, full_delete):
        video_path = video['video_path']
        video_id = video['id']
        self.delete_videos_db(video_id)
        if full_delete:
            if os.path.exists(video_path):
                os.remove(video_path)



    def check_video_data(self, new_video_data):
        first_check = self.check_directory_exists(new_video_data['video_path'])
        second_check = self.check_file_name(new_video_data['video_name'])

        if not first_check:
            print("dir problem")
            return False
        elif not second_check:
            print("name problem")
            return False
        else:
            return True

    def update_video_info(self, data_for_update, with_replace):
        self.update_video_in_db(data_for_update)
        if with_replace:
            os.rename(self.current_video['video_path'], data_for_update['video_path'])

    def edit_video_info(self, data_for_update):

        id = self.current_video['id']
        date = self.current_video['video_date']
        format = self.current_video['video_format']

        new_path = data_for_update['video_path']
        new_name = data_for_update['video_name']
        new_desc = data_for_update['video_desc']
        new_icon = data_for_update['video_icon']

        new_full_path = f"{new_path}/{new_name}.{format}"
        old_full_path = self.current_video['video_path']
        replace_flag = True if new_full_path != old_full_path else False

        data_for_update['id'] = id
        data_for_update['video_format'] = format
        data_for_update['video_date'] = date
        data_for_update['video_icon'] = new_icon
        data_for_update['video_path'] = new_full_path
        data_for_update['video_name'] = new_name
        data_for_update['video_desc'] = new_desc

        self.update_video_info(data_for_update, with_replace=replace_flag)


    def fetch_last_id_db(self):
        try:
            with db.connect(self.db) as connection:
                cursor = connection.cursor()
                cursor.execute(f"SELECT MAX(id) FROM video")
                last_id = cursor.fetchone()[0]
                connection.commit()
                return last_id

        except Exception as e:
            print(f"Произошла ошибка во время выполнения операции: {e}")
    def fetch_videos_db(self):
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

                print(records)
                return records
                # return []
        except Exception as e:
            print("Произошла ошибка во время выполнения операции вставки: %s", e)

    def delete_videos_db(self, id):
        try:
            with db.connect(self.db) as connection:
                cursor = connection.cursor()
                cursor.execute('''
                        DELETE FROM video
                        WHERE id = ?
                    ''', (id,))
                connection.commit()
                print(f"Видео с id {id} успешно удалено из базы данных.")
        except Exception as e:
            print(f"Произошла ошибка во время выполнения операции удаления: {e}")

    def insert_video_into_db(self, video):
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
            print("Произошла ошибка во время выполнения операции вставки: %s", e)

    def update_video_in_db(self, video):
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
                               (
                                   video['video_name'],
                                   video['video_desc'],
                                   video['video_format'],
                                   video['video_date'],
                                   video['video_path'],
                                   video['video_icon'],
                                   video['id']))
                connection.commit()
        except Exception as e:
            print(f"Произошла ошибка во время выполнения операции обновления: {e}")



    def try_to_find(self, url):
        try:
            self.pytube_instance = YouTube(url,
                                           on_progress_callback=self.on_progress,
                                           on_complete_callback=self.on_complete)
            return True

        except Exception as e:
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

    def fetch_frames_per_second(self, streams):

        result = []
        for stream in streams:
            fps = stream.fps
            if fps and fps not in result:
                result.append(fps)
        return result

    def select_suit_stream(self):

        self.video_for_downloading['suit_video_stream'] = self.video_for_downloading['filtered_streams'].first()
        self.video_for_downloading['suit_audio_stream'] = (self.pytube_instance.streams
                                                           .filter(only_audio=True, file_extension='mp4')
                                                           .order_by('abr')
                                                           .desc()
                                                           .first())

    def get_additional_download_data(self):
        return {
            'resolutions': self.video_for_downloading['resolutions'],
            'formats': self.video_for_downloading['formats'],
            'fps': self.video_for_downloading['fps']
        }

    def update_streams_by_filter(self, res=None, fmt=None, fps=None):
        query = self.pytube_instance.streams.filter(progressive=False)
        self.video_for_downloading['resolutions'] = self.fetch_resolutions(query)

        if res:
            query = query.filter(res=res)
            self.video_for_downloading['formats'] = self.fetch_formats(query)
        if fmt:
            query = query.filter(file_extension=fmt)
            self.video_for_downloading['fps'] = self.fetch_frames_per_second(query)
        if fps:
            query = query.filter(fps=int(fps))

        self.video_for_downloading['filtered_streams'] = query.order_by('resolution').desc()

    def check_download_video_data(self, data):
        name = self.video_for_downloading['video_name']
        format = data['format']
        path = data['path']
        if path == "default":
            path = self.download_directory

        first_check = self.check_directory_exists(data['path'])
        if first_check:
            self.video_for_downloading['user_format'] = format
            self.video_for_downloading['user_full_path'] = f"{path}/{name}.{format}"

            return True
        else:
            return False

    def download_video_thread(self):
        video_filename = self.video_for_downloading['suit_video_stream'].download(output_path='../../app/appData/')
        audio_filename = self.video_for_downloading['suit_audio_stream'].download(output_path='../../app/appData/')


        input_video = ffmpeg.input(video_filename)
        input_audio = ffmpeg.input(audio_filename)
        output_video = self.video_for_downloading['user_full_path']

        try:
            ffmpeg.output(input_video, input_audio, output_video, codec='copy').overwrite_output().run(
                quiet=True)

            message = f"READY"

            os.remove(video_filename)
            os.remove(audio_filename)

            self.append_after_download()
            self.controller.download_end(message)
        except Exception as e:
            print(e)




    def on_progress(self, stream, chunk, bytes_remaining):
        total_size = stream.filesize
        bytes_downloaded = total_size - bytes_remaining
        percentage = (bytes_downloaded / total_size) * 100
        message = f"Downloading {stream.type}. ({percentage:.2f}%)"
        self.controller.download_going(message)

    def on_complete(self, stream, file_path):
        message = f"Downloaded {stream.type}"
        if stream.type == "audio":
            message = f"Downloaded {stream.type}. Processing ..."
        self.controller.download_going(message)

    def start_download(self):
        self.select_suit_stream()
        thread = threading.Thread(target=self.download_video_thread)
        thread.start()

    def fetching_common_data_thread(self):

        self.video_for_downloading['video_name'] = self.pytube_instance.title
        self.video_for_downloading['thumbnail_url'] = self.pytube_instance.thumbnail_url
        self.video_for_downloading['video_icon'] = f"../../app/appData/temp/preview.jpg"
        self.video_for_downloading['filtered_streams'] = self.pytube_instance.streams.filter(progressive=False)

        response = requests.get(self.video_for_downloading['thumbnail_url'])

        if response.status_code == 200:

            file_name = self.video_for_downloading['video_icon']
            with open(file_name, 'wb') as f:
                f.write(response.content)
            self.controller.common_download_data_ready(True)

        else:
            self.controller.common_download_data_ready(False)

    def fetch_common_download_data(self):
        thread = threading.Thread(target=self.fetching_common_data_thread)
        thread.start()

    def get_common_download_data(self):
        self.update_streams_by_filter()
        data = {
            "video_name": self.video_for_downloading['video_name'],
            "video_icon": self.video_for_downloading['video_icon'],
            "resolutions": self.video_for_downloading['resolutions']
        }
        return data


    def append_after_download(self):
        creation_time = os.path.getctime(self.video_for_downloading['user_full_path'])
        formatted_date = datetime.fromtimestamp(creation_time).strftime('%d.%m.%Y')


        video_data = {
            "video_name": self.video_for_downloading['video_name'],
            "video_desc": "-",
            "video_format": self.video_for_downloading['user_format'],
            "video_date": formatted_date,
            "video_path": self.video_for_downloading['user_full_path'],
            "video_icon": self.video_for_downloading['video_icon']
        }
        last_id = int(self.insert_video_into_db(video_data))


        name = str(last_id)
        temp_icon_path = f"../../app/appData/temp/preview.jpg"
        formated_icon_path = f"../../app/appData/videoIcons/{name}.jpg"
        os.rename(temp_icon_path, formated_icon_path)

        video_data["video_icon"] = formated_icon_path
        video_data["id"] = last_id

        self.update_video_in_db(video_data)



