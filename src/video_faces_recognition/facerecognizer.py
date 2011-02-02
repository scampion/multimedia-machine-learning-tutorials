import os
import sys
import Image
from gzip import GzipFile

import numpy as np
import pylab as pl

from scikits.learn.grid_search import GridSearchCV
from scikits.learn.metrics import classification_report
from scikits.learn.metrics import confusion_matrix
from scikits.learn.pca import RandomizedPCA
from scikits.learn.pca import PCA
import pca 
from scikits.learn.svm import SVC

################################################################################
# Load training data 
train_dir = "training_preprocessed"
files = [ (os.path.basename(root), os.path.join(root,f))
          for root, dir, files in os.walk(train_dir)
          for f in files]

faces = [np.array(Image.open(f).getdata())
         for c, f in files]
face_filenames = [c for c, f in files]

# normalize each picture by centering brightness
faces = np.array(faces) 
faces -= faces.mean(axis=1)[:, np.newaxis]


################################################################################
# Index category names into integers suitable for scikit-learn
categories = [c for c, f in files]
category_names = np.unique(categories)
target = np.searchsorted(category_names, categories)
selected_target = target 

mask = np.in1d(target, selected_target)

X_train = faces
y_train = target

################################################################################
# Compute a PCA (eigenfaces) on the face dataset

n_components = 150
print "Extracting the top %d eigenfaces" % n_components
pca_sl = RandomizedPCA(n_components=n_components, whiten=True)
pca_sl.fit(X_train)
#components, mean = pca.pca(X_train, n_components)

#print "PCA components shape", pca.components_.T.shape 
#eigenfaces = pca.components_.T.reshape((-1, 64, 64))

# project the input data on the eigenfaces orthonormal basis
X_train_pca = pca_sl.transform(X_train)
#X_train_pca = pca.transform(X_train, mean, components)

################################################################################
# Train a SVM classification model

print "Fitting the classifier to the training set"
param_grid = {
    'C': [1, 5, 10, 50, 100],
    'gamma': [0.0001, 0.0005, 0.001, 0.005, 0.01, 0.1],
    }
clf = GridSearchCV(SVC(kernel='rbf'), param_grid,
                   fit_params={'class_weight': 'auto'})

clf = clf.fit(X_train_pca, y_train)
print "Best estimator found by grid search:"
print clf.best_estimator



