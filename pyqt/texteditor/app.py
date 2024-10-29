from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt5.uic import loadUi

import sys

from ui.main import Ui_MainWindow
from service import *

filter = "Text Files(*.txt);; Python Files(*.py)"

class Main(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(Main, self).__init__()
        # loadUi("ui/main.ui", self)
        self.setupUi(self)

        self.textEdit.setTabStopWidth(16)

        self.currentPath = None

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
        self.textEdit.clear()
        self.setWindowTitle("Untitled")
        self.currentPath = None
    
    def saveFile(self):
        if self.currentPath:
            write(self.currentPath, self.textEdit.toPlainText())
        else:
            self.saveFileAs()

    def saveFileAs(self):
        filename = QFileDialog.getSaveFileName(self, "Save File", ".", filter)[0]
        if filename:
            print(f)
            self.currentPath = filename
            self.setWindowTitle(filename)
            write(self.currentPath, self.textEdit.toPlainText())
    
    def openFile(self):
        filename = QFileDialog.getOpenFileName(self, "Open File", ".", filter)[0]
        if not filename:
            return
        
        self.currentPath = filename
        self.setWindowTitle(filename)
        text = read(filename)
        self.textEdit.setText(text)

        
            
    def setDarkMode(self):
        self.setStyleSheet("""
        QWidget{
            background-color: rgb(33,33,33);
            color: #FFFFFF;
        }
        QTextEdit{
            background-color: rgb(46,46,46);
        }
        QMenuBar::item:selected{
            color: #FFF
        } 
        """)

    def setLightMode(self):
        self.setStyleSheet("")

    
    def incFontSize(self):
        ""
    
    def decFontSize(self):
        ""


    
if __name__ == "__main__":

    app = QApplication(sys.argv)
    ui = Main()
    ui.show()
    app.exec_()