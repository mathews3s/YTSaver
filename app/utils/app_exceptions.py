
class DatabaseOperationError(Exception):
    def __init__(self, message, operation, trouble):
        super().__init__(message)
        self.operation = operation
        self.trouble = trouble


class FfmpegError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.title = "ffmpeg error"


class DownloadVideoStreamError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.title = "video stream error"


class DownloadAudioStreamError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.title = "audio stream error"


class DownloadPreviewError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.title = "download preview error"


class CommonDataFetchError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.title = "download common data error"



class VideoStreamsDownloadError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.title = "download common data error"


class AddingDownloadVideoDatabaseError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.title = "adding db downloaded video error"


class PreparingDownloadedVideoDataError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.title = "preparing data of downloaded video for db  error"


class EditVideoError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.title = "edit data in db error"


class DeleteVideoError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.title = "delete data from db error"


class CheckingDataForVideoError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.title = "while checking data error"


class FindingPytubeVideoError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.title = "delete data from db error"


class ClearingDirectoryError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.title = "delete data from db error"
