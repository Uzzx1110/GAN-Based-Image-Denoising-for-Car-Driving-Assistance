import streamlit as st
import tempfile
import os
import base64
from backend import process_frame, obj_model, sign_model, enet_model
import cv2

st.set_page_config(page_title="🚗 Autonomous Driving App", layout="centered")
st.title("🚗 Driving Assistance Simulation")
st.markdown("Choose your source for detection:")


def set_background_with_gradient(image_file):
    with open(image_file, "rb") as img_file:
        encoded = base64.b64encode(img_file.read()).decode()
    css = f'''
    <style>
    .stApp {{
      /* background image */
      background: url("data:image/avif;base64,{encoded}") center/cover no-repeat fixed;
      position: relative;
    }}
    .stApp::before {{
      content: "";
      position: absolute;
      top: 0; left: 0; right: 0; bottom: 0;
      /* gradient overlay from transparent to rgba black */
      background: linear-gradient(
        to bottom right,
        rgba(0, 0, 0, 0.3) 0%,
        rgba(0, 0, 0, 0.6) 100%
      );
      z-index: -1;
    }}
    /* ensure content is above overlay */
    .stApp > * {{
      position: relative;
      z-index: 0;
    }}
    </style>
    '''
    st.markdown(css, unsafe_allow_html=True)

# Apply it
set_background_with_gradient(r"C:\Users\DELL\Documents\GitHub\AutonomousDrivingGanMV\aerial-drone-following-futuristic-3d-600nw-2198425195.webp")

# === Helper function ===
def process_uploaded_video(input_path, output_path):
    cap = cv2.VideoCapture(input_path)
    fps = int(cap.get(cv2.CAP_PROP_FPS)) or 30
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        processed_frame = process_frame(frame, obj_model, sign_model, enet_model)
        out.write(processed_frame)

    cap.release()
    out.release()

# === Webcam Option ===
if st.button("Live Webcam"):
    st.warning("Press 'q' in the webcam window to stop live detection.")
    cap = cv2.VideoCapture(0)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        processed_frame = process_frame(frame, obj_model, sign_model, enet_model)

        cv2.imshow("Live Webcam Detection", processed_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# === Upload Video Option ===
uploaded_file = st.file_uploader("Upload a video for processing (mp4, avi, mov)", type=["mp4", "avi", "mov"])

if uploaded_file is not None:
    st.success("Video uploaded successfully!")

    # Save temp file
    tfile = tempfile.NamedTemporaryFile(delete=False, suffix='.mp4')
    tfile.write(uploaded_file.read())

    output_video_path = "processed_output.mp4"
    
    st.info("Processing your video, please wait...")
    process_uploaded_video(tfile.name, output_video_path)
    st.success("Processing done! Here's the output:")

    st.video(output_video_path)

    with open(output_video_path, "rb") as file:
        st.download_button(
            label="Download Processed Video",
            data=file,
            file_name="processed_output.mp4",
            mime="video/mp4"
        )
