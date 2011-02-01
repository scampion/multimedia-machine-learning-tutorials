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
 
logging.basicConfig(level=logging.DEBUG)

PICS_DIR = "256_ObjectCategories"
CATS = { 'moto' : '145.motorbikes-101',
         'plane': '251.airplanes-101' } 

for name,dir in CATS.items():
    dir = os.path.join(PICS_DIR,dir)
    surfs = {}
    for file in os.listdir(dir):
        file = os.path.join(dir,file)
        logging.debug('%s in progress ...' % file)
        image      = cv.LoadImage(file)  
        image_gray = cv.CreateImage(cv.GetSize(image), image.depth, 1)
        cv.CvtColor(image, image_gray, cv.CV_BGR2GRAY)
        k, v = cv.ExtractSURF(image_gray, None, cv.CreateMemStorage(),
                              (1, 300, 3, 1))
        surfs[file] = np.array(v)
    pickle.dump(surfs,open(name,'wb'))
