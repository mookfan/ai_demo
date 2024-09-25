import cv2
import streamlit as st
import face_recognition
from deepface import DeepFace
import numpy as np
from datetime import datetime

st.set_page_config(layout="wide")
st.title("Webcam Live Feed")

models = ["VGG-Face", "Facenet", "OpenFace", "DeepFace", "DeepID"]


with st.container():
    col1, col2 = st.columns(2)
    with col1:
        sub_col1, sub_col2 = st.columns(2)
        with sub_col1:
            uploaded_file = st.file_uploader("Target Person", type="jpg")
            if uploaded_file is not None:
                # Convert the file to an opencv image.
                file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
                opencv_image = cv2.imdecode(file_bytes, 1)

                # Now do something with the image! For example, let's display it:
        with sub_col2:
            if uploaded_file is not None:
                st.image(opencv_image, channels="BGR", use_column_width=True)
        run = st.checkbox('Run Detection')
    with col2:
        st.text("Camera 1")
        FRAME_WINDOW = st.image([], use_column_width=True)
        camera = cv2.VideoCapture(0)

DETECT_WINDOW = st.image([])

while run:
    _, frame = camera.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    # Find all the faces and face encodings in the current frame of video
    face_locations = face_recognition.face_locations(frame)

    # Display the results
    for top, right, bottom, left in face_locations:
        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
    
        face = frame[top:bottom, left:right]
        try:
            # Compare the current frame with the reference image
            result = DeepFace.verify(img1_path=frame, img2_path=opencv_image)
            if result["verified"]:
                # resize the image
                face_rez = cv2.resize(face.copy(), (50, 50))
                DETECT_WINDOW.image(face_rez, caption=f"Founded {datetime.now()}")
        except:
            pass
    FRAME_WINDOW.image(frame)