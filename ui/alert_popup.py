from PyQt5.QtWidgets import QDialog, QLabel, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt

class AlertPopup(QDialog):
    def __init__(self, threat_type="Unknown"):
        super().__init__()
        self.setWindowTitle("⚠️ Screen Sentry Alert")
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.Dialog)
        self.setMinimumWidth(400)
        self.result_action = None  # "keep" or "dismiss"

        layout = QVBoxLayout()

        title = QLabel(f"🚨 Privacy Threat Detected!")
        title.setStyleSheet("font-size: 16px; font-weight: bold; color: red;")
        title.setAlignment(Qt.AlignCenter)

        detail = QLabel(f"Threat: {threat_type}\nScreen is currently blurred for protection.")
        detail.setAlignment(Qt.AlignCenter)
        detail.setWordWrap(True)

        btn_layout = QHBoxLayout()

        keep_btn = QPushButton("🔒 Keep Blurred")
        keep_btn.setStyleSheet("background: #c0392b; color: white; padding: 8px 16px; font-size: 13px;")
        keep_btn.clicked.connect(self.keep_blur)

        dismiss_btn = QPushButton("✅ I'm Safe — Remove Blur")
        dismiss_btn.setStyleSheet("background: #27ae60; color: white; padding: 8px 16px; font-size: 13px;")
        dismiss_btn.clicked.connect(self.dismiss_blur)

        btn_layout.addWidget(keep_btn)
        btn_layout.addWidget(dismiss_btn)

        layout.addWidget(title)
        layout.addSpacing(10)
        layout.addWidget(detail)
        layout.addSpacing(20)
        layout.addLayout(btn_layout)
        self.setLayout(layout)

    def keep_blur(self):
        self.result_action = "keep"
        self.accept()

    def dismiss_blur(self):
        self.result_action = "dismiss"
        self.accept()