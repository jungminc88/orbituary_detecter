Below is the summary for how I approached the problem and answers to the main questions.

# 1. Summary of the data #
- Data Size
  - 121478
- Time Frame
  - From 'Wed Mar 01 03:15:41 +0000 2017' to 'Thu Mar 02 03:43:14 +0000 2017' Japan Time
- Details
  - Details of the data can be found in `details_data`

# 2. Summary of the approach #

- What are the (online and publicly accessible) sources the tool is using?
  - This tool draws data from Twitter API.
  - To extract person names from tweets, I used [mecab-ipadic-NEologd](https://github.com/neologd/mecab-ipadic-neologd/wiki/Home)
  

- How would you define and quantify 'famous'?
  - In this tool, it is measured by the number of times the name appears in the tweet data.
  - The user can determine the minimum number of counts to be deemed 'famous'.
  
