"""
spam_naives_classifer.py : tutorial implementation of naives bayesiens spam classifier 
 
Copyright (C) 2011 Sebastien Campion <seb@scamp.fr>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
from __future__ import division
import os
import numpy as np
from math import sqrt,pi,exp,log

#use numpy module function loadtxt to load data as 
#an 2D array of vectors
 
data = np.loadtxt('spambase.data') 
spams = [ d for d in data if d[-1]==1]
hams  = [ d for d in data if d[-1]==0]

def learn(data,learn_size=50,nbattrs=58): 
    """
    learning function : 
    compute mean and standard deviation for each attributes
    :rtype : array of tuple (mean,std)
    """
    data = np.array(data)
    sample = data#[0:learn_size]
    attrs = np.hsplit(sample, nbattrs)
    return [ (np.mean(v), np.std(v)) for v in attrs[:-1] ]

spams_stats = learn(spams)
hams_stats  = learn(hams)


# print 'spams stats'
# for e,v in spams_stats:
#     print e,v
# print 'hams stats',hams_stats
# for e,v in spams_stats:
#     print e,v

def pgauss(esp,var,x):
    """
    compute probability using gaussian function
    """
    return 1 / (sqrt(var) * sqrt(2*pi)) * exp( - 0.5 * (((x - esp) / var) **2 ))

def is_spam(data,spams_stats,hams_stats):
    r = 0
    for i,d in enumerate(data[:-1]):
        e,v = spams_stats[i]
        if e == 0 and v == 0 :
            ps = 0 
        else :
            ps = pgauss(e,v,d)

        e,v = hams_stats[i]
        if e == 0 and v == 0 :
            ph = 1
        else :
            ph = pgauss(e,v,d)

        try : 
            r += log(ps/ph)
        except ValueError:
            continue
            print 'math value error', data
        except ZeroDivisionError:
            #print 'ph is null math value error', data
            return True 
        
    return r > 0 

#Some individual test 
#for i in [1000,2000,4000]:
#    print 'mail nb:',i,is_spam(data[i],spams_stats,hams_stats)


rh = rs = nb_spams_detected = 0 
for d in data:
    spam = is_spam(d,spams_stats,hams_stats)
    #print 'is spam',spam, d[-1],d[-1]==1,d[-1] == spam
    if spam : 
        nb_spams_detected += 1 

    if d[-1] == 1 and spam : 
            rs += 1 

    if d[-1] == 0 and not spam : 
            rh += 1 

print '-'*80
print 'HAM'
print 'precision :', rh/(len(data)-nb_spams_detected)
print 'recall :', rh/len(hams)

print '-'*80
print 'SPAM'
print 'precision :', rs/nb_spams_detected
print 'recall :', rs/len(spams)


