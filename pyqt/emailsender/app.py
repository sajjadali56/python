from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
import sys

from ui.main import Ui_MainWindow
from email_sender import send_email

class EmailSender(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(EmailSender, self).__init__()
        self.setupUi(self)
    
        self.pushButtonSend.clicked.connect(self.sendEmail)

    def sendEmail(self):

        recipient = self.lineEditRec.text().strip()
        subject = self.lineEditSub.text().strip()
        body = self.textEditEmail.toPlainText().strip()

        if recipient:
            send_email(recipient, subject, body)
        else:
            message = QMessageBox()
            message.setWindowTitle("Error!")
            message.setText("Please write the recipient address...")
            message.setIcon(QMessageBox.Icon.Critical)
            message.exec_()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = EmailSender()
    ui.show()
    app.exec_()