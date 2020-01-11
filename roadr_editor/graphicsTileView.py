from PyQt5.QtWidgets import *
from PyQt5 import QtGui, QtCore

class GraphicsTileView(QGraphicsView):
    def __init__(self, parent):
        super(GraphicsTileView, self).__init__(parent)
        self.uiParent = None

    def setUiParent(self, parent):
        self.uiParent = parent

    def mouseMoveEvent(self, event):
        self.uiParent.graphicsMouseMoveEvent()
        print(event.pos())