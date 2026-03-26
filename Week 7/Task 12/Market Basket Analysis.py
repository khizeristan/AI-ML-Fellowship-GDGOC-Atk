# Import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.datasets import make_blobs
from sklearn.cluster import AgglomerativeClustering
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE

from mlxtend.frequent_patterns import apriori, association_rules

# Generate synthetic dataset
X, y = make_blobs(n_samples=300, centers=3, random_state=42)

# Plot original data
plt.scatter(X[:,0], X[:,1])
plt.title("Original Dataset")
plt.show()

# -------- K-Means (from scratch) --------
def kmeans(X, k, iterations=100):
    # Randomly initialize centroids
    centroids = X[np.random.choice(len(X), k, replace=False)]

    for _ in range(iterations):
        clusters = [[] for _ in range(k)]

        # Assign points to nearest centroid
        for point in X:
            distances = [np.linalg.norm(point-centroid) for centroid in centroids]
            cluster_index = np.argmin(distances)
            clusters[cluster_index].append(point)

        # Update centroids
        new_centroids = []
        for cluster in clusters:
            new_centroids.append(np.mean(cluster, axis=0))

        centroids = np.array(new_centroids)

    return centroids, clusters

# Apply K-Means
centroids, clusters = kmeans(X, 3)

# Plot clusters
for cluster in clusters:
    cluster = np.array(cluster)
    plt.scatter(cluster[:,0], cluster[:,1])

plt.scatter(centroids[:,0], centroids[:,1], c='red', s=200)
plt.title("K-Means Clustering")
plt.show()

# -------- Hierarchical Clustering --------
model = AgglomerativeClustering(n_clusters=3)
labels = model.fit_predict(X)

plt.scatter(X[:,0], X[:,1], c=labels)
plt.title("Hierarchical Clustering")
plt.show()

# -------- PCA --------
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

plt.scatter(X_pca[:,0], X_pca[:,1])
plt.title("PCA Result")
plt.show()

# -------- t-SNE --------
tsne = TSNE(n_components=2)
X_tsne = tsne.fit_transform(X)

plt.scatter(X_tsne[:,0], X_tsne[:,1])
plt.title("t-SNE Visualization")
plt.show()

# -------- Market Basket Analysis --------
data = {
    'Milk':[1,0,1,1,0],
    'Bread':[1,1,1,0,0],
    'Butter':[0,1,1,1,0],
    'Eggs':[1,1,0,1,1]
}

df = pd.DataFrame(data)

# Generate frequent itemsets
frequent_items = apriori(df, min_support=0.4, use_colnames=True)

# Generate association rules
rules = association_rules(frequent_items, metric="confidence", min_threshold=0.6)

# Plot rules
sns.scatterplot(x="support", y="confidence", data=rules)
plt.title("Association Rules")
plt.show()