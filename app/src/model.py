import sqlite3 as db
import json
import copy
import os
import time
from datetime import datetime


class Model:
    def __init__(self):
        self.db = "../appData/database.db"
        self.download_directory = "../../download"

        self.founded_videos = None
        self.videos_count = None
        self.video_1 = None
        self.video_2 = None
        self.current_video = None
        self.offset_collection = 0




    def update_storages(self):
        # проверяю записи в бд на их существование в NTFS
        self.check_videos_in_db()

        # проверяю баз. дир на наличие файлов
        if self.check_default_directory_exists():
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




    def check_default_directory_exists(self):
        if not os.path.exists(self.download_directory):
            os.makedirs(self.download_directory)
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
                                    WHERE video_id = ?''',
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
