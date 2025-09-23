import sqlite3 as db
from app.utils.app_exceptions import *

# there are functions for all database manipulating in app


def create_database(database: str):
    """
        Creates a database with the necessary video table structure for storing video information.

        Parameters:
        - database (str): The name of the database.

        Raises:
        - DatabaseOperationError: If an error occurs during the database creation operation.

        Returns:
        - None
    """

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
        raise DatabaseOperationError(message="Error", operation="on create_db", trouble=e)


def update_video_db(database: str, video: dict):
    """
        Updates a video record in the database.

        Parameters:
        - database (str): The name of the database.
        - video (dict): The video data to be updated.

        Raises:
        - DatabaseOperationError: If an error occurs during the database update operation.

        Returns:
        - None
    """

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


def read_videos_db(database: str):
    """
        Reads video records from the database.

        Parameters:
        - database (str): The name of the database.

        Returns:
        - list: List of video records.

        Raises:
        - DatabaseOperationError: If an error occurs during the database read operation.
    """

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


def delete_video_db(database: str, video_id: int):
    """
        Deletes a video record from the database based on the provided video ID.

        Parameters:
        - database (str): The name of the database.
        - video_id (int): The ID of the video to be deleted.

        Raises:
        - DatabaseOperationError: If an error occurs during the database delete operation.

        Returns:
        - None
    """

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


def create_video_db(database: str, video: dict):
    """
        Creates a new video record in the database.

        Parameters:
        - database (str): The name of the database.
        - video (dict): The video data to be inserted.

        Returns:
        - int: The ID of the newly created video record.

        Raises:
        - DatabaseOperationError: If an error occurs during the database insert operation.
    """

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