#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 01:15:06 2017

@author: min
"""

from pymongo import MongoClient
import collections


import MeCab as mc
import sys 
import unicodedata
reload(sys)  
import re, pprint


#print unicode chars
def pp(obj):
     pp = pprint.PrettyPrinter(indent=4, width=160)
     str = pp.pformat(obj)
     return re.sub(r"\\u([0-9a-f]{4})", lambda x: unichr(int("0x"+x.group(1),16)), str)


#obtain person names from a string
def getPersonNames(sentence):
    t = mc.Tagger('-Ochasen -d /usr/local/lib/mecab/dic/mecab-ipadic-neologd')
    sentence = sentence.replace('\n', ' ')
    text = sentence.encode('utf-8') 
    node = t.parseToNode(text) 
    person_names = []
    for i in range(140):  # a tweet has at maximum 140 chars
        if node.surface != "":  # excluding header and footer
            if node.feature.split(",")[6] in ["さん","氏"]:#stopwords
                node = node.next
            else:
                word_type = node.feature.split(",")[2]
                if  word_type == "人名": #the word type is person name
                    person_name = node.feature.split(",")[6]
                    person_names.append(person_name.decode('utf-8'))
                
        node = node.next
        if node is None:
            break
    return person_names #returns a list of all person names in the sentence


#import data from MongoDB
connect = MongoClient('localhost', 27017)
db = connect.orbituary
tweetdata = db.tweetdata
meta = db.metadata


#make a list of all names in the and a list of all cooccurrences in the data
list_names = []
list_cooccurrence = []
for d in tweetdata.find({},{'text':1}):
    res = getPersonNames(unicodedata.normalize('NFKC', d['text'])) # Convert half-width chars to full-width
    list_names.extend(res)
    res2 = tuple(set(res))
    list_cooccurrence.append(res2)

print pp(  collections.Counter(list_names).most_common()  ) #List of all names that appear in the data.
print pp(  collections.Counter(list_cooccurrence).most_common()  )#List of all cooccurrences of names.
