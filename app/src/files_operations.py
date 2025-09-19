import os
import uuid
import re
import ffmpeg
from app_exceptions import *
import shutil

def clear_directory(directory):
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as err:
            raise ClearingDirectoryError(err)


def get_file_extension(absolute_path, with_dot: bool = True):
    if with_dot:
        return os.path.splitext(absolute_path)[1]
    else:
        return os.path.splitext(absolute_path)[1][1:]

def get_file_name(absolute_path):
    return os.path.splitext(os.path.basename(absolute_path))[0]



def normalize_path(path: str):
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

def check_file_exist(path_to_file):
    if not os.path.exists(path_to_file):
        return False
    else:
        return True

def get_full_path(path:str):
    return os.path.abspath(path)


def check_file_name(path: str):
    pattern = r'^[\w\sа-яА-ЯёЁ\-_.]+$'
    if re.match(pattern, path):
        return True
    else:
        return False


def concat_audio_video_files(video_file, audio_file, output_temp_video_path, output_temp_name,
                             output_path):
    try:

        input_video = ffmpeg.input(video_file)
        input_audio = ffmpeg.input(audio_file)

        output_format = get_file_extension(video_file)
        output_temp_video_name = output_temp_name + output_format
        output_temp_video = os.path.join(output_temp_video_path, output_temp_video_name)
        
        ffmpeg.output(input_video, input_audio, output_temp_video, codec='copy').overwrite_output().run(quiet=True)
        
        auto_name = generate_unique_filename() + output_format
        output_video = os.path.join(output_path, auto_name)
        
        os.rename(output_temp_video, output_video)

        return output_video

    except Exception as err:
        raise FfmpegError(err)
