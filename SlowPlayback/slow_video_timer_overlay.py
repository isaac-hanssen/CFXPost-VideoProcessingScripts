import cv2
import os

video_name = "UPSA_Heat_Contour_1.wmv"
playback_speed = 0.1

simulation_start = 0
simulation_end = 100

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
frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

new_fps = fps * playback_speed

writer = cv2.VideoWriter(
    output_path,
    cv2.VideoWriter_fourcc(*"mp4v"),
    new_fps,
    (width, height)
)

frame_number = 0

while True:
    ret, frame = cap.read()

    if not ret:
        break

    progress = frame_number / max(frames - 1, 1)

    sim_time = (
        simulation_start
        + progress * (simulation_end - simulation_start)
    )

    text = f"Time = {sim_time:.1f} min"

    cv2.putText(
        frame,
        text,
        (20, height - 30),      # bottom left
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (255, 255, 255),
        3
    )

    cv2.putText(
        frame,
        text,
        (20, height - 30),      # black outline
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 0, 0),
        1
    )

    writer.write(frame)
    frame_number += 1

cap.release()
writer.release()