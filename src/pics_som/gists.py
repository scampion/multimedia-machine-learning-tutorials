# gists.py : compute gists for spatial envelope dataset 
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

import leargist 
import Image
import os
import logging 
import pickle 

LOG_FILENAME='gists.log'
logging.basicConfig(filename=LOG_FILENAME,level=logging.DEBUG)

PICS_DIR="spatial_envelope_256x256_static_8outdoorcategories"

def compute_gist():
    gists = {}
    for pic in os.listdir(PICS_DIR):
        path = os.path.join(PICS_DIR,pic)
        logging.debug('GIST computing : '+path)
        im = Image.open(path)        
        g = leargist.color_gist(im)
        gists[path] = g
    pickle.dump(gists,open(PICS_DIR+'.gists','wb'))

compute_gist()


    
