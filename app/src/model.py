import sqlite3 as db
import json


class Model:
    def __init__(self):
        self.db = "../appData/database.db"

        self.playlists = self.get_playlists_db()
        self.playlists_count = self.get_playlists_count_db()

        self.playlist_1 = None
        self.playlist_2 = None
        self.selected_playlist = None
        self.offset_playlists = 0
        self.setup_current_playlists()

        self.videos = None
        self.videos_count = None

        self.video_1 = None
        self.video_2 = None
        self.selected_video = None
        self.offset_videos = 0

    def get_playlists_count(self):
        return self.playlists_count

    def get_current_playlists_info(self):
        return self.playlist_1, self.playlist_2, self.selected_playlist

    def set_playlist1_as_current(self):
        self.selected_playlist = self.playlist_1

    def set_playlist2_as_current(self):
        self.selected_playlist = self.playlist_2






    def get_videos_count(self):
        return self.videos_count

    def get_current_videos_info(self):
        return self.video_1, self.video_2, self.selected_video

    def set_video1_as_current(self):
        self.selected_video = self.video_1

    def set_video2_as_current(self):
        self.selected_video = self.video_2










    def get_playlists_db(self):
        try:
            with db.connect(self.db) as connection:
                cursor = connection.cursor()
                cursor.execute('''
                    SELECT 
                    id, playlist_name, playlist_count_videos, 
                    playlist_path, playlist_icon, playlist_date
                    FROM 
                    playlist
                    ORDER BY playlist_name''')
                playlists = cursor.fetchall()
                print(playlists)
                return playlists
        except Exception as e:
            print("Произошла ошибка во время выполнения операции вставки: %s", e)

    def get_playlists_count_db(self):
        try:
            with db.connect(self.db) as connection:
                cursor = connection.cursor()
                cursor.execute('''
                    SELECT COUNT(*)
                    FROM 
                    playlist''')
                count = cursor.fetchone()[0]
                print(count)
                return count
        except Exception as e:
            print("Произошла ошибка во время выполнения операции вставки: %s", e)

    def setup_current_playlists(self):
        item1 = None
        item2 = None
        try:
            item1 = self.playlists[0 + self.offset_playlists]
            item2 = self.playlists[1 + self.offset_playlists]
        except Exception as e:
            print("Произошла ошибка во время выбора playlists", e)
        if (item1 is None) and (not (item2 is None)):
            self.playlist_1 = item2
            self.playlist_2 = None
        elif (item2 is None) and (not (item1 is None)):
            self.playlist_1 = item1
            self.playlist_2 = None
        else:
            self.playlist_1 = item1
            self.playlist_2 = item2

    def playlists_offset_up(self):
        if self.offset_playlists > 0:
            self.offset_playlists -= 2

    def playlists_offset_down(self):
        if self.offset_playlists < self.playlists_count - 1:
            self.offset_playlists += 2
            print(self.offset_playlists)












    def get_videos_db(self):
        try:
            with db.connect(self.db) as connection:
                cursor = connection.cursor()
                cursor.execute('''
                    SELECT 
                    id, video_name, video_desc, video_format, video_date
                    playlist_path, playlist_icon, playlist_date
                    FROM 
                    video
                    ORDER BY video_name''')
                playlists = cursor.fetchall()
                print(playlists)
                return playlists
        except Exception as e:
            print("Произошла ошибка во время выполнения операции вставки: %s", e)

    def get_videos_count_db(self):
        try:
            with db.connect(self.db) as connection:
                cursor = connection.cursor()
                cursor.execute('''
                    SELECT COUNT(*)
                    FROM
                    video''')
                count = cursor.fetchone()[0]
                print(count)
                return count
        except Exception as e:
            print("Произошла ошибка во время выполнения операции вставки: %s", e)

    def setup_current_videos(self):
        item1 = None
        item2 = None
        try:
            item1 = self.videos[0 + self.offset_videos]
            item2 = self.videos[1 + self.offset_videos]
        except Exception as e:
            print("Произошла ошибка во время выбора videos", e)
        if (item1 is None) and (not (item2 is None)):
            self.video_1 = item2
            self.video_2 = None
        elif (item2 is None) and (not (item1 is None)):
            self.video_1 = item1
            self.video_2 = None
        else:
            self.video_1 = item1
            self.video_2 = item2

    def videos_offset_up(self):
        if self.offset_videos > 0:
            self.offset_videos -= 2

    def videos_offset_down(self):
        if self.offset_videos < self.videos_count - 1:
            self.offset_videos += 2
            print(self.offset_videos)





















    def get_default_settings(self):
        with open('../appData/default-app-settings.json', 'r') as file:
            parsed = json.load(file)
        return parsed

    def insert_playlist_into_db(self, ):
        try:
            with db.connect(self.db) as connection:
                cursor = connection.cursor()
                cursor.execute('''
                    INSERT INTO playlist (
                        playlist_name, 
                        playlist_count_videos,
                        playlist_path, 
                        playlist_icon)
                    VALUES (?, ?, ?, ?)''',
                ("f1", "en", 1, "../../"))
                connection.commit()
        except Exception as e:
            print("Произошла ошибка во время выполнения операции вставки: %s", e)


    def insert(self):
         try:
             with db.connect(self.db) as connection:
                 cursor = connection.cursor()
                 cursor.execute('''
                     INSERT INTO SETTINGS_SET
                     (SET_NAME, LANGUAGE, DASH_ALLOW, DEF_PATH)
                     VALUES (?, ?, ?, ?)''',
                 ("f1", "en", 1, "../../"))
                 connection.commit()
         except Exception as e:
             print("Произошла ошибка во время выполнения операции вставки: %s", e)