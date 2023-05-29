import cv2
import streamlit as st


def list_camera_devices():
    index = 0
    while True:
        cap = cv2.VideoCapture(index)
        if not cap.read()[0]:
            break
        print(f"Camera {index}: OK")
        cap.release()
        index += 1

list_camera_devices()

#video_capture = cv2.VideoCapture(0)

# Display the camera widget in Streamlit
stframe = st.empty()

#while True:
    #ret, frame = video_capture.read()
    #if not ret:
    #    break

    # Display the captured frame in Streamlit
    #stframe.image(frame, channels="BGR")

# Release the camera
#video_capture.release()