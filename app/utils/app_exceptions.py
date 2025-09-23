# there are all exceptions in app

class DatabaseOperationError(Exception):
    def __init__(self, message, operation, trouble):
        super().__init__(message)
        self.operation = operation
        self.trouble = trouble


class FfmpegError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.title = "ffmpeg processing error"


class DownloadStreamError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.title = "download stream error"


class DownloadPreviewError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.title = "download preview error"


class CommonDataFetchError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.title = "download common data error"


class FindingVideoError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.title = "finding video error"


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
        self.title = "edited data checking error"


class ClearingDirectoryError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.title = "clearing temp folder error"


class AppDirectoriesConstructingError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.title = "constructing app folders error"
