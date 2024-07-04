import cv2
from PyQt5.QtCore import QThread, pyqtSignal


# 重写run方法：线程执行的内容
# Thread的实例对象 start run就会自动执行
class Video(QThread):
    # 使用信号与槽函数向外传递数据
    #       发送者     video
    #       信号类型   自定义信号类型
    #       槽函数     （）
    send = pyqtSignal(int, int, int, bytes)

    def __init__(self, parent=None):
        super(Video, self).__init__(parent)
        # 准备工作
        self.dev = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    # 重写run方法
    def run(self):
        # 耗时操作
        while True:
            ret, frame = self.dev.read()
            h, w, c = frame.shape()
            img_bytes = frame.tobytes()
            self.send.emit(h, w, c, img_bytes)
            QThread.usleep(1000000)


