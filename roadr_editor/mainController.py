from PyQt5.QtWidgets import *
from PyQt5 import QtGui, QtCore
from roadr_editor.main import Ui_MainWindow
from roadr_editor.settingsController import settingsController
from roadr_editor.settingssys import settings_system
import roadr_editor.strings as printStrings
from roadr_editor.assets import asset_system

class mainController(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super(mainController, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.graphicsView.setUiParent(self)
        self.tabifyDockWidget(self.ui.tilesWidget, self.ui.collWidget)
        self.modeGroup = QActionGroup(self)
        self.modeGroup.addAction(self.ui.actionSelection_Mode)
        self.modeGroup.addAction(self.ui.actionPlace_Mode)
        self.ui.actionPlace_Mode.setChecked(True)
        self.ui.tilesWidget.raise_()

        self.assets = None
        self.settingsSYS = settings_system()
        if self.settingsSYS.noSettings:
            self.ui.statusbar.showMessage(printStrings.NOT_CONFIGURED)
        else:
            self.readSettings()
        
        self.scene = QGraphicsScene(self)
        self.ui.graphicsView.setScene(self.scene)
        self.scene.addText("Hello!")
        self.scene.addRect(QtCore.QRectF(0, 0, 30, 20), pen=QtGui.QPen(), brush=QtGui.QBrush())

        self.ui.actionAbout_Qt.triggered.connect(lambda: self.openAboutQt())
        self.ui.actionSettings.triggered.connect(lambda: self.openSettings())
        self.ui.actionSelection_Mode.toggled.connect(lambda: self.selectionToggled(bool))
        self.ui.actionPlace_Mode.toggled.connect(lambda: self.placeToggled(bool))
        self.ui.actionQuit.triggered.connect(lambda: self.quit())

        self.resize(self.sizeHint())

    def openAboutQt(self):
        QMessageBox.aboutQt(self, printStrings.TITLE)

    def openSettings(self):
        self.settings = settingsController(self.settingsSYS, self)
        self.settings.show()

    def selectionToggled(self, toggle):
        print(toggle())

    def placeToggled(self, toggle):
        print(toggle())

    def quit(self):
        QApplication.quit()

    def graphicsMouseMoveEvent(self):
        if self.settingsSYS.noSettings == True:
            self.ui.statusbar.showMessage(printStrings.NOT_CONFIGURED)

    def readSettings(self):
        self.settingsSYS.parse()
        self.assets = asset_system(self.settingsSYS.assetPath)
        self.assets.parseDef()
        self.assets.trimAll()
        self.assets.mergePaths()
        self.loadAssets()

    def loadAssets(self):
        row = 0
        num = 0
        self.ui.tableWidget.insertRow(self.ui.tableWidget.rowCount())

        for tile in self.assets.tiles:
            if num == self.ui.tableWidget.columnCount():
                row += 1
                num = 0
                self.ui.tableWidget.insertRow(self.ui.tableWidget.rowCount())

            tileImage = QtGui.QImage(tile.filename)
            self.ui.tableWidget.setItem(row, num, QTableWidgetItem(QtGui.QIcon(QtGui.QPixmap().fromImage(tileImage)), tile.id))
            num += 1