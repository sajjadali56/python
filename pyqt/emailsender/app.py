from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

from ui.main import Ui_MainWindow

class EmailSender(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(EmailSender, self).__init__()
        self.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = EmailSender()
    ui.show()
    app.exec_() 