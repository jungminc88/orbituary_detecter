Detects when a famous person passes away using Twitter data. This page explains how to run this tool.
For the demonstration of this tool, see `RESULTS.dm`. For the summary of the approach, see `SUMMARY.dm`.


# 1. Preparation #
If you would rather use the existing json data that I provide than to obtain data first hand, you can skip 1.1 through 1.3.

## 1.1 Obtain a Twitter API account and note your consumer_key, consumer_secret, access_token, and access_secret ##
Follow the instruction at
https://dev.twitter.com/ .
    
## 1.2 Install the authorization library ##
Here, we use [Requests-OAuthlib](https://requests-oauthlib.readthedocs.io/en/latest/).
    
```
pip install requests_oauthlib
```
## 1.3 Install MongoDB and pymongo ##
We use MongoDB to save the data([install manual](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-os-x/)).

In order to access MongoDB from python, we need pymongo:
 ```
 pip install pymongo
 ```
 
## 1.4 Install Mecab and mecab-ipadic-NEologd ##
- [Install Mecab](http://taku910.github.io/mecab/)
- [Install mecab-ipadic-NEologd (Neologism dictionary for MeCab)](https://github.com/neologd/mecab-ipadic-neologd)


# 2.  Obtain tweets #
Run `gettweets.py`
This gets the tweets that contains the word "死去"("death" or "die") and saves them into `db.tweetdata`.
This is modified from a [code](http://qiita.com/kenmatsu4/items/23768cbe32fe381d54a2) written by [kenmatsu4](http://qiita.com/kenmatsu4/items/23768cbe32fe381d54a2).

# 3. Make lists #
Run `makelists.py`
This code parses each tweet, extracts person names, and make a list of person names that appear in the data, as well as a list of cooccurrences, both with counts. The former is a list of candidates for correct names whereas the latter can help narrow down the candidate list.


# 4. Fine-tuning lists #
The list is expected to contain all the names of notable people who died in the period. (very small risk of Type 1 error)
However, it does contain a lot of names of who are not dead (or non-person names like band names). (large risk of Type 2 error)
To reduce the wrong names from the list, run `finetune.py`




