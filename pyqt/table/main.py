from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem, QHeaderView

import sys

def get_styles() -> str:
    with open("style.css", "r") as f:
        styles = f.read()
    return styles

class Main(QWidget):
    def __init__(self):
        super(Main, self).__init__()
        self.setWindowTitle("Load Excel Data")

        layout = QVBoxLayout(self)
        self.setLayout(layout)

        self.table_widget = QTableWidget()
        layout.addWidget(self.table_widget)

        # Adjust each column width to fit content
        self.table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)

        self.load_data()
    
    def load_data(self):
        path = "MOCK_DATA.csv"
        with open(path, "r") as file:
            data = file.read().split("\n")
        headers = data[0].split(",")
        headers.remove("id")
        list_values = [val.split(",")[1:] for val in data[1:]]

        self.table_widget.setRowCount(len(data))
        self.table_widget.setColumnCount(len(headers))

        self.table_widget.setHorizontalHeaderLabels(headers)
        
        for i in range(len(list_values)):
            value = list_values[i]
            for j in range(len(value)):
                item = QTableWidgetItem(value[j])
                self.table_widget.setItem(i, j, item)   

        self.setStyleSheet(get_styles())
         

    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main()
    window.showMaximized()
    app.exec_()