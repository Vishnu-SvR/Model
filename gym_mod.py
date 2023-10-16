pip install streamlit
pip install stramlit opencv-python
pip install streamlit cvzone
pip install streamlit ultralytics

import cv2
import math
import matplotlib.pyplot as plt
import cvzone
from ultralytics import YOLO

cls_names= ['BenchPress', 'DeadLift', 'Gym-Exercies', 'Jalon', 'ShoulderPress', 'Squat']

model = YOLO('best_all.pt')

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

while True:
    ret, frame = cap.read()
    results = model(frame, stream=True)
    for r in results:
        boxes = r.boxes
        for box in boxes:
            x1,y1,x2,y2 = box.xyxy[0]
            x1,y1,x2,y2 = int(x1), int(y1), int(x2), int(y2)
            print(x1,y1,x2,y2)
            cv2.rectangle(frame, (x1,y1),(x2,y2),(255,0,0),2)
            conf = math.ceil((box.conf[0]*100))/100
            print(conf)
            cls = int(box.cls[0])
            cvzone.putTextRect(frame, f'{cls_names[cls]} {conf}',(x1,y1), thickness=2,colorT=(0,0,0),colorR=(255,255,255),offset=5, scale=2)
    cv2.imshow('Yolo', frame)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
