import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN
from matplotlib.colors import ListedColormap

data = pd.read_csv('circle_coordinates1.csv')
center_x = data['Center X']
center_y = data['Center Y']
coordinates = np.column_stack((center_x, center_y))
dbscan = DBSCAN(eps=0.1, min_samples=5)
dbscan.fit(coordinates)
colors = np.array(['blue', 'red', 'green', 'orange'])
labels = np.array(['Cluster 1', 'Cluster 2', 'Cluster 3', 'Noise'])
cmap = ListedColormap(colors)
plt.scatter(center_x, center_y, c=dbscan.labels_, cmap=cmap, alpha=0.5)
plt.title('DBSCAN Clustering for Region Detection')
plt.xlabel('Center X')
plt.ylabel('Center Y')
plt.legend(handles=[plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=color, markersize=10, label=label) for color, label in zip(colors, labels)])
plt.show()