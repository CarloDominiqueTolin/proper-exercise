import cv2
import streamlit as st

video_capture = cv2.VideoCapture(0)

# Display the camera widget in Streamlit
stframe = st.empty()

while True:
    ret, frame = video_capture.read()
    if not ret:
        break

    # Display the captured frame in Streamlit
    stframe.image(frame, channels="BGR")

# Release the camera
video_capture.release()