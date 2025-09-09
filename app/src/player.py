
import cv2
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import QTimer
from PyQt5.QtCore import Qt


class VideoPlayer():
    def __init__(self, video_path, output_widget, pause_widget, forward_widget, back_widget, time_widget):

        self.video_path = video_path
        self.cap = cv2.VideoCapture(video_path)
        self.paused = False

        self.video_widget = output_widget

        self.play_button = pause_widget
        self.play_button.clicked.connect(self.toggle_pause)

        self.seek_forward_button = forward_widget
        self.seek_forward_button.clicked.connect(self.seek_forward)

        self.seek_backward_button = back_widget
        self.seek_backward_button.clicked.connect(self.seek_backward)


        self.timer = QTimer()
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(25)

        self.time_widget = time_widget

    def toggle_pause(self):
        self.paused = not self.paused

    def seek_forward(self):
        current_pos = self.cap.get(cv2.CAP_PROP_POS_MSEC)
        self.cap.set(cv2.CAP_PROP_POS_MSEC, current_pos + 10000)

    def seek_backward(self):
        current_pos = self.cap.get(cv2.CAP_PROP_POS_MSEC)
        self.cap.set(cv2.CAP_PROP_POS_MSEC, max(current_pos - 10000, 0))

    def update_frame(self):
        if not self.paused:
            ret, frame = self.cap.read()
            if not ret:
                self.cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
                return

            total_seconds = self.cap.get(cv2.CAP_PROP_POS_MSEC) / 1000


            minutes = int(total_seconds // 60)
            seconds = int(total_seconds % 60)


            self.time_widget.setText(f"{minutes:02d}:{seconds:02d}")

            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            height, width, channel = frame.shape
            bytes_per_line = 3 * width
            q_img = QImage(frame.data, width, height, bytes_per_line, QImage.Format_RGB888)


            pixmap = QPixmap.fromImage(q_img).scaled(self.video_widget.size(), aspectRatioMode=Qt.KeepAspectRatio)

            self.video_widget.setPixmap(pixmap)
            self.video_widget.setAlignment(Qt.AlignCenter)
    def close_video(self):
        self.cap.release()

