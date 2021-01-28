from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette
from PyQt5.QtWidgets import QWidget, QLabel


class Canvas(QWidget):
    def __init__(self):
        super().__init__()
        self.setAutoFillBackground(True)
        self.setBackgroundRole(QPalette.Base)
        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.white)
        self.setPalette(p)