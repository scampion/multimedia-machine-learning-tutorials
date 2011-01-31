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
from scikits.learn import neighbors
from subprocess import *
import cStringIO
import logging 

logging.basicConfig(level=logging.DEBUG)

def load_mfcc(file):
    '''
    return MFCC coefficients per 10ms 
    '''
    cmd_ffmpeg  = "ffmpeg -i %s " % file
    cmd_ffmpeg += "-f wav -acodec pcm_s16le -ar 16000 -ac 1 -" 
    cmd_sfbcep  = "sfbcep -f 16000 -p 14 -r 24 -e -Z -R -L 400 -D -A - -"
    cmd_scopy   = "scopy -o ascii - -"
    
    ffmpeg = Popen(cmd_ffmpeg.split(' '), stdout=PIPE,stderr=open(os.devnull)) 
    sfbcep = Popen(cmd_sfbcep.split(' '), stdin=ffmpeg.stdout, stdout=PIPE)
    scopy  = Popen(cmd_scopy.split(' '), stdin=sfbcep.stdout, stdout=PIPE)

    out, err = scopy.communicate()
    sfbcep.communicate()

    output = cStringIO.StringIO()
    output.write(out)
    output.seek(0)
    return np.loadtxt(output)


DATA_DIR='data' 
mfccs = {'speech' : [],
         'music'  : []}

for audio_type in mfccs.keys() :
    d = os.path.join(DATA_DIR,audio_type)
    for file in os.listdir(d):        
        logging.info('Loading file : %s' % file)
        if '.mp3' != os.path.splitext(file)[-1] :
            continue
        m = load_mfcc(os.path.join(DATA_DIR,audio_type,file))
        mfccs[audio_type].extend(m)

labels = [0]*len(mfccs['speech']) + [1]*len(mfccs['music'])
datas  = mfccs['speech']+mfccs['music']

clf = neighbors.Neighbors() 
clf.fit(datas,labels)

if module == '__main__':
    SAMPLE_IN_MS = 1000
    MFCC_SIZE_IN_MS =10
    K=5
    step = SAMPLE_IN_MS/MFCC_SIZE_IN_MS

    for i in ['music','speech','both']:
        mfcc = load_mfcc('data/query/%s.mp3' % i ) 
        for j in range(0,int(len(mfcc)/step)): 
            sample = mfcc[j*step : (j+1)*step]
            r = clf.predict(sample,k=K)

            nb_music  = len(np.flatnonzero(r == 1)) 
            nb_speech = len(np.flatnonzero(r == 0)) 
            if nb_music > nb_speech :
                res = 'music'
            else:
                res = 'speech'
            print '%s | sample %i | %s | m[%03d] p[%03d]' % (i,j,res,nb_music,
                                                             nb_speech)






