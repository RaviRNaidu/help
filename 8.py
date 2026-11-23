#K-means
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

# Load Iris dataset
iris = load_iris()
X = iris.data

# Use first two features for 2D clustering
X = X[:, :2]

# Create and train K-Means model
model = KMeans(n_clusters=3, random_state=42, n_init=10)
y_pred = model.fit_predict(X)

# Display clustering metrics
print("Number of Clusters:", 3)
print("Inertia:", model.inertia_)
print("Silhouette Score:", silhouette_score(X, y_pred))

# Display cluster centers
print("\nCluster Centers:")
print(model.cluster_centers_)

# Plot clusters
plt.scatter(X[:, 0], X[:, 1], c=y_pred, cmap='viridis',
            label="Data Points")

# Plot centroids
plt.scatter(model.cluster_centers_[:, 0],
            model.cluster_centers_[:, 1],
            color='red', marker='X', s=200, label="Centroids")

plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")
plt.title("K-Means Clustering - Iris Dataset")
plt.legend()
plt.show()

# User input prediction
print("\nEnter flower measurements:")
sl = float(input("Sepal Length: "))
sw = float(input("Sepal Width: "))

sample = np.array([[sl, sw]])
cluster = model.predict(sample)

print("Predicted Cluster:", cluster[0] + 1)
