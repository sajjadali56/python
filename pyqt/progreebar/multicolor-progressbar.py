from PyQt5.QtWidgets import QApplication, QProgressBar, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QPainter, QColor, QBrush, QLinearGradient


class MultiColorProgressBar(QProgressBar):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setTextVisible(False)  # Disable default text display

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # Get the current progress bar geometry
        rect = self.rect()
        progress_width = int(rect.width() * self.value() / self.maximum())

        # Define colors for different segments
        segment_colors = [
            QColor("red"),
            QColor("green"),
            QColor("yellow"),
            QColor("blue"),
        ]

        # Create a gradient to fill the progress bar smoothly
        gradient = QLinearGradient(0, 0, rect.width(), 0)
        for i, color in enumerate(segment_colors):
            # Calculate the position for each color
            position = i / (len(segment_colors) - 1)
            gradient.setColorAt(position, color)

        # Fill the progress bar with the gradient
        painter.fillRect(rect, QBrush(gradient))

        # Clip the painting to the current progress
        painter.setClipRect(0, 0, progress_width, rect.height())
        painter.fillRect(0, 0, progress_width, rect.height(), QBrush(gradient))

        painter.end()


class ProgressWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Multi-Color Progress Bar")
        self.setGeometry(300, 300, 400, 200)  # Set window size

        layout = QVBoxLayout()

        # Create progress bar
        self.progress_bar = MultiColorProgressBar(self)
        self.progress_bar.setMaximum(100)
        self.progress_bar.setValue(0)
        layout.addWidget(self.progress_bar)

        # Create start button
        self.start_button = QPushButton("Start Progress", self)
        self.start_button.clicked.connect(self.start_progress)
        layout.addWidget(self.start_button)

        self.setLayout(layout)

        # Timer to update progress
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_progress)

        self.current_progress = 0

    def start_progress(self):
        if not self.timer.isActive():
            self.current_progress = 0
            self.progress_bar.setValue(self.current_progress)
            self.timer.start(100)  # Update every 100 ms

    def update_progress(self):
        if self.current_progress < 100:
            self.current_progress += 1
            self.progress_bar.setValue(self.current_progress)
        else:
            self.timer.stop()  # Stop the timer when progress reaches 100%


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)

    # Create and show the main window
    window = ProgressWindow()
    window.show()

    # Run the application's event loop
    sys.exit(app.exec_())
