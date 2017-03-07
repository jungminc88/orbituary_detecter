#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# Modified from a code by kenmatsu4: http://qiita.com/kenmatsu4/items/23768cbe32fe381d54a2 .

from requests_oauthlib import OAuth1Session
from requests.exceptions import ConnectionError, ReadTimeout, SSLError
import json, datetime, time, pytz, re, sys,traceback, pymongo
#from pymongo import Connection     # Connection classは廃止されたのでMongoClientに変更 
from pymongo import MongoClient
from collections import defaultdict
import numpy as np


#Give your account information for accessing Twitter API

KEYS = { 
        'consumer_key':'',
        'consumer_secret':'',
        'access_token':'',
        'access_secret':'',
       }

twitter = None
connect = None
db      = None
tweetdata = None
meta    = None

def initialize(): # Initialize access information for Twitter and MongoDB.
    global twitter, twitter, connect, db, tweetdata, meta
    twitter = OAuth1Session(KEYS['consumer_key'],KEYS['consumer_secret'],
                            KEYS['access_token'],KEYS['access_secret'])

    connect = MongoClient('localhost', 27017)
    db = connect.orbituary
    tweetdata = db.tweetdata
    meta = db.metadata

initialize()



# Put the search word "死去" and obtain the tweet data.
def getTweetData(search_word, max_id, since_id):
    global twitter
    url = 'https://api.twitter.com/1.1/search/tweets.json'
    params = {'q': search_word,
              'count':'100',
    }
    # max_id can be set (get tweets before max_id)
    if max_id != -1:
        params['max_id'] = max_id
    # since_id can be set (get tweets since since_id)
    if since_id != -1:
        params['since_id'] = since_id

    req = twitter.get(url, params = params)   # Obtain tweets

    # Breaking down the information
    if req.status_code == 200: # If success
        timeline = json.loads(req.text)
        metadata = timeline['search_metadata']
        statuses = timeline['statuses']
        limit = req.headers['x-rate-limit-remaining'] if 'x-rate-limit-remaining' in req.headers else 0
        reset = req.headers['x-rate-limit-reset'] if 'x-rate-limit-reset' in req.headers else 0              
        return {"result":True, "metadata":metadata, "statuses":statuses, "limit":limit, "reset_time":datetime.datetime.fromtimestamp(float(reset)), "reset_time_unix":reset}
    else: # If fail
        print ("Error: %d" % req.status_code)
        return{"result":False, "status_code":req.status_code}

# Returns the Japan Time at the time when the tweet was made
def str_to_date_jp(str_date):
    dts = datetime.datetime.strptime(str_date,'%a %b %d %H:%M:%S +0000 %Y')
    return pytz.utc.localize(dts).astimezone(pytz.timezone('Asia/Tokyo'))

# Return the time now (Unix)
def now_unix_time():
    return time.mktime(datetime.datetime.now().timetuple())



#-------------Obtain tweet data repeatedly-------------#
sid= -1
mid = -1
count = 0

res = None
while(True):    
    try:
        count = count + 1
        sys.stdout.write("%d, "% count)
        res = getTweetData(u'死去', max_id=mid, since_id=sid)
        if res['result']==False:
            # If fail, break
            print "status_code", res['status_code']
            break

        if int(res['limit']) == 0:    # Access limit. Halt.
            # Add 'created_datetime'
            print "Adding created_at field."
            for d in tweetdata.find({'created_datetime':{ "$exists": False }},{'_id':1, 'created_at':1}):
                #print str_to_date_jp(d['created_at'])
                tweetdata.update({'_id' : d['_id']}, 
                     {'$set' : {'created_datetime' : str_to_date_jp(d['created_at'])}})
            #remove_duplicates()

            # Compute wait time
            diff_sec = int(res['reset_time_unix']) - now_unix_time()
            print "sleep %d sec." % (diff_sec+5)
            if diff_sec > 0:
                time.sleep(diff_sec + 5)
        else:
            # metadata processing
            if len(res['statuses'])==0:
                sys.stdout.write("statuses is none. ")
            elif 'next_results' in res['metadata']:
                # Store the result to MongoDB
                meta.insert({"metadata":res['metadata'], "insert_date": now_unix_time()})
                for s in res['statuses']:
                    tweetdata.insert(s)
                next_url = res['metadata']['next_results']
                pattern = r".*max_id=([0-9]*)\&.*"
                ite = re.finditer(pattern, next_url)
                for i in ite:
                    mid = i.group(1)
                    break
            else:
                sys.stdout.write("next is none. finished.")
                break
    except SSLError as (errno, request):
        print "SSLError({0}): {1}".format(errno, strerror)
        print "waiting 5mins"
        time.sleep(5*60)
    except ConnectionError as (errno, request):
        print "ConnectionError({0}): {1}".format(errno, strerror)
        print "waiting 5mins"
        time.sleep(5*60)
    except ReadTimeout as (errno, request):
        print "ReadTimeout({0}): {1}".format(errno, strerror)
        print "waiting 5mins"
        time.sleep(5*60)
    except:
        print "Unexpected error:", sys.exc_info()[0]
        traceback.format_exc(sys.exc_info()[2])
        raise
    finally:
        info = sys.exc_info()
