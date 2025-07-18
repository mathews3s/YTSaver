import sqlite3 as db
import json




class Model:
    def __init__(self):
        self.db = "../appData/database.db"

    def get_default_settings(self):
        with open('../appData/default-app-settings.json', 'r') as file:
            parsed = json.load(file)
        return parsed

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

    def get_icon_of_playlist(self, playlist):
        pass

    def get_two_playlist(self, id_first_pl):
        try:
            with db.connect(self.db) as connection:
                cursor = connection.cursor()
                cursor.execute('''
                    SELECT 
                    playlist_name, playlist_count_videos, 
                    playlist_path, playlist_icon, playlist_date
                    FROM playlist 
                    WHERE id >= ? 
                    LIMIT 2''', (id_first_pl,))
                playlists = cursor.fetchall()
                print(playlists)
        except Exception as e:
            print("Произошла ошибка во время выполнения операции вставки: %s", e)

    def get_first_playlists_id(self):
        try:
            with db.connect(self.db) as connection:
                cursor = connection.cursor()
                cursor.execute('''
                    SELECT id
                    FROM playlist 
                    LIMIT 2''', (id_first_pl,))
                playlists = cursor.fetchall()
                print(playlists)
        except Exception as e:
            print("Произошла ошибка во время выполнения операции вставки: %s", e)