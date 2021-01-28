# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import QPolygon


class Canvas(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(30, 30, 600, 400)
        self.rectangle_begin = QtCore.QPoint(100,50)  # Module rectangle top left corner
        self.rectangle_end = QtCore.QPoint(400,250)    # Module rectangle bottom right corner
        self.center_text = ''                   # Module name in the center of rectangle
        self.show()

        self.Tri_In_H = 20
        self.Tri_In_F = 40

    # All canvas painting actions are handled here. This method run in a loop continuously
    def paintEvent(self, event):
        qp = QtGui.QPainter(self)
        br = QtGui.QBrush(QtGui.QColor(100, 10, 10, 40))
        qp.setBrush(br)
        qp.drawRect(QtCore.QRect(self.rectangle_begin, self.rectangle_end))         # Draw module rectangle
        qp.drawText((self.rectangle_begin+self.rectangle_end)/2, self.center_text)  # Write the name of module rectangle

        # Draw input ports and their names
        for i in Port:
            if i.port_type == 'input':
                i.points = [self.rectangle_begin + QtCore.QPoint(int(-self.Tri_In_H),  int(self.Tri_In_F * i.in_order)),
                            self.rectangle_begin + QtCore.QPoint(0, int(self.Tri_In_F/2 + self.Tri_In_F * i.in_order)),
                            self.rectangle_begin + QtCore.QPoint(int(-self.Tri_In_H), int(self.Tri_In_F + self.Tri_In_F * i.in_order))]
            elif i.port_type == 'output':
                i.points = [self.rectangle_end + QtCore.QPoint(self.Tri_In_H, int(-self.Tri_In_F / 2 - self.Tri_In_F * i.out_order)),
                            self.rectangle_end + QtCore.QPoint(0, int(-self.Tri_In_F - self.Tri_In_F * i.out_order)),
                            self.rectangle_end + QtCore.QPoint(0, int(- self.Tri_In_F * i.out_order))]
            elif i.port_type == 'inout':
                i.points = [self.rectangle_begin + QtCore.QPoint(int(-self.Tri_In_H), int(self.Tri_In_F * i.in_order)),
                            self.rectangle_begin + QtCore.QPoint(0, int(self.Tri_In_F / 2 + self.Tri_In_F * i.in_order)),
                            self.rectangle_begin + QtCore.QPoint(int(-self.Tri_In_H), int(self.Tri_In_F + self.Tri_In_F * i.in_order)),
                            self.rectangle_begin + QtCore.QPoint(int(-2 * self.Tri_In_H), int(self.Tri_In_F / 2 + self.Tri_In_F * i.in_order))]
            i.set_polygon()
            qp.drawPolygon(i.polygon)

    # When mouse is pressed, the top left corner of the rectangle being drawn is saved
    def mousePressEvent(self, event):
        self.rectangle_begin = event.pos()
        self.rectangle_end = event.pos()
        self.update()

    # When mouse is pressed and moving, the bottom right corner of the rectangle also changes and shown in screen
    def mouseMoveEvent(self, event):
        self.rectangle_end = event.pos()
        self.update()

    # After mouse has released, the bottom right corner of the rectangle is assigned and rectangle placed in screen
    def mouseReleaseEvent(self, event):
        self.rectangle_end = event.pos()
        self.update()


# Below two classes are to store all input port objects
class IterPort(type):
    def __iter__(cls):
        return iter(cls._allPorts)


class Port(metaclass=IterPort):
    _allPorts = []

    def __init__(self):
        self._allPorts.append(self)
        self.points = [QtCore.QPoint()]
        self.polygon = QPolygon(self.points)
        self.text = ''
        self.in_order = 0
        self.out_order = 0
        self.set_polygon()
        self.port_type = 'empty'

    def set_polygon(self):
        self.polygon = QPolygon(self.points)
