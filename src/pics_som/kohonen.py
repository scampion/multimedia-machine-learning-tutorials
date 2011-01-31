# kohonen.py : kohonen self organized map 2D  
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
import Image
import math 
import numpy as np

LOG_FILENAME='kohonen.log'
logging.basicConfig(filename=LOG_FILENAME,level=logging.DEBUG)

def save_rgb(kmap,iteration,thumb_size=32):
    '''Function to save map using 3 dim, as RGB'''    
    outfile = 'iter_%08d.jpg' % iteration
    neurons = kmap.neurons
    tsize = (thumb_size,thumb_size) 
    size  = tuple([v * thumb_size for v in neurons.shape[0:2] ])
    im  = Image.new('RGB',size)

    for x in range(neurons.shape[0]):
        for y in range(neurons.shape[1]):
            color = tuple(neurons[x][y])
            t = Image.new('RGB',tsize,color)
            im.paste(t,(x*thumb_size,y*thumb_size))            
    im.save(outfile)

class Kohonen2DMap():
    def __init__(self,size,dim,neurons=None):
        self.log = logging.getLogger('kohonen.map')
        self.dim = dim 
        self.size = size 
        self.neurons = neurons
        if neurons == None  :
            self.neurons = np.random.rand(size,size,dim)#/10
        self.iteration = 0 

    def eucl(self,x, y):
        d = x - y
        #return np.sqrt(np.sum(d ** 2 , axis=-1))
        return np.sum(d ** 2 , axis=-1) #optimize perf without sqrt compute
        
    def bmu(self,data):
        assert data.shape[0] == self.neurons.shape[-1] 
        data = np.resize(data,self.neurons.shape) 
        dists = self.eucl(data,self.neurons)
        min = dists.argmin()
        #w = np.unravel_index(min,dists.shape)
        return divmod(min,self.size)
        
    def learn(self,datas,nbiter,learning_rate=1,callback=None):
        '''Given an sample of datas, we randomly choose one of them for each 
        iteration.
        A good ratio, nb datas = 2 or 3 x nbiter'''
        self.iteration = 0   
        indices = np.random.random_integers(0,len(datas)-1,nbiter)
        for i in indices: 
            l = nbiter/self.size
            lr = learning_rate * math.exp(-self.iteration/l)
            self._learn_vector(datas[i], nbiter, lr)
            self.iteration += 1 
            if callback != None:
                callback(self,self.iteration)

    def _learn_vector(self, data, nbiter, lr):
        w = self.bmu(data)
        radius = self.radius_of_the_neighbordhood(nbiter)
        for n in self.neurons_in_radius(w,radius):
            nx,ny = n
            wt = self.neurons[nx][ny]
            dr = self.dist(w,n,radius)
            self.neurons[nx][ny] = wt + dr*lr*(data-wt)

            self.log.debug(('nod',n,
                            'l_rate',lr,
                            'd_radius',dr))

        self.log.debug(('bmu',w,
                        'iter',self.iteration,
                        'radius',radius))
    
    def dist(self,w,n,radius):
        wx,wy = w
        nx,ny = n
        d = (wx-nx)**2 + (wy-ny)**2
        #offcial paper implementation : return math.exp(-d/2*radius**2)
        return math.exp(-d/radius)
    
    def neurons_in_radius(self,w,radius):
        wi,wj = w 
        r = []
        for i in range(self.neurons.shape[0]):
            for j in range(self.neurons.shape[1]):
                if math.sqrt((i-wi)**2 + (j-wj)**2) < radius:
                    r.append((i,j))
        return r
        
    def radius_of_the_neighbordhood(self,nbiter):
        l = nbiter/self.size
        return self.size * math.exp(-self.iteration/l)


