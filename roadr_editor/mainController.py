from PyQt5.QtWidgets import *
from PyQt5 import QtGui, QtCore
from roadr_editor.main import Ui_MainWindow

class mainController(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super(mainController, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.scene = QGraphicsScene(self)
        self.ui.graphicsView.setScene(self.scene)
        self.scene.addText("Hello!")
        self.scene.addRect(QtCore.QRectF(0, 0, 30, 20), pen=QtGui.QPen(), brush=QtGui.QBrush())

        self.ui.actionAbout_Qt.triggered.connect(lambda: self.openAboutQt())

    def openAboutQt(self):
        QMessageBox.aboutQt(self, "Road Runner Editor")