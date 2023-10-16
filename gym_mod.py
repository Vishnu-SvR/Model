# import streamlit as st
# import cv2
# import math
# import cvzone
# from ultralytics import YOLO

# cls_names = ['BenchPress', 'DeadLift', 'Gym-Exercies', 'Jalon', 'ShoulderPress', 'Squat']

# # Load YOLO model
# model = YOLO('best_all.pt')

# # Function to detect objects and draw bounding boxes
# def detect_objects(frame):
#     results = model(frame, stream=True)
#     for r in results:
#         boxes = r.boxes
#         for box in boxes:
#             x1, y1, x2, y2 = box.xyxy[0]
#             x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
#             cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)
#             conf = math.ceil((box.conf[0] * 100)) / 100
#             cls = int(box.cls[0])
#             cvzone.putTextRect(frame, f'{cls_names[cls]} {conf}', (x1, y1),
#                                thickness=2, colorT=(0, 0, 0), colorR=(255, 255, 255), offset=5, scale=2)

#     return frame

# def main():
#     st.title("YOLO Object Detection in Streamlit")
#     cap = cv2.VideoCapture(0)
#     cap.set(3, 640)
#     cap.set(4, 480)

#     # Create a placeholder to display the video stream
#     video_placeholder = st.empty()

#     while True:
#         ret, frame = cap.read()
#         if not ret:
#             st.error("Error: Could not read frame.")
#             break

#         # Perform object detection and update the frame
#         frame_with_objects = detect_objects(frame)

#         # Display the frame in Streamlit
#         video_placeholder.image(frame_with_objects, channels="BGR", use_column_width=True)

#         # Check for user input to stop the stream
#         if st.button("Stop Stream"):
#             break

#     # Release the camera when the app is closed
#     cap.release()

# if __name__ == "__main__":
#     main()

apt-get update && apt-get install -y python3-opencv
import streamlit as st
import cv2

def main():
    st.set_page_config(page_title="Streamlit WebCam App")
    st.title("Webcam Display Steamlit App")
    st.caption("Powered by OpenCV, Streamlit")
    cap = cv2.VideoCapture(0)
    frame_placeholder = st.empty()
    stop_button_pressed = st.button("Stop")
    while cap.isOpened() and not stop_button_pressed:
        ret, frame = cap.read()
        if not ret:
            st.write("Video Capture Ended")
            break
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame_placeholder.image(frame,channels="RGB")
        if cv2.waitKey(1) & 0xFF == ord("q") or stop_button_pressed:
            break
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
