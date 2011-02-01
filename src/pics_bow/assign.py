# assign.py : bow   
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
import numpy.linalg
import pickle
import time 

logging.basicConfig(level=logging.DEBUG)

def vq3(vectors,centroids):
    '''
    naives python implementation
    '''
    nbcluster,dim = centroids.shape
    quant = [0]*nbcluster
    for v in vectors:
        d = []
        for c in centroids :
            delta = 0 
            for i in range(dim):
                delta += (v[i]-c[i])**2
            d.append(delta)
            best_c = min(d)
            quant[int(best_c)] += 1
    return quant

def vq2(vectors,centroids):
    nbcluster,dim = centroids.shape
    r = np.zeros((nbcluster,))
    for v in vectors:
        delta = (v - centroids)**2
        c =  np.sum(delta,axis=1).argmin()        
        r[c] += 1 
    return r

def vq(vectors,centroids):
    diff = vectors[np.newaxis,:,:] - centroids[:,np.newaxis,:]
    dist = np.sum(diff**2, axis=-1)
    ind = np.argmin(dist,axis=0)
    return np.resize(np.bincount(ind),8)


LEARN_SIZE = 100
EVAL_SIZE  = 696

moto, plane, centroids = [pickle.load(open(file)) 
                          for file in ['moto','plane','centroids']]

logging.info('Data loaded') 


t = time.time()

logging.info('Vector quantizaton of training data ...') 
moto_train_data = moto.items()[0:LEARN_SIZE]
moto_vq_train = [vq(vectors,centroids)
                 for file,vectors 
                 in moto_train_data]

logging.info('\tmoto done.') 

plane_train_data = plane.items()[0:LEARN_SIZE]
plane_vq_train = [vq(vectors,centroids)
                  for file,vectors 
                  in plane_train_data ]

logging.info('\tplane done.') 

np.save('moto_vq_train' ,moto_vq_train)
np.save('plane_vq_train',plane_vq_train)


logging.info('Vector quantizaton of evaluation data ...') 
#MOTO
moto_eval_data = moto.items()[ LEARN_SIZE : LEARN_SIZE+EVAL_SIZE ]
#moto_eval_data = moto.items()[ 0 : EVAL_SIZE ]
moto_vq_eval  = [vq(vectors,centroids) 
                 for file,vectors 
                 in moto_eval_data]

logging.info('\tmoto done.') 

#PLANE 
plane_eval_data = plane.items()[ LEARN_SIZE : LEARN_SIZE+EVAL_SIZE ]
#plane_eval_data = plane.items()[ 0 : EVAL_SIZE ]
plane_vq_eval  = [vq(vectors,centroids) 
                  for file,vectors 
                  in plane_eval_data]
logging.info('\tplane done.') 

logging.info('time '+str(time.time()-t))
np.save('moto_vq_eval',moto_vq_eval)
np.save('plane_vq_eval',plane_vq_eval)

