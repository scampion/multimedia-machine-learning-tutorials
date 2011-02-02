import numpy as np 
from scipy import linalg

def pca(X, n_components):
    mean = np.mean(X, axis=0)
    X -= mean
    U, S, V = linalg.svd(X, full_matrices=False)

    #whiten 
    n_samples = X.shape[0]
    explained_variance = (S ** 2) / n_samples
    explained_variance_ratio = explained_variance / explained_variance.sum()
    components = np.dot(V.T, np.diag(1.0 / S)) * np.sqrt(n_samples)

    #keep some values
    components = V.T[:, :n_components]

    return components, mean 

def transform(X, mean, components):
    Xr = X - mean
    Xr = np.dot(Xr, components)
    return Xr    

def eigenfaces(components):
    return components.T.reshape((-1, 64, 64))
