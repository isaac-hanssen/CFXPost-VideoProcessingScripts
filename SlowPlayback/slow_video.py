import cv2
import os

video_name = "UPSA_Heat_Contour_1.wmv"
playback_speed = 0.1

input_path = os.path.join("IO", "input", video_name)

name, _ = os.path.splitext(video_name)
output_path = os.path.join(
    "IO",
    "output",
    f"{name}x{playback_speed}.mp4"
)

cap = cv2.VideoCapture(input_path)

fps = cap.get(cv2.CAP_PROP_FPS)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

writer = cv2.VideoWriter(
    output_path,
    cv2.VideoWriter_fourcc(*"mp4v"),
    fps * playback_speed,
    (width, height)
)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    writer.write(frame)

cap.release()
writer.release()

print(f"Saved: {output_path}")
