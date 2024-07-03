from PyQt5.Qt import Qt
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QDialog
from app.mdui import Ui_Dialog
import cv2 as cv
from ai.haha import DistortEffect
class MainDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.e = DistortEffect()
        self.img = cv.imread('data/1.jpg')
        self.showimg()

    def showimg(self):
        # opencv图片 =>QImage=>QPixmap=>按比例缩放==>QT labels显示
        h, w, c = self.img.shape
        img_bytes= self.img.tobytes()

        imgae = QImage(img_bytes, w, h, w * c, QImage.Format_BGR888)
        pix = QPixmap.fromImage(imgae)
        # 自动缩放
        width = self.ui.label_2.width()
        height = self.ui.label_2.height()
        scale_pix = pix.scaled(width, height, Qt.KeepAspectRatio)
        self.ui.label_2.setPixmap(scale_pix)

    def big(self):
        self.img = self.e.MinFrame(self.img)
        self.showimg()

