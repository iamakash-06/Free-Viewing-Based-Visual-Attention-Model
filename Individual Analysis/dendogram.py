import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage

data = pd.read_csv('circle_coordinates1.csv')
center_x = data['Center X']
center_y = data['Center Y']
coordinates = np.column_stack((center_x, center_y))
Z = linkage(coordinates, method='ward')

plt.figure(figsize=(10, 5))
plt.title('Hierarchical Clustering Dendrogram')
plt.xlabel('Index')
plt.ylabel('Distance')
dendrogram(Z)
plt.show()
