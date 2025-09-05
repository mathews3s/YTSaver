import sqlite3 as db
import json
import copy


class Model:
    def __init__(self):
        self.db = "../appData/database.db"

        self.founded_videos = self.fetch_videos_db()
        self.founded_count = len(self.founded_videos)

        self.video_1 = None
        self.video_2 = None
        self.current_video = None
        self.offset_collection = 0
        # self.setup_current_videos()

    def get_videos_info(self):
        info = {
            'first': self.video_1,
            'second': self.video_2,
            'current': self.current_video
        }
        return info

    def get_videos_count(self):
        return len(self.founded_videos)

    def set_video_as_current(self, video):
        self.current_video = copy.deepcopy(video)


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
                records = cursor.fetchall()
                print(records)
                # return records
                return []
        except Exception as e:
            print("Произошла ошибка во время выполнения операции вставки: %s", e)




    def setup_current_videos(self):
        item1 = None
        item2 = None
        try:
            item1 = self.founded_videos[0 + self.offset_collection]
            item2 = self.founded_videos[1 + self.offset_collection]
        except Exception as e:
            print("Произошла ошибка во время выбора playlists", e)
        if (item1 is None) and (not (item2 is None)):
            self.transform_in_dict(self.video_1, item2)
        elif (item2 is None) and (not (item1 is None)):
            self.transform_in_dict(self.video_1, item1)
            self.video_2 = None
        elif (not item1 is None) and (not item2 is None):
            self.video_1 = {}
            self.video_2 = {}
            self.transform_in_dict(self.video_1, item1)
            self.transform_in_dict(self.video_2, item2)

    def transform_in_dict(self, playlist_dict, playlist_tuple):
        keys = ['id', 'name', 'desc', 'format', 'date', 'path', 'icon']
        for key, value in zip(keys, playlist_tuple):
            playlist_dict[key] = value

    def videos_offset_up(self):
        if self.offset_collection > 0:
            self.offset_collection -= 2

    def videos_offset_down(self):
        if self.offset_collection < self.founded_count - 2:
            self.offset_collection += 2
            print(self.offset_collection)





































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