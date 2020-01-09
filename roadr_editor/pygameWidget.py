#from PySide2.QtWidgets import *
#from PySide2 import QtGui
from PyQt5.QtWidgets import *
from PyQt5 import QtGui
import pygame
import sys

class PygameWidget(QWidget):
    def __init__(self, parent=None):
        super(PygameWidget, self).__init__(parent)
        self.surface = None
        self.display = None

        self.w = None
        self.h = None
        self.image = None
        self.pix = None
        self.data = None
        self.scene = None
        self.view = None

    def getSize(self):
        return (self.width(), self.height())

    def update(self):
        data = self.surface.get_buffer().raw
        self.pix.detach()
        self.image = QtGui.QImage(data, self.w, self.h, QtGui.QImage.Format_RGB32)
        self.pix.fromImage(self.image)
        
    def init(self, surface, display):
        self.w = surface.get_width()
        self.h = surface.get_height()
        self.surface = surface
        self.display = display
        self.scene = QGraphicsScene(self)
        self.view = QGraphicsView(self.scene, self)
        data = self.surface.get_buffer().raw
        self.image = QtGui.QImage(data, self.w, self.h, QtGui.QImage.Format_RGB32)
        self.pix = QtGui.QPixmap(self.image)
        self.scene.addPixmap(self.pix)

    #def paintEvent(self, event):
        #qp = QtGui.QPainter()
        #qp.begin(self)
        #qp.drawImage(0, 0, self.image)
        #qp.end()

    def resizeEvent(self, event):
        size = self.getSize()
        self.display.set_mode(size=size)
        self.w = size[0]
        self.h = size[1]
        self.update()