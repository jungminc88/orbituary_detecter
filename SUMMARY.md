#  Summary of the approach #

- What are the (online and publicly accessible) sources the tool is using?
  - This tool draws data from Twitter API.
  
- How does your tool identify its target strings?
  - To extract person names from tweets, I used [mecab-ipadic-NEologd](https://github.com/neologd/mecab-ipadic-neologd/wiki/Home). As shown in `RESULT.dm`, this dictionary detects famous names as well as strings that are likely to be Japanese names, seemingly at a 100% rate.
  
- How would you define and quantify 'famous'?
  - In this tool, it is measured by the number of times the name appears in the tweet data.
  - The user can determine the minimum number of counts to be deemed 'famous'.
  
- How do you measure your tool's performance?
  - I check it against the orbituaries of [Asahi Shimbun (Japanese newpaper site)](http://www.asahi.com/obituaries/).
  - I measure the tool's performance by the rate of Type 1 errors (missing the correct names) and Type 2 errors (including wrong names) as follows:
    - Type 1 error rate = (number of missing correct names in the returned list) / (number of correct names)
    - Type 2 error rate = (number of wrong names in the returned list) / (length of the returned list)
  - As shown in `RESULTS.dm`, Type 1 error rate is close to zero. Type 2 error rate is also low with usual standard for 'famous'. Even if the user chooses a very broad standard for 'famous', after eliminating names that are likely to be wrong using `finetune.py`, Type 2 error is close to zero.
