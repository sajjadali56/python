from PyQt5.QtWidgets import QApplication, QProgressBar
from PyQt5.QtGui import QPainter, QLinearGradient
from PyQt5.QtCore import Qt, QRectF


class CustomProgressBar(QProgressBar):
    def paintEvent(self, event):
        painter = QPainter(self)
        rect = self.rect()
        gradient = QLinearGradient(rect.topLeft(), rect.topRight())

        # Set gradient colors dynamically
        gradient.setColorAt(0.0, Qt.red)
        gradient.setColorAt(0.5, Qt.yellow)
        gradient.setColorAt(1.0, Qt.green)

        painter.fillRect(rect, gradient)

        # Draw text
        progress_text = f"{self.value()}%"
        painter.setPen(Qt.black)
        painter.drawText(rect, Qt.AlignCenter, progress_text)


app = QApplication([])

progress_bar = CustomProgressBar()
progress_bar.setValue(70)
progress_bar.resize(300, 50)
progress_bar.show()

app.exec_()
