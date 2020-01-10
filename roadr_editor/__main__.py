import sys
from PyQt5.QtWidgets import *
from roadr_editor.mainController import mainController

def main():
    app = QApplication([])
    form = mainController()
    form.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()