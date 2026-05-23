from ultralytics import YOLO
import os

class PhoneDetector:
    def __init__(self):
        base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        model_path = os.path.join(base, "models", "yolov8n.pt")
        self.model = YOLO(model_path)

    def detect(self, frame):
        results = self.model(frame, conf=0.4, verbose=False)
        phone_detected = False
        for r in results:
            for box in r.boxes:
                cls = int(box.cls[0])
                label = self.model.names[cls]
                if label == "cell phone":
                    phone_detected = True
        annotated = results[0].plot()
        return annotated, phone_detected