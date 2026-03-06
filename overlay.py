from PyQt5.QtWidgets import QMainWindow, QLabel
from PyQt5.QtCore import Qt

class Overlay(QMainWindow):
    def __init__(self, screensize):
        super().__init__()
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setWindowFlag(Qt.WindowStaysOnTopHint)

        self.setWindowTitle("Cowboy overlay")
        self.screenWidth = screensize.width()
        self.screenHeight = screensize.height()
        self.setGeometry(0,0,self.screenWidth ,self.screenHeight)

        self.initUI()
    
    def initUI(self):
        self.wheat = QLabel(self)
        self.wheat.setGeometry(self.screenWidth//2, self.screenHeight - 380, 556, 420)
        self.wheat.setStyleSheet("border-image: url(wheat.png);")

        self.hat = QLabel(self)
        self.hat.setGeometry(0, 0, self.screenWidth, 250)
        self.hat.setStyleSheet("border-image: url(hat.png);")