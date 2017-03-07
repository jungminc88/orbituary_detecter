Detects when a famous person dies using Twitter data. This is a part of the application for intership at GumGum.
This tool draws tweets 

# 1. Preparation: Access Twitter API and MongoDB #

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
# 2.  Obtain Tweets #
Run `<gettweet.py>`
This gets the tweets that contains the word "死去"("death" or "die") and saves them into `<db.tweetdata>`.

# 3. Make lists #
Run `<twparse.py>`
This code parses each tweet, extracts person names, and make a list of person names that appear in the data, as well as a list of cooccurrences, both with counts.

# 4. Test #
The list is expected to contain all the names of notable people who died in the period (low Type 1 error).
However, it does contain a lot of names of who are not dead (or non-person names like band names).
To reduce the wrong names from the list, run `<cooccurrence>` after setting list_candidates.




