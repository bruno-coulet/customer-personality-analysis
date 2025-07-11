import numpy as np

def create_centroids(X, K):
    #  k indices différents et aléatoires parmi les lignes de X, sans répétition.
    indices = np.random.choice(X.shape[0], K, replace=False)
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


def compute_inertia(X, labels, centroids):
    inertia = 0
    for i in range(centroids.shape[0]):
        cluster_points = X[labels == i]
        distances = np.linalg.norm(cluster_points - centroids[i], axis=1)
        inertia += np.sum(distances ** 2)
    return inertia






