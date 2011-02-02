# bow.py : Bag of Word  
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
import os
import logging 
import pickle
import numpy as np  
from scikits.learn.svm import SVC
from string import punctuation
from operator import itemgetter

logging.basicConfig(level=logging.DEBUG)
lab_train, vec_train , lab_test, vec_test = [pickle.load(open(file)) 
                                             for file 
                                             in ['labels_training.pik',
                                                 'vectors_training.pik',
                                                 'labels_test.pik',
                                                 'vectors_test.pik']]
logging.info("Data loaded") 

cat_train = list(set(lab_train))
cat_test  = list(set(lab_test))
assert cat_test == cat_train 

lab_train = [cat_train.index(l) for l in lab_train]
lab_test  = [cat_test.index(l) for l in lab_test]

clf = SVC(kernel='rbf')
clf.fit(vec_train, lab_train)

pickle.dump(clf,open('classifier.pik','wb'))






