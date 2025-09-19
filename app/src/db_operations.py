import sqlite3 as db
from app_exceptions import *


def create_database(database):
    try:
        with db.connect(database) as connection:
            cursor = connection.cursor()

            cursor.execute('''CREATE TABLE IF NOT EXISTS "video" (
                   "id" INTEGER PRIMARY KEY AUTOINCREMENT,
                   "video_name" TEXT NOT NULL UNIQUE,
                   "video_desc" TEXT NOT NULL,
                   "video_format" TEXT NOT NULL,
                   "video_date" TEXT NOT NULL,
                   "video_path" TEXT NOT NULL UNIQUE,
                   "video_icon" TEXT
               )''')

            cursor.execute("PRAGMA table_info('video')")
            existing_columns = [column[1] for column in cursor.fetchall()]
            required_columns = ["id", "video_name", "video_desc", "video_format", "video_date", "video_path",
                                "video_icon"]

            for column in required_columns:
                if column not in existing_columns:
                    cursor.execute(f"ALTER TABLE video ADD COLUMN {column} TEXT")

    except Exception as e:
        raise DatabaseOperationError(message="Error", operation="on read", trouble=e)


def update_video_db(database, video):
    try:
        with db.connect(database) as connection:
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


def read_videos_db(database):
    try:
        with db.connect(database) as connection:
            cursor = connection.cursor()
            cursor.execute('''
                SELECT 
                id, video_name, video_desc, video_format, video_date,
                video_path, video_icon
                FROM 
                video
                ORDER BY video_name''')
            columns = [column[0] for column in cursor.description]
            records = [dict(zip(columns, record)) for record in cursor.fetchall()]
            return records
    except Exception as e:
        raise DatabaseOperationError(message="Error", operation="on read", trouble=e)


def delete_video_db(database, video_id):
    try:
        with db.connect(database) as connection:
            cursor = connection.cursor()
            cursor.execute('''
                DELETE FROM video
                WHERE id = ?
            ''', (video_id,))
            connection.commit()
    except Exception as e:
        raise DatabaseOperationError(message="Error", operation="on delete", trouble=e)


def create_video_db(database, video):
    try:
        with db.connect(database) as connection:
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
                (video['video_name'],
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