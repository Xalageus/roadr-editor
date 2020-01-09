#from PySide2.QtWidgets import *
from PyQt5.QtWidgets import *
import pygame
from roadr_editor.main import Ui_MainWindow

class mainController(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super(mainController, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        pygame.init()

        self.ui.pgWidget.init(pygame.Surface(self.ui.pgWidget.getSize()), pygame.display)