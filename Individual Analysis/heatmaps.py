import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('circle_coordinates1.csv')
center_x = data['Center X']
center_y = data['Center Y']

heatmap, xedges, yedges = np.histogram2d(center_x, center_y, bins=50)

plt.figure(figsize=(10, 8))
plt.imshow(heatmap.T, extent=[xedges[0], xedges[-1], yedges[0], yedges[-1]], origin='lower', cmap='hot')
plt.colorbar(label='Frequency')
plt.title('User Gaze Heatmap')
plt.xlabel('X Coordinate')
plt.ylabel('Y Coordinate')
plt.grid(True)
plt.show()
