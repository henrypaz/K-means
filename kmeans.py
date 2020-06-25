from copy import deepcopy
import numpy as np
import matplotlib.pyplot as plot
import pandas as pd
from sklearn.cluster import KMeans
#importing Dataset
dataset = pd.read_csv('Libro1.csv')
X = dataset.iloc[:, 1:6].values #colonne che mi interessano
print (X)
#Find the number of clusters
wcss = []

for i in range (1,16): #15 cluster
    kmeans = KMeans(n_clusters = i, init='k-means++', random_state=0) 
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)

plot.plot(range(1,16),wcss)
plot.title('Elbow Method')
plot.xlabel('Number of clusters')
plot.ylabel('wcss')
plot.show()

#KMeans clustering
kmeans= KMeans(n_clusters=5, max_iter=600, algorithm = 'auto')
y=kmeans.fit_predict(X)

plot.scatter(X[y == 0,0], X[y==0,1], s=25, c='red', label='Cluster 1')
plot.scatter(X[y == 1,0], X[y==1,1], s=25, c='blue', label='Cluster 2')
plot.scatter(X[y == 2,0], X[y==2,1], s=25, c='magenta', label='Cluster 3')
plot.scatter(X[y == 3,0], X[y==3,1], s=25, c='cyan', label='Cluster 4')

plot.scatter(kmeans.cluster_centers_[:,0], kmeans.cluster_centers_[:,1], s=25, c='yellow', label='Centroid')
plot.title('KMeans Clustering')
plot.xlabel('Acousticness')
plot.ylabel('Danceability')
plot.legend()
plot.show()
