from PyQt5.QtWidgets import (
    QMainWindow, QWidget, QLabel, QPushButton,
    QVBoxLayout, QHBoxLayout, QFrame
)
from PyQt5.QtCore import Qt, QTimer, pyqtSignal
from PyQt5.QtGui import QFont, QPixmap, QImage
import cv2
import numpy as np
from core.face_detector import FaceDetector
from core.phone_detector import PhoneDetector
from ui.blur_overlay import BlurOverlay
from ui.alert_popup import AlertPopup

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Screen Sentry")
        self.setMinimumSize(900, 600)

        # State
        self.monitoring_active = False
        self.blur_overlay = None
        self.popup_shown = False
        self.user_dismissed = False

        # Detectors
        self.face_detector = FaceDetector()
        self.phone_detector = PhoneDetector()

        # Webcam
        self.cap = cv2.VideoCapture(0)

        # Timer for frame processing
        self.timer = QTimer()
        self.timer.timeout.connect(self.process_frame)

        self.init_ui()

    def init_ui(self):
        central = QWidget()
        self.setCentralWidget(central)
        main_layout = QHBoxLayout(central)
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(20)

        # ── LEFT: Webcam Feed ──
        left_panel = QVBoxLayout()
        cam_label_title = QLabel("📷 Live Webcam Feed")
        cam_label_title.setFont(QFont("Arial", 12, QFont.Bold))

        self.cam_label = QLabel()
        self.cam_label.setFixedSize(540, 400)
        self.cam_label.setStyleSheet("background: #111; border: 2px solid #333; border-radius: 8px;")
        self.cam_label.setAlignment(Qt.AlignCenter)
        self.cam_label.setText("Webcam Inactive")

        left_panel.addWidget(cam_label_title)
        left_panel.addWidget(self.cam_label)
        left_panel.addStretch()

        # ── RIGHT: Controls ──
        right_panel = QVBoxLayout()
        right_panel.setSpacing(16)

        title = QLabel("🛡️ Screen Sentry")
        title.setFont(QFont("Arial", 20, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)

        subtitle = QLabel("Real-time Privacy Protection")
        subtitle.setAlignment(Qt.AlignCenter)
        subtitle.setStyleSheet("color: gray; font-size: 13px;")

        # Status
        self.status_label = QLabel("● INACTIVE")
        self.status_label.setFont(QFont("Arial", 14, QFont.Bold))
        self.status_label.setStyleSheet("color: gray;")
        self.status_label.setAlignment(Qt.AlignCenter)

        # Toggle Button
        self.toggle_btn = QPushButton("▶  START PROTECTION")
        self.toggle_btn.setFixedHeight(50)
        self.toggle_btn.setFont(QFont("Arial", 12, QFont.Bold))
        self.toggle_btn.setStyleSheet("""
            QPushButton {
                background: #27ae60; color: white;
                border-radius: 10px; padding: 10px;
            }
            QPushButton:hover { background: #2ecc71; }
        """)
        self.toggle_btn.clicked.connect(self.toggle_monitoring)

        # Threat indicators
        sep = QFrame()
        sep.setFrameShape(QFrame.HLine)
        sep.setStyleSheet("color: #ddd;")

        threats_title = QLabel("Detection Status")
        threats_title.setFont(QFont("Arial", 11, QFont.Bold))

        self.face_indicator = self.make_indicator("👤 Multiple Faces", "gray")
        self.phone_indicator = self.make_indicator("📱 Phone Detected", "gray")
        self.risk_indicator  = self.make_indicator("🚨 Privacy Risk", "gray")

        right_panel.addWidget(title)
        right_panel.addWidget(subtitle)
        right_panel.addSpacing(10)
        right_panel.addWidget(self.status_label)
        right_panel.addWidget(self.toggle_btn)
        right_panel.addSpacing(10)
        right_panel.addWidget(sep)
        right_panel.addWidget(threats_title)
        right_panel.addWidget(self.face_indicator)
        right_panel.addWidget(self.phone_indicator)
        right_panel.addWidget(self.risk_indicator)
        right_panel.addStretch()

        main_layout.addLayout(left_panel, 3)
        main_layout.addLayout(right_panel, 2)

    def make_indicator(self, text, color):
        lbl = QLabel(f"  {text}")
        lbl.setFixedHeight(36)
        lbl.setStyleSheet(f"""
            background: #f0f0f0; border-radius: 8px;
            font-size: 13px; font-weight: bold; color: {color};
            padding-left: 10px;
        """)
        return lbl

    def set_indicator(self, label, active):
        color = "#c0392b" if active else "#888"
        bg = "#fdecea" if active else "#f0f0f0"
        label.setStyleSheet(f"""
            background: {bg}; border-radius: 8px;
            font-size: 13px; font-weight: bold; color: {color};
            padding-left: 10px;
        """)

    def toggle_monitoring(self):
        if not self.monitoring_active:
            self.monitoring_active = True
            self.timer.start(30)  # ~30fps
            self.toggle_btn.setText("⏹  STOP PROTECTION")
            self.toggle_btn.setStyleSheet("""
                QPushButton { background: #c0392b; color: white; border-radius: 10px; padding: 10px; }
                QPushButton:hover { background: #e74c3c; }
            """)
            self.status_label.setText("● ACTIVE")
            self.status_label.setStyleSheet("color: #27ae60; font-size: 14px; font-weight: bold;")
        else:
            self.stop_monitoring()

    def stop_monitoring(self):
        self.monitoring_active = False
        self.timer.stop()
        self.toggle_btn.setText("▶  START PROTECTION")
        self.toggle_btn.setStyleSheet("""
            QPushButton { background: #27ae60; color: white; border-radius: 10px; padding: 10px; }
            QPushButton:hover { background: #2ecc71; }
        """)
        self.status_label.setText("● INACTIVE")
        self.status_label.setStyleSheet("color: gray; font-size: 14px; font-weight: bold;")
        self.cam_label.setText("Webcam Inactive")
        self.cam_label.setStyleSheet("background: #111; border: 2px solid #333; border-radius: 8px; color: white;")
        self.remove_blur()
        self.set_indicator(self.face_indicator, False)
        self.set_indicator(self.phone_indicator, False)
        self.set_indicator(self.risk_indicator, False)

    def process_frame(self):
        ret, frame = self.cap.read()
        if not ret:
            return

        frame = cv2.resize(frame, (540, 400))

        # Run detectors
        frame, face_count = self.face_detector.detect(frame)
        frame, phone_detected = self.phone_detector.detect(frame)

        multiple_faces = face_count > 1
        privacy_risk = multiple_faces or phone_detected

        # Update indicators
        self.set_indicator(self.face_indicator, multiple_faces)
        self.set_indicator(self.phone_indicator, phone_detected)
        self.set_indicator(self.risk_indicator, privacy_risk)

        # Handle blur/popup
        if privacy_risk and not self.user_dismissed:
            if self.blur_overlay is None:
                self.show_blur()
            if not self.popup_shown:
                self.popup_shown = True
                threat_msg = []
                if multiple_faces: threat_msg.append("Multiple faces detected")
                if phone_detected: threat_msg.append("Phone detected near screen")
                self.show_alert(", ".join(threat_msg))
        elif not privacy_risk:
            self.user_dismissed = False
            self.popup_shown = False
            self.remove_blur()

        # Display frame in UI
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb.shape
        qt_img = QImage(rgb.data, w, h, ch * w, QImage.Format_RGB888)
        self.cam_label.setPixmap(QPixmap.fromImage(qt_img))

    def show_blur(self):
        self.blur_overlay = BlurOverlay()
        self.blur_overlay.show()

    def remove_blur(self):
        if self.blur_overlay:
            self.blur_overlay.close()
            self.blur_overlay = None

    def show_alert(self, threat_type):
        popup = AlertPopup(threat_type)
        popup.exec_()
        if popup.result_action == "dismiss":
            self.user_dismissed = True
            self.remove_blur()
        # if "keep" — blur stays

    def closeEvent(self, event):
        self.cap.release()
        self.remove_blur()
        event.accept()