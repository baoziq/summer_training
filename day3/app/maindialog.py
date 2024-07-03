from PyQt5.QtWidgets import QDialog
from app.mdui import Ui_Dialog
class MainDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

