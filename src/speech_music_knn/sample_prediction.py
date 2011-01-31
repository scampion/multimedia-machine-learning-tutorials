# speech_music.py : audio segmentation by type music or speech 
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
import os 
import logging 
import speech_music as sm 

SAMPLE_IN_MS = 1000
MFCC_SIZE_IN_MS =10
K=5
step = SAMPLE_IN_MS/MFCC_SIZE_IN_MS

for i in ['music','speech','both']:
    mfcc = sm.load_mfcc('data/query/%s.mp3' % i ) 
    for j in range(0,int(len(mfcc)/step)): 
        sample = mfcc[j*step : (j+1)*step]
        r = sm.clf.predict(sample,k=K)
        res = 'speech'
        nb_music  = len(np.flatnonzero(r == 1)) 
        nb_speech = len(np.flatnonzero(r == 0)) 
        if nb_music / nb_speech > 1 :
            res = 'music'
        print '%s | sample %i | %s | m[%03d] p[%03d]' % (i,j,res,nb_music,nb_speech)



