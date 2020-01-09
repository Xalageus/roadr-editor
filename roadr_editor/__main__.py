import sys
#from PySide2.QtWidgets import *
from PyQt5.QtWidgets import *
from roadr_editor.mainController import mainController

app = QApplication([])
form = mainController()
form.show()
sys.exit(app.exec_())