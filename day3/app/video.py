import cv2
from PyQt5.QtCore import QThread


class Video(QThread):
    def __init__(self, parent=None):
        super(Video, self).__init__(parent)
        self.video = cv2.VideoCapture(0)
        self.video.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        self.video.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        self.video.set(cv2.CAP_PROP_FPS, 60)
        self.video.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
        self.video.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
        self.video.set(cv2.CAP_PROP_FRAME_WIDTH, 128)
        self.video.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
        self.video.set(cv2.CAP_PROP_FPS, 30)
        self.video.set(cv2.CAP_PROP_FRAME_WIDTH, 128)
        self.video.set(cv2.CAP_PROP_FRAME_HEIGHT, 128)
        self.video.set(cv2.CAP_PROP_FRAME_WIDTH, 128)
        self.video.set(cv2.CAP_PROP_FRAME_HEIGHT, 128)
