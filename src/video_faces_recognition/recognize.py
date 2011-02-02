#!/usr/bin/python
import sys
import os
import cv
import Image 
import facerecognizer 

pi = Image.open(sys.argv[1])
f = np.array(pi.getdata())                
X_test_pca = facerecognizer.pca_sl.transform([f])
y_pred = facerecognizer.clf.predict(X_test_pca)
name = facerecognizer.category_names[y_pred[0]]
print name 
