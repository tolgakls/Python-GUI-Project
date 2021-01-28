import sys
import traceback

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QMenuBar, QAction, QHBoxLayout, QTabWidget, QTextEdit
from PyQt5 import QtCore

from canvas import Canvas, InputPort, OutputPort

title = "GUI PROJECT"

# Explaın the flow of the code
# Explaın the purpose of each class
# Example: MaınWındow class: Thıs class has so and so components and ıt's prımary objectıve ıs ...


class MainWindow(QWidget):
    def __init__(self):
        try:
            super().__init__()
            self.setupUI()
        except Exception as e:
            print(e)
            exc_info = sys.exc_info()
            traceback.print_exception(*exc_info)

    def setupUI(self):
        self.in_order = 0  # input port order
        self.out_order = 0  # output port order
        self.canvas = Canvas()

        self.setWindowTitle(title)
        self.setFixedSize(600, 400)

        mainLayout = QVBoxLayout()
        mainLayout.setContentsMargins(0, 0, 0, 0)

        tabLayout = QVBoxLayout()
        # Initialize tab screen
        self.tabs = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()

        # Add tabs
        # Explaın WHY do we add tabs?
        self.tabs.addTab(self.tab1, "Code Editor")
        self.tabs.addTab(self.tab2, "RTL Design")

        # Create first tab
        self.tab1.layout = QVBoxLayout(self)
        self.textEdit = QTextEdit()
        self.tab1.layout.addWidget(self.textEdit)
        self.tab1.setLayout(self.tab1.layout)

        # Create second tab
        self.tab2.layout = QVBoxLayout(self)
        self.tab2.layout.addWidget(self.canvas, 16)
        self.tab2.setLayout(self.tab2.layout)

        # Add tabs to widget
        tabLayout.addWidget(self.tabs)

        menubar = QMenuBar()
        mainLayout.addWidget(menubar)

        # Under file menu, Save action is used to save block design and written code
        saveAction = QAction("&Save...", self)
        saveAction.triggered.connect(self.save)

        # Under file menu, Load action is used to load block design or written code
        loadAction = QAction("&Load...", self)
        loadAction.triggered.connect(self.load)

        # Under file menu, Add Input Port action is used to add input port to both code and block
        inputAction = QAction("&Add Input Port...", self)
        inputAction.triggered.connect(self.draw_input)

        # Under file menu, Add Output Port action is used to add output port to both code and block
        outputAction = QAction("&Add Output Port...", self)
        outputAction.triggered.connect(self.draw_output)

        # Under file menu, Add Inout Port action is used to add inout port to both code and block
        inoutAction = QAction("&Add Inout Port...", self)
        inoutAction.triggered.connect(self.draw_inout)

        fileMenu = menubar.addMenu("&File")
        fileMenu.addAction(saveAction)
        fileMenu.addAction(loadAction)
        fileMenu.addAction(inputAction)
        fileMenu.addAction(outputAction)
        fileMenu.addAction(inoutAction)

        # Under Generate menu, Generate Block action is used to compile code and generate block
        generateBlockAction = QAction("&Generate Block...", self)
        generateBlockAction.triggered.connect(self.generate_block)

        # Under Generate menu, Generate Code action is used to compile block and generate code
        generateCodeAction = QAction("&Generate Code...", self)
        generateCodeAction.triggered.connect(self.generate_code)

        generateMenu = menubar.addMenu("&Generate")
        generateMenu.addAction(generateBlockAction)
        generateMenu.addAction(generateCodeAction)

        appLayout = QHBoxLayout()
        appLayout.setContentsMargins(10, 0, 10, 10)

        appLayout.addLayout(tabLayout, 10)
        mainLayout.addLayout(appLayout, 1)
        self.setLayout(mainLayout)

    def save(self):
        pass

    def load(self):
        pass

    def draw_block(self):
        pass

    def draw_input(self):
        tempClass = InputPort()
        tempClass.points = [self.canvas.rectangle_begin + QtCore.QPoint(int(-self.canvas.Tri_In_H), int(self.canvas.Tri_In_F * tempClass.order)),
                    self.canvas.rectangle_begin + QtCore.QPoint(0, int(self.canvas.Tri_In_F / 2 + self.canvas.Tri_In_F * tempClass.order)),
                    self.canvas.rectangle_begin + QtCore.QPoint(int(-self.canvas.Tri_In_H), int(self.canvas.Tri_In_F + self.canvas.Tri_In_F * tempClass.order))]
        tempClass.set_polygon()
        tempClass.order = self.in_order
        self.in_order = self.in_order + 1

    def draw_output(self):
        tempClass = OutputPort()
        tempClass.points = [self.canvas.rectangle_end + QtCore.QPoint(self.canvas.Tri_In_H, int(-self.canvas.Tri_In_F / 2 - self.canvas.Tri_In_F * tempClass.order)),
                    self.canvas.rectangle_end + QtCore.QPoint(0, int(-self.canvas.Tri_In_F - self.canvas.Tri_In_F * tempClass.order)),
                    self.canvas.rectangle_end + QtCore.QPoint(0, int(- self.canvas.Tri_In_F * tempClass.order))]
        tempClass.set_polygon()
        tempClass.order = self.out_order
        self.out_order = self.out_order + 1

    def draw_inout(self):
        pass

    def generate_block(self):
        mytext = self.textEdit.toPlainText()
        lines = mytext.splitlines()
        text_input = []
        text_output = []
        text_center = ''
        for line in lines:
            x = [s.strip() for s in line.split(' ')]
            if 'module' in x:
                text_center = x[1]
            if 'input' in x:
                text_input.append(x[1])
                self.draw_input()
            if 'output' in x:
                text_output.append(x[1])
                self.draw_output()

        self.canvas.center_text = text_center

    def generate_code(self):
        pass

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    w = MainWindow()
    w.show()

    sys.exit(app.exec_())
