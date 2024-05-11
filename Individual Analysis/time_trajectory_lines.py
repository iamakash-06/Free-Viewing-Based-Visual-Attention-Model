import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import colors as mcolors

data = pd.read_csv('circle_coordinates1.csv')
time = data['Time (s)']
center_x = data['Center X']
center_y = data['Center Y']

normalized_time = (time - time.min()) / (time.max() - time.min())
cmap = plt.cm.viridis

plt.figure(figsize=(8, 6))
for i in range(len(center_x)):
    plt.scatter(center_x[i], center_y[i], c=cmap(normalized_time[i]), s=100, alpha=0.5)

for i in range(len(center_x) - 1):
    plt.plot([center_x[i], center_x[i + 1]], [center_y[i], center_y[i + 1]], color='gray', alpha=0.5)

norm = mcolors.Normalize(vmin=time.min(), vmax=time.max())
cbar = plt.colorbar(plt.cm.ScalarMappable(norm=norm, cmap=cmap))
cbar.set_label('Time (s)')

plt.title('User Gaze Trajectory')
plt.xlabel('X Coordinate')
plt.ylabel('Y Coordinate')
plt.grid(True)
plt.show()
