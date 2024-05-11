import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('circle_coordinates1.csv')
center_x = data['Center X']
center_y = data['Center Y']

screen_width = 1920
screen_height = 1080

heatmap, xedges, yedges = np.histogram2d(center_x, center_y, bins=[screen_width//10, screen_height//10])

plt.figure(figsize=(10, 8))
plt.imshow(heatmap.T, extent=[0, screen_width, 0, screen_height], origin='lower', cmap='hot')
plt.colorbar(label='Frequency')
plt.title('Frequency of Focus')
plt.xlabel('X Coordinate')
plt.ylabel('Y Coordinate')
plt.grid(True)
plt.show()
