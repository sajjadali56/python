import os
from PyQt5.QtWidgets import QApplication, QProgressBar, QPushButton, QVBoxLayout, QWidget, QFileDialog
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
        self.start_button = QPushButton("Start Reading File", self)
        self.start_button.clicked.connect(self.start_progress)
        layout.addWidget(self.start_button)

        # Set layout
        self.setLayout(layout)

        # Timer to increment progress
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_progress)

        # Variables for file reading
        self.file_path = None
        self.file_size = 0
        self.bytes_read = 0

    def start_progress(self):
        # Open a file dialog to select a file
        self.file_path, _ = QFileDialog.getOpenFileName(
            self, "Select a file to read")
        if self.file_path:
            # Get the file size
            self.file_size = os.path.getsize(self.file_path)
            self.bytes_read = 0  # Reset bytes read
            self.progress_bar.setMaximum(100)
            self.progress_bar.setValue(0)
            self.timer.start(100)  # Timer triggers every 100 ms

            # Start reading the file in the background
            self.read_file_in_chunks()

    def read_file_in_chunks(self):
        chunk_size = 1024  # Read in 1 KB chunks
        with open(self.file_path, 'rb') as file:
            while (chunk := file.read(chunk_size)):
                self.bytes_read += len(chunk)
                progress = (self.bytes_read / self.file_size) * 100
                self.progress_bar.setValue(int(progress))
                QApplication.processEvents()  # Process events to update the GUI

            self.timer.stop()  # Stop timer when reading is complete

    def update_progress(self):
        # This method can be used to update the progress if needed
        pass


if __name__ == "__main__":
    app = QApplication([])

    # Create the main application window
    window = ColorfulProgressBar()
    window.show()

    app.exec_()
