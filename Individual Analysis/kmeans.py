import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

data = pd.read_csv('circle_coordinates1.csv')
center_x = data['Center X']
center_y = data['Center Y']

coordinates = np.column_stack((center_x, center_y))

n_clusters = 5

kmeans = KMeans(n_clusters=n_clusters)
kmeans.fit(coordinates)

cluster_centers = kmeans.cluster_centers_

plt.scatter(center_x, center_y, c=kmeans.labels_, cmap='viridis', alpha=0.5)
plt.scatter(cluster_centers[:, 0], cluster_centers[:, 1], marker='x', color='red', label='Cluster Centers')
plt.title('K-means Clustering for Region Detection')
plt.xlabel('Center X')
plt.ylabel('Center Y')
plt.legend()
plt.show()
