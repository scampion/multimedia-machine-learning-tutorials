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
import milk.supervised.randomforest as rf
#from milk.supervised.multi import one_against_one

logging.basicConfig(level=logging.DEBUG)

###############################################################################
# Load training data 

moto_vq_train, plane_vq_train = [np.load(file)
                                 for file 
                                 in ['moto_vq_train.npy','plane_vq_train.npy']]
labels = [0]* moto_vq_train.shape[0] + [1]* plane_vq_train.shape[0]


###############################################################################
# Train Random Forrest 

learner = rf.rf_learner()
#learner = rf.one_against_one(rf_learner)

model = learner.train(np.vstack([moto_vq_train,plane_vq_train]),
        np.array(labels))


###############################################################################
# Evaluation 
moto_vq_eval, plane_vq_eval  = [np.load(file) 
                                for file 
                                in ['moto_vq_eval.npy','plane_vq_eval.npy']]

errors = 0
errors += len([vq for vq in moto_vq_eval  if model.apply(vq) != 0 ])
errors += len([vq for vq in plane_vq_eval if model.apply(vq) != 1 ])
 
total = moto_vq_eval.shape[0]+plane_vq_eval.shape[0]
print 'Precision : %0.2f%% (%d/%d)' % (100-errors/total*100,total-errors,total)
