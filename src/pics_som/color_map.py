# color_map.py : kohonen SOM 'hello word'  
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
import kohonen 
import logging 
import numpy as np 

logging.basicConfig(level=logging.DEBUG)


def main(size,nbiter,lr):
    NBCHANNEL = 3 
    init = np.random.random_integers(0,255,size**2*NBCHANNEL)
    init = init.reshape(size,size,NBCHANNEL)

    sample = np.array([[0,0,0],
                       [255,0,0],
                       [0,255,0],
                       [0,0,255],
                       [255,255,0],
                       [0,255,255]])

    k = km(size,NBCHANNEL,init)
    kohonen.save_rgb(k,0)
    k.learn(sample,nbiter,lr,callback=kohonen.save_rgb)
    kohonen.save_rgb(k,100000)

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

    main(options.size, options.nbiter, options.learning_rate)

            
	
	

    



