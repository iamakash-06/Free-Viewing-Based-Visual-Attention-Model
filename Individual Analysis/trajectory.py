import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('circle_coordinates1.csv')
time = data['Time (s)']
center_x = data['Center X']
center_y = data['Center Y']

plt.figure(figsize=(8, 6))
plt.plot(center_x, center_y, marker='o', markersize=5, linestyle='-', color='b')
plt.title('User Gaze Trajectory')
plt.xlabel('X Coordinate')
plt.ylabel('Y Coordinate')
plt.grid(True)
plt.show()
