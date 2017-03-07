Detects when a famous person dies using Twitter data. This is a part of the application for intership at GumGum.
This tool draws tweets 

# 1. Preparation: Access Twitter API and MongoDB #
## 1.1 Obtain a Twitter API account and note your consumer_key, consumer_secret, access_token, and access_secret ##
    Follow the instruction at
    https://dev.twitter.com/ .
    
## 1.2 Install the authorization library ##
Here, we use [Requests-OAuthlib](https://requests-oauthlib.readthedocs.io/en/latest/).
    
  ```sh
      pip install requests_oauthlib
  ```
## 1.3 Install MongoDB and pymongo ##
We use MongoDB to save the data.
    [MongoDB install manual](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-os-x/)
    In order to access MongoDB from python, we need pymongo:
    ```sh
    pip install pymongo
    ```
# 2.  
