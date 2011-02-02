# bow.py : Bag of Word

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
import os
import logging 
import pickle
import numpy as np  
from string import punctuation

logging.basicConfig(level=logging.DEBUG)

def vectorize(dir,codebook):
    labels  = []
    vectors = []
    news    = []
    vocabulary = [k for k,v in codebook]
    vocab_size = len(vocabulary)

    for root,dirs,files in os.walk(dir):
        for new in files:
            cat = os.path.split(root)[-1]
            v = np.zeros((vocab_size),dtype='int32')
            for word in (word.strip(punctuation).lower()
                         for line in open(os.path.join(root,new))
                         for word in line.split()
                         if word.strip(punctuation).lower() 
                         in vocabulary):
                i = vocabulary.index(word)
                v[i] += 1 
            news.append(new)
            labels.append(cat)
            vectors.append(v)
    return news,labels,np.array(vectors)


codebook = pickle.load(open('tfidf_codebook.dat')) 
#filtering email adresss
codebook = [(w,v) for w,v in codebook if not '@' in w ]
#codebook = codebook[0:10000]

#for dataset in ['test']:
for dataset in ['training','test']:
    news,lab,vec = vectorize("Reuters21578-Apte-90Cat/%s/" % dataset,codebook)
    pickle.dump(lab,open('labels_%s.pik'  % dataset,'wb'))
    pickle.dump(vec,open('vectors_%s.pik' % dataset,'wb'))
    pickle.dump(news,open('news_%s.pik' % dataset,'wb'))
    logging.info('Vectorization %s finish' % dataset)

