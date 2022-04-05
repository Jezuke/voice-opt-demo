from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
from PyQt6.QtCore import QSize, Qt
from pygame import mixer

import sys

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("MyApp")

        layout = QVBoxLayout()
        
        button = QPushButton("Pussy Popper!")
        button.clicked.connect(self.button_clicked)
        button.clicked.connect(self.button_toggled)
        button.setCheckable(True)

        button2 = QPushButton("Whatup Bitch?")
        button2.clicked.connect(self.button2_clicked)
        button2.clicked.connect(self.button2_toggled)
        button2.setCheckable(True)

        layout.addWidget(button)
        layout.addWidget(button2)

        container = QWidget()
        container.setLayout(layout)

        self.setMinimumSize(QSize(960,540))
        self.setCentralWidget(container)

    def button_clicked(self):
        mixer.music.load('../audio/ayo.mp3')
        mixer.music.play()
        print("Clicked")

    def button_toggled(self, checked):
        print("Checked?", checked)

    def button2_clicked(self):
        mixer.music.load('../audio/bitch.mp3')
        mixer.music.play()
        print("Clicked")

    def button2_toggled(self, checked):
        print("Checked?", checked)

mixer.init()
app = QApplication(sys.argv)
window = MainWindow()
window.show() # Windows are hidden by default

app.exec()