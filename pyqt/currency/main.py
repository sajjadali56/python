from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import ui.mainDialog as mainDialog

import sys
import requests

class MainDialog(QDialog, mainDialog.Ui_Dialog):

    def __init__(self, parent=None):
        super(MainDialog, self).__init__(parent)
        self.setupUi(self)


if __name__ == "__main__":

    app = QApplication(sys.argv)
    form = MainDialog()
    form.show()
    app.exec_()