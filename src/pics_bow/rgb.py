# surfs.py : compute surfs descriptors for calltech 256 dataset 
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
import cv 
import numpy as np
import os,pickle
import PIL.Image as Image 

logging.basicConfig(level=logging.DEBUG)

PICS_DIR = "256_ObjectCategories"
CATS = { 'moto' : '145.motorbikes-101',
         'plane': '251.airplanes-101' } 

for name,dir in CATS.items():
    dir = os.path.join(PICS_DIR,dir)
    raws = {}
    for file in os.listdir(dir):
        file = os.path.join(dir,file)
        logging.debug('%s in progress ...' % file)
        img = Image.open(file)
        img = img.resize((64, 64), Image.ANTIALIAS)
        img = img.convert('L')
        a = img.getdata()
        raws[file] = np.array(a).reshape((64,64))
    pickle.dump(raws, open(name,'wb'))
