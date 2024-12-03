from PyQt5.QtWidgets import QApplication, QProgressBar, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtCore import QTimer


class ColorfulProgressBar(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # Set a fixed size for the main window
        self.setWindowTitle("Colorful Progress Bar")
        self.setGeometry(300, 300, 400, 200)  # x, y, width, height

        # Create layout
        layout = QVBoxLayout(self)

        # Create a progress bar
        self.progress_bar = QProgressBar(self)
        self.progress_bar.setValue(0)  # Start progress at 0%
        self.progress_bar.setStyleSheet("""
            QProgressBar {
                border: 2px solid #555;
                border-radius: 5px;
                text-align: center;
                height: 30px; /* Ensure proper sizing */
            }
            QProgressBar::chunk {
                background: qlineargradient(
                    x1: 0, y1: 0, x2: 1, y2: 0,
                    stop: 0 red,
                    stop: 0.5 yellow,
                    stop: 1 green
                );
            }
        """)
        layout.addWidget(self.progress_bar)

        # Create a button to start progress
        self.start_button = QPushButton("Start Progress", self)
        self.start_button.clicked.connect(self.start_progress)
        layout.addWidget(self.start_button)

        # Set layout
        self.setLayout(layout)

        # Timer to increment progress
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_progress)

        # Current progress
        self.current_progress = 0

    def start_progress(self):
        self.current_progress = 0
        self.progress_bar.setValue(self.current_progress)
        self.timer.start(100)  # Timer triggers every 100 ms

    def update_progress(self):
        if self.current_progress < 100:
            self.current_progress += 1
            self.progress_bar.setValue(self.current_progress)
        else:
            self.timer.stop()  # Stop timer when progress reaches 100%


if __name__ == "__main__":
    app = QApplication([])

    # Create the main application window
    window = ColorfulProgressBar()
    window.show()

    app.exec_()
