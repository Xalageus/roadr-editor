from PyQt5.QtWidgets import *
from PyQt5 import QtGui, QtCore
from roadr_editor.settings import Ui_Settings
from roadr_editor.assets import asset_system

class settingsController(Ui_Settings, QDialog):
    def __init__(self):
        super(settingsController, self).__init__()
        self.ui = Ui_Settings()
        self.ui.setupUi(self)

        self.ui.checkLabel.setVisible(False)

    def chooseFolder(self):
        assetFolder = str(QFileDialog.getExistingDirectory(self, "Select Asset folder"))
        if assetFolder is not None:
            self.ui.checkLabel.setText("Checking...")
            self.ui.assetLine.setText(assetFolder)
            self.ui.checkLabel.setVisible(True)

            assetSYS = asset_system(assetFolder)
            if assetSYS.checkFolder():
                self.ui.checkLabel.setText("Asset folder is valid")
            else:
                self.ui.checkLabel.setText("Asset folder is invalid")