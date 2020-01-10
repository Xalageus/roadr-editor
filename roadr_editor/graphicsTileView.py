from PyQt5.QtWidgets import *
from PyQt5 import QtGui, QtCore

class GraphicsTileView(QGraphicsView):
    def __init__(self, parent):
        super(GraphicsTileView, self).__init__(parent)

    def mouseMoveEvent(self, event):
        print(event.pos())