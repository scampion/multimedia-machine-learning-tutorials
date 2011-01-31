# gist_map.py : kohonen SOM using gists descriptor  
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
from kohonen import Kohonen2DMap as km 
import logging 
import pickle 
import numpy as np 
import Image 
import os 

logging.basicConfig(level=logging.DEBUG)

PICS_DIR = "spatial_envelope_256x256_static_8outdoorcategories"
DIM = 960 
GISTS = pickle.load(open(PICS_DIR+'.gists'))
ALLGISTS = np.array([gist for file,gist in GISTS.items()])

#kind = [file.split('/')[1].split('_')[0] for file,gist in GISTS.items()[0:256]]
#for t in ['highway', 'opencountry', 'coast','street',
#          'tallbuilding','forest','insidecity','mountain']:
#     print t,len([f for f in kind if f==t  ])

def save_img(kmap,iteration,thumb_size=32):
    '''Function to save map using 3 dim, as RGB'''    
    outfile = 'iter_%08d.jpg' % iteration
    neurons = kmap.neurons
    tsize = (thumb_size,thumb_size) 
    size  = tuple([v * thumb_size for v in neurons.shape[0:2] ])
    im  = Image.new('RGB',size)

    for f,g in GISTS.items()[256:-1]:
        x,y = kmap.bmu(g)
        t = Image.open(f).resize(tsize)
        im.paste(t,(x*thumb_size,y*thumb_size))

    im.save(outfile)

def main(size,nbiter,lr):
    neurons_init = ALLGISTS[0:size**2].reshape((size,size,-1))    

    k = km(size,DIM,neurons_init)

    pics = ['forest_text111.jpg',
            'mountain_n44001.jpg',
            'coast_bea1.jpg',
            'street_art1041.jpg',
            'highway_bost161.jpg',
            'opencountry_land381.jpg',
            'insidecity_bost141.jpg',
            'tallbuilding_a632011.jpg']

    sample = np.array([ GISTS[os.path.join(PICS_DIR,p)] for p in pics ])
    k.learn(sample,nbiter,lr)#,callback=save_img)


def main_all(size,nbiter,lr):
    #neurons_init = None #ALLGISTS[0:size**2].reshape((size,size,-1))
    neurons_init = ALLGISTS[0:size**2].reshape((size,size,-1))
    k = km(size,DIM,neurons_init)
    k.learn(ALLGISTS,nbiter,lr)
    logging.info('Map computing ... finish')
    save_img(k,100000,thumb_size=64)

if __name__ == '__main__':
    from optparse import OptionParser
    parser = OptionParser()
    parser.add_option("-s", "--size", dest="size", help="size of the map",
                      default=8, type='int',  metavar="SIZE")
    parser.add_option("-i", "--iter", dest="nbiter", help="number of iteration",
                      default=8, type='int',  metavar="NBITER")

    parser.add_option("-l", "--lr", dest="learning_rate",
                      help="learning rate",default=1, type='float',
                      metavar="LR")

    (options, args) = parser.parse_args()

    main_all(options.size, options.nbiter, options.learning_rate)

            
	
	

    



