from PyQt5.QtWidgets import *
from PyQt5 import QtGui, QtCore

class GraphicsTileView(QGraphicsView):
    def __init__(self, parent):
        super(GraphicsTileView, self).__init__(parent)
        self.uiParent = None
        self.gScene = GraphicsTileScene(self)

        self.setScene(self.gScene)

    def setUiParent(self, parent):
        self.uiParent = parent

    def mouseMoveEvent(self, event):
        self.uiParent.graphicsMouseMoveEvent()
        print(event.pos())

    def addRow(self):
        rect = self.sceneRect()
        rect.adjust(0, -self.gScene.height, 0, 0)
        self.setSceneRect(rect)
        self.gScene.addRow()

class GraphicsTileScene(QGraphicsScene):
    def __init__(self, parent):
        super(GraphicsTileScene, self).__init__(parent)
        self.width = 36
        self.height = 32
        self.rowCount = 0

        i = 0
        while i < (self.height / 2):
            self.addRow()
            i += 1

    def addRow(self):
        self.drawGrid((-self.height) * self.rowCount)
        self.rowCount += 1

    def drawGrid(self, col):
        i = 0
        while i < 10:
            self.addRect(QtCore.QRectF(i * self.width, col, self.width, self.height), pen=QtGui.QPen(), brush=QtGui.QBrush())
            i += 1