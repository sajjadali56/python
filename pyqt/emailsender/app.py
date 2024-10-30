from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

from ui.main import Ui_MainWindow

class Main(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(Main, self).__init__()
        self.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = Main()
    ui.show()
    app.exec_()