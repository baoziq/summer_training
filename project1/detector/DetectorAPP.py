from PyQt5.QtWidgets import QApplication
from project1.detector.MainFrame import MainFrame
import sys


class DetectorApp(QApplication):
    def __init__(self):
        super(DetectorApp, self).__init__(sys.argv)
        self.dialog = MainFrame()
        self.dialog.show()
