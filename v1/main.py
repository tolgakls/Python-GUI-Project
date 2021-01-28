import sys
import traceback

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QMenuBar, QAction, QHBoxLayout, QPushButton

from canvas import Canvas

title = "GUI PROJECT"


class MainWindow(QWidget):
    def __init__(self):
        try:
            super().__init__()
            self.canvas = Canvas()
            self.setupUI()
        except Exception as e:
            print(e)
            exc_info = sys.exc_info()
            traceback.print_exception(*exc_info)

    def setupUI(self):
        self.setWindowTitle(title)
        self.setFixedSize(600, 400)

        mainLayout = QVBoxLayout()
        mainLayout.setContentsMargins(0, 0, 0, 0)

        menubar = QMenuBar()
        mainLayout.addWidget(menubar)

        saveAction = QAction("&Save...", self)
        saveAction.triggered.connect(self.save)

        loadAction = QAction("&Load...", self)
        loadAction.triggered.connect(self.load)

        fileMenu = menubar.addMenu("&File")
        fileMenu.addAction(saveAction)
        fileMenu.addAction(loadAction)

        appLayout = QHBoxLayout()
        appLayout.setContentsMargins(10, 0, 10, 10)
        btnLayout = QVBoxLayout()
        btnLayout.setContentsMargins(10, 0, 10, 0)

        self.block_btn = QPushButton("BLOCK")
        self.block_btn.clicked.connect(self.draw_block)
        btnLayout.addWidget(self.block_btn)

        self.input_btn = QPushButton("INPUT")
        self.input_btn.clicked.connect(self.draw_input)
        btnLayout.addWidget(self.input_btn)

        self.output_btn = QPushButton("OUTPUT")
        self.output_btn.clicked.connect(self.draw_output)
        btnLayout.addWidget(self.output_btn)

        self.inout_btn = QPushButton("INOUT")
        self.inout_btn.clicked.connect(self.draw_output)
        btnLayout.addWidget(self.inout_btn)

        appLayout.addLayout(btnLayout, 1)
        appLayout.addWidget(self.canvas, 16)
        mainLayout.addLayout(appLayout, 1)
        self.setLayout(mainLayout)

    def save(self):
        pass

    def load(self):
        pass

    def draw_block(self):
        pass

    def draw_input(self):
        pass

    def draw_output(self):
        pass

    def draw_inout(self):
        pass


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    w = MainWindow()
    w.show()

    sys.exit(app.exec_())
