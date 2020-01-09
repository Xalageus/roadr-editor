import sys
import os
#from PySide2.QtWidgets import *
from PyQt5.QtWidgets import *
from roadr_editor.mainController import mainController

os.environ["SDL_VIDEODRIVER"] = "windib"
app = QApplication([])
form = mainController()
form.show()
sys.exit(app.exec_())