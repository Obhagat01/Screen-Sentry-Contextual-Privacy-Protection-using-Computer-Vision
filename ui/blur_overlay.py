from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt
import numpy as np
import cv2
from core.screen_blur import get_blurred_screen

class BlurOverlay(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(
            Qt.FramelessWindowHint |
            Qt.WindowStaysOnTopHint |
            Qt.Tool
        )
        self.setAttribute(Qt.WA_TranslucentBackground, False)
        self.showFullScreen()

        self.label = QLabel(self)
        self.label.setAlignment(Qt.AlignCenter)
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.label)
        self.setLayout(layout)
        self.update_blur()

    def update_blur(self):
        img = get_blurred_screen()
        h, w, ch = img.shape
        qt_img = QImage(img.data, w, h, ch * w, QImage.Format_BGR888)
        self.label.setPixmap(QPixmap.fromImage(qt_img).scaled(
            self.size(), Qt.KeepAspectRatioByExpanding
        ))