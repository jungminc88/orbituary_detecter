#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 19:40:37 2017

@author: min
"""
import collections
import numpy as np
ln = collections.Counter(list_names).keys()
lc = collections.Counter(list_cooccurrence).keys()

import collections

list_candidates = [u'ムッシュかまやつ', u'綾小路翔',u'堺正章']
cooccurrence = {}
for i in list_candidates:
    for j in list_candidates:
        if i!=j:
            cooccurrence[i,j] = 0
            for n in collections.Counter(list_cooccurrence).keys():
                if i in n and j in n:
                    cooccurrence[i,j] += collections.Counter(list_cooccurrence).values()[collections.Counter(list_cooccurrence).keys().index(n)]
                
