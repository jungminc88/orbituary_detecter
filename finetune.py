#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 19:40:37 2017

@author: min
"""
import collections

#First, determine the list of candidates for correct names:

#list_candidates = collections.Counter(list_names).keys()

#You can use the above list as the list of candidates, but for reducing the run-time,
#I recommend reducing the elements in list_canditates as much as possible.
list_candidates = [u'ムッシュかまやつ', u'綾小路翔',u'堺正章']

#Next, for every possible pair, count the number of cooccurrence:
cooccurrence = {}
for i in list_candidates:
    for j in list_candidates:
        if i!=j:
            cooccurrence[i,j] = 0
            for n in collections.Counter(list_cooccurrence).keys():
                if i in n and j in n:
                    cooccurrence[i,j] += collections.Counter(list_cooccurrence).values()[collections.Counter(list_cooccurrence).keys().index(n)]

print pp(cooccurrence)
collections
#If person A occurs mostly with person B but not with others while person B occurs with others,
#then we can infer that B is the deceased person and A comes up only in relation to B, hence eliminate A from the list.
