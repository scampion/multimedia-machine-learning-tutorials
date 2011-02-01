# kmeans.py : compute centroids  
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
import numpy as np
import pickle
from scikits.learn.cluster import KMeans
import logging 
import time

logging.basicConfig(level=logging.DEBUG)

LEARN_SIZE = 100
K = 8
ITER = 10 

moto,plane  = [pickle.load(open(file)) 
               for file in ['moto','plane']]

logging.info('Data loaded') 

m   = np.vstack([v for f,v in  moto.items()[0:LEARN_SIZE]])
p   = np.vstack([v for f,v in plane.items()[0:LEARN_SIZE]])
all = np.vstack([m,p])

km = KMeans(k=K,max_iter=ITER)
km.fit(all) 

filename = 'centroids_%d_%d_%d' % (LEARN_SIZE,K,ITER)
pickle.dump(km.cluster_centers_,open(filename,'wb'))

