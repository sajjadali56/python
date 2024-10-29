from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.uic import loadUi

import sys

from ui.main import Ui_MainWindow

class Main(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(Main, self).__init__()
        # loadUi("ui/main.ui", self)
        self.setupUi(self)

        self.actionNew.triggered.connect(self.newFile)
        self.actionSave.triggered.connect(self.saveFile)
        self.actionSave_As.triggered.connect(self.saveFileAs)
        self.actionOpen.triggered.connect(self.openFile)
        self.actionSet_Dark_Mode.triggered.connect(self.setDarkMode)
        self.actionSet_Light_Mode.triggered.connect(self.setLightMode)
        self.actionIncrease_Font_Size.triggered.connect(self.incFontSize)
        self.actionDecrease_Font_Size.triggered.connect(self.decFontSize)

        self.actionClose.triggered.connect(lambda : self.close())

        self.actionUndo.triggered.connect(lambda: self.textEdit.undo())
        self.actionRedo.triggered.connect(lambda: self.textEdit.redo())
        self.actionCut.triggered.connect(lambda: self.textEdit.cut())
        self.actionCopy.triggered.connect(lambda: self.textEdit.copy())
        self.actionPaste.triggered.connect(lambda: self.textEdit.paste())

    def newFile(self):
        print("new file")
    
    def saveFile(self):
        ""

    def saveFileAs(self):
        ""
    
    def openFile(self):
        ""
            
    def setDarkMode(self):
        ""

    def setLightMode(self):
        ""
    
    def incFontSize(self):
        ""
    
    def decFontSize(self):
        ""


    
if __name__ == "__main__":

    app = QApplication(sys.argv)
    ui = Main()
    ui.show()
    app.exec_()