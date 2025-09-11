import sqlite3 as db
import json
import copy
import os
import time
import re
from datetime import datetime
from pytubefix import YouTube as YTManager
import ffmpeg
import threading

test_url = "https://www.youtube.com/watch?v=K6rKRdayW78"


class Model:
    def __init__(self):
        self.db = "../appData/database.db"
        self.download_directory = "../../download"
        self.controller = None

        self.founded_videos = None
        self.videos_count = None
        self.video_1 = None
        self.video_2 = None
        self.current_video = None
        self.offset_collection = 0

        self.download_url = None
        self.manager = {
            'youtube_obj' : None,
            'streams': None,
            'suit_video_stream': None,
            'suit_audio_stream': None,
            'video_name': None,
            'resolutions' : None,
            'formats': None,
            'fps': None
        }

    def set_feedback(self, cntrl):
        self.controller = cntrl


    def update_storages(self):
        # проверяю записи в бд на их существование в NTFS
        self.check_videos_in_db()

        # проверяю баз. дир на наличие файлов
        if self.check_directory_exists(self.download_directory):
            self.check_default_directory()

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

    def find_videos_in_directory(self, dir):
        video_extensions = ('.mp4', '.avi', '.mov', '.mkv', '.wmv', '.flv')  # Расширения видеофайлов
        videos = []

        for root, dirs, files in os.walk(dir):
            for file in files:
                if file.lower().endswith(video_extensions):
                    full_path = os.path.abspath(os.path.join(root, file))
                    video_format = os.path.splitext(file)[1][1:]
                    creation_time = os.path.getctime(full_path)
                    formatted_date = datetime.fromtimestamp(creation_time).strftime('%d.%m.%Y')

                    videos.append({
                        'video_name': file,
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
        videos_to_change = []
        videos = self.fetch_videos_db()

        for video in videos:
            video_path = video['video_path']
            icon_path = video['video_icon']
            id = video['id']

            if os.path.exists(video_path):
                if not icon_path == 'nf':
                    if not os.path.exists(icon_path):
                        videos_to_change.append(video)
            else:
                videos_to_remove.append(video)

            for video in videos_to_remove:
                self.delete_video(video, False)


    def set_videos_from_db(self):
        self.founded_videos = self.fetch_videos_db()

    def get_videos_info(self):
        info = {
            'first': self.video_1,
            'second': self.video_2,
            'current': self.current_video
        }
        return info

    def update_videos_count(self):
        self.videos_count = len(self.founded_videos)

    def get_videos_count(self):
        return self.videos_count

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

    def check_file_name(self, filename):
        pattern = r"^[a-zA-Z0-9_.-]+$"

        if re.match(pattern, filename):
            return True
        else:
            return False

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

    def update_video_info(self, new_info, with_replace):
        self.update_video_in_db(new_info)
        if with_replace:
            os.rename(self.current_video['video_path'], new_info['video_path'])

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
            connection.commit()
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
        # test_url = "https://www.youtube.com/watch?v=mRfUpvpEasQ"
        try:
            self.manager['youtube_obj'] = YTManager(url, on_progress_callback=self.on_progress)
            self.manager['video_name'] = self.manager['youtube_obj'].title
            self.update_streams_by_filter()

            return True

        except Exception as e:
            return False

    def fetch_resolutions(self):

        resolutions = []
        for stream in self.manager['streams']:
            resolution = stream.resolution
            if resolution and resolution not in resolutions:
                resolutions.append(resolution)
        return resolutions

    def fetch_formats(self):

        formats = []
        for stream in self.manager['streams']:
            format = stream.subtype
            if format and format not in formats:
                formats.append(format)
        return formats

    def fetch_frames_per_second(self):

        result = []
        for stream in self.manager['streams']:
            fps = stream.fps
            if fps and fps not in result:
                result.append(fps)
        return result

    def select_suit_stream(self):

        self.manager['suit_video_stream'] = self.manager['streams'].first()
        self.manager['suit_audio_stream'] = (self.manager['youtube_obj'].streams
                                             .filter(only_audio=True, file_extension='mp4')
                                             .order_by('abr')
                                             .desc()
                                             .first())

    def get_suitable_streams_information(self):
        return {
            'video_name': self.manager['video_name'],
            'resolutions': self.manager['resolutions'],
            'formats': self.manager['formats'],
            'fps': self.manager['fps']
        }

    def update_streams_by_filter(self, res=None, fmt=None, fps=None):

        if res and fmt and fps:
            self.manager['streams'] = (self.manager['youtube_obj']
                                       .streams.filter(progressive=False, res=res, file_extension=fmt, fps=int(fps) )
                                       .order_by('resolution')
                                       .desc())
        elif res and fmt:
            self.manager['streams'] = (self.manager['youtube_obj']
                                       .streams.filter(progressive=False, res=res, file_extension=fmt)
                                       .order_by('resolution')
                                       .desc())
            self.manager['fps'] = self.fetch_frames_per_second()
        elif res:
            self.manager['streams'] = (self.manager['youtube_obj']
                                       .streams.filter(progressive=False,res=res)
                                       .order_by('resolution')
                                       .desc())
            self.manager['formats'] = self.fetch_formats()
        else:
            self.manager['streams'] = (self.manager['youtube_obj']
                                       .streams.filter(progressive=False)
                                       .order_by('resolution')
                                       .desc())
            self.manager['resolutions'] = self.fetch_resolutions()

    def check_download_video_data(self, data):
        first_check = self.check_directory_exists(data['path'])
        if first_check:
            return True
        else:
            return False

    def download_video(self):
        video_filename = self.manager['suit_video_stream'].download()
        audio_filename = self.manager['suit_audio_stream'].download()

        input_video = ffmpeg.input(video_filename)
        input_audio = ffmpeg.input(audio_filename)

        ffmpeg.output(input_video, input_audio, "../finishedVid.mp4", codec='copy').overwrite_output().run(
            quiet=True)
        return True

    def on_progress(self, stream, chunk, bytes_remaining):
        total_size = stream.filesize
        bytes_downloaded = total_size - bytes_remaining
        percentage = (bytes_downloaded / total_size) * 100
        print(f"Downloaded {bytes_downloaded} out of {total_size} bytes ({percentage:.2f}%)")
        self.feedback.download_going()

    def start_download(self):

        self.select_suit_stream()
        thread = threading.Thread(target=self.download_video)
        thread.start()

