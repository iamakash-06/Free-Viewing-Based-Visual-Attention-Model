import cv2
import numpy as np
import csv
import os

video_path = '20_2.mp4'
csv_filename = 'circle_coordinates1.csv'

if os.path.exists(csv_filename):
    os.remove(csv_filename)

cap = cv2.VideoCapture(video_path)

fps = cap.get(cv2.CAP_PROP_FPS)

csv_file = open(csv_filename, 'w', newline='')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Time (s)', 'Center X', 'Center Y', 'Radius'])

frame_number = 0

while cap.isOpened():
    ret, frame = cap.read()

    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    edges = cv2.Canny(gray, 50, 150)

    circles = cv2.HoughCircles(edges, cv2.HOUGH_GRADIENT, dp=1, minDist=20,
                               param1=50, param2=30, minRadius=50, maxRadius=69)

    if circles is not None:
        circles = np.uint16(np.around(circles))
        for circle in circles[0, :]:
            center = (circle[0], circle[1])
            radius = circle[2]
            time_seconds = frame_number / fps
            csv_writer.writerow([time_seconds, center[0], center[1], radius])
            cv2.circle(frame, center, radius, (0, 255, 0), 2)

    cv2.imshow('Detected Circles', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    frame_number += 1

csv_file.close()

cap.release()
cv2.destroyAllWindows()