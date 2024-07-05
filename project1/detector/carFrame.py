import numpy as np
from PyQt5.QtWidgets import QDialog, QApplication
from project1.detector.DetectorFrameUI import DetectorDialog
from project1.detector.video import Video
import sys


class DetectorFrame(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = DetectorDialog()
        self.ui.setupUi(self)

        self.video_thread = Video('/Users/baozi/summer_training/project1/data/demo1.mp4')
        self.video_thread.send.connect(self.show_image_and_count)
        self.video_thread.start()

    def show_image_and_count(self, h, w, c, b, th_id, num):
        frame = np.frombuffer(b, dtype=np.uint8).reshape(h, w, c)
        self.ui.update_frame(frame)
        self.ui.update_vehicle_count(num)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = DetectorFrame()
    mainWindow.show()
    sys.exit(app.exec_())
