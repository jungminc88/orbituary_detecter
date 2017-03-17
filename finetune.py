#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 19:40:37 2017

@author: min
"""
import collections
import numpy as np
#First, determine the list of candidates for correct names:
#dict_temp = dict(collections.Counter(list_names).most_common())
#list_candidates = sorted(dict_temp, key=.get,reverse=True)[:10]


#You can use the above list as the list of candidates, but for reducing the run-time,
#I recommend reducing the elements in list_canditates as much as possible.
list_candidates = [u'ムッシュかまやつ', u'綾小路翔',u'堺正章']

#Next, for every possible pair, count the number of cooccurrence:

l=len(list_candidates)

coocc_mat=np.zeros((l, l))

for i in range(l):
    for j in range(i+1,l):
        
        for n in collections.Counter(list_cooccurrence).keys():
                if list_candidates[i] in n and list_candidates[j] in n:
                    coocc_mat[i,j] += collections.Counter(list_cooccurrence).values()[collections.Counter(list_cooccurrence).keys().index(n)]
        coocc_mat[j,i] = coocc_mat[i,j]

for i in range(l):
    print max(coocc_mat[i,:])/sum(coocc_mat[i,:])
    

#If person A occurs mostly with person B but not with others while person B occurs with others,
#then we can infer that B is the deceased person and A comes up only in relation to B, hence eliminate A from the list.
