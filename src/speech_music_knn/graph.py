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
logging.basicConfig(level=logging.DEBUG)
import speech_music as sm 

logging.info('Speech/Music classifier loaded') 

def predict(k=5,sample_size=1000):
    mfcc_size =10
    step = sample_size/mfcc_size
    predictions = {'music' : [],
                   'speech': [],
                   'both'  : []}

    for at,ar in predictions.items():
        file = 'data/query/%s.mp3' % at 
        logging.info('Load file %s' % file)
        mfcc = sm.load_mfcc(file)
        for j in range(0,int(len(mfcc)/step)): 
            sample = mfcc[j*step : (j+1)*step]
            r = sm.clf.predict(sample,k)
            logging.debug((j,r))
            predictions[at] = np.r_[predictions[at], r]
    return predictions

def display_results(predictions,sep=392):
    truth = { 'music' : [0]*len(predictions['music']),
              'speech': [1]*len(predictions['speech']),
              'both':   [1]*sep+[0](len(predictions['both']-sep))}
    for at in truth.keys():
        diff = np.abs(truth[at] - predictions[at])
        print '%s %0.3f' % (at, np.sum(diff)/len(diff))


for k in range(1,10):
    logging.info('K = %i' % k)
    p = predict(k)
    display_results(p)


