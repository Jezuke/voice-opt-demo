from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt6.QtCore import QSize, Qt

import sys

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("MyApp")
        button = QPushButton("Press Me!")
        button.setCheckable(True)
        button.clicked.connect(self.button_clicked)
        button.clicked.connect(self.button_toggled)

        self.setMinimumSize(QSize(960,540))
        self.setCentralWidget(button)

    def button_clicked(self):
        print("Clicked")

    def button_toggled(self, checked):
        print("Checked?", checked)

app = QApplication(sys.argv)
window = MainWindow()
window.show() # Windows are hidden by default

app.exec()
