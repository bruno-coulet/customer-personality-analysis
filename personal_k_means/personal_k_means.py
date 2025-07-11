
from sklearn.datasets import load_iris
import numpy as np, pandas as pd

iris = load_iris()
X = iris.data       
y = iris.target     

df = pd.DataFrame(X, columns=iris.feature_names)

# X.shape
X.shape[0]

# Nombre de centroïdes
K = 4

def create_centroids(X, K):
    # Nombre de centroïde
    k = 4
    #  k indices différents et aléatoires parmi les lignes de X, sans répétition.
    indices = np.random.choice(X.shape[0], k, replace=False)
    # tableau (k, 4) contenant k centroïdes initiaux choisis parmi les points du dataset.
    initial_centroids = X[indices]

    return initial_centroids


def assign_to_clusters(X, initial_centroids):
    # Calcul des distances entre chaque point et chaque centroïde
    distances = np.linalg.norm(X[:, np.newaxis] - initial_centroids, axis=2)
    
    # Affectation : indice du centroïde le plus proche
    cluster_labels = np.argmin(distances, axis=1)
    
    return cluster_labels    


def update_centroids(X, cluster_labels, K):
    new_centroids = np.zeros((K, X.shape[1]))
    for i in range(K):
        cluster_points = X[cluster_labels == i]
        if len(cluster_points) > 0:
            new_centroids[i] = cluster_points.mean(axis=0)
    return new_centroids


centroids = create_centroids(X, K)

for iteration in range(10):  # ou jusqu'à convergence
    cluster_labels = assign_to_clusters(X, centroids)
    new_centroids = update_centroids(X, cluster_labels, K)
    
    if np.allclose(new_centroids, centroids, atol=1e-4):
        print(f"Convergence à l’itération {iteration}")
        break
    
    centroids = new_centroids



print("Centroids finaux :\n", centroids,"\n")
print("Exemples de labels assignés :", cluster_labels[:10])
