# classif.py : classif pictures with BOW    
# Copyright (C) 2011 Sebastien Campion <seb@scamp.fr>

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
from __future__ import division
import logging 
import numpy as np
from scikits.learn.svm import SVC
from scikits.learn.grid_search import GridSearchCV
from scikits.learn.metrics import confusion_matrix
from scikits.learn.metrics import classification_report

logging.basicConfig(level=logging.DEBUG)

###############################################################################
# Load training data 

moto_vq_train, plane_vq_train = [np.load(file)
                                 for file 
                                 in ['moto_vq_train.npy','plane_vq_train.npy']]
labels = [0]* moto_vq_train.shape[0] + [1]* plane_vq_train.shape[0]


###############################################################################
# Train SVM

param_grid = {
    'C': [1, 5, 10, 50, 100],
    'gamma': [0.0001, 0.0005, 0.001, 0.005, 0.01, 0.1],
    }

clf = GridSearchCV(SVC(kernel='rbf'), param_grid,
                   fit_params={'class_weight': 'auto'})

#clf = SVC(kernel='rbf')
#clf = SVC(kernel='linear')

clf.fit(np.vstack([moto_vq_train,plane_vq_train]),
        np.array(labels))

print "Best estimator found by grid search:"
#print clf.best_estimator

###############################################################################
# Evaluation 

moto_vq_eval, plane_vq_eval  = [np.load(file) 
                                for file 
                                in ['moto_vq_eval.npy','plane_vq_eval.npy']]

y_name = ['moto']*moto_vq_eval.shape[0] + ['plane']* plane_vq_eval.shape[0]
y_test = [0]* moto_vq_eval.shape[0] + [1]* plane_vq_eval.shape[0]
y_test = np.array(y_test)


y_pred = clf.predict(np.vstack([moto_vq_eval, plane_vq_eval]))


print classification_report(y_test, y_pred, labels=labels, class_names=y_name)
print confusion_matrix(y_test, y_pred)
