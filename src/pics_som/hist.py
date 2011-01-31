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

def compute_hist():
    hists = {}
    for pic in os.listdir(PICS_DIR):
        path = os.path.join(PICS_DIR,pic)
        logging.debug('HIST computing : '+path)
        im = Image.open(path)        
        g = learhist.color_hist(im)
        hists[path] = g
    pickle.dump(hists,open(PICS_DIR+'.hists','wb'))

compute_hist()


    
