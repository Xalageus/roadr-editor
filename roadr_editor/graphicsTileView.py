from PyQt5.QtWidgets import *
from PyQt5 import QtGui, QtCore

class GraphicsTileView(QGraphicsView):
    def __init__(self, parent):
        super(GraphicsTileView, self).__init__(parent)
        self.uiParent = None

        scene = GraphicsTileScene(self)
        self.setScene(scene)
        scene.addText("Hello!")
        scene.addRect(QtCore.QRectF(0, 0, 30, 20), pen=QtGui.QPen(), brush=QtGui.QBrush())

    def setUiParent(self, parent):
        self.uiParent = parent

    def mouseMoveEvent(self, event):
        self.uiParent.graphicsMouseMoveEvent()
        print(event.pos())

    def addRow(self):
        rect = self.sceneRect()
        rect.adjust(0, -40, 0, 0)
        self.setSceneRect(rect)

class GraphicsTileScene(QGraphicsScene):
    def __init__(self, parent):
        super(GraphicsTileScene, self).__init__(parent)

    def mouseMoveEvent(cls, self, QGraphicsSceneMouseEvent):
        print(QGraphicsSceneMouseEvent.pos())
        return super().mouseMoveEvent(self, QGraphicsSceneMouseEvent)