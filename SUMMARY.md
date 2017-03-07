Below is the summary for how I approached the problem and answers to the main questions.

# 1. Summary of the data #
- Data Size
  - 121478 tweets
- Time Frame
  - From 'Wed Mar 01 03:15:41 +0000 2017' to 'Thu Mar 02 03:43:14 +0000 2017' Japan Time
- Details
  - Details of the data can be found in `DEMO.md`

# 2. Summary of the approach #

- What are the (online and publicly accessible) sources the tool is using?
  - This tool draws data from Twitter API.
  
- How does your tool identify its target strings?
  - To extract person names from tweets, I used [mecab-ipadic-NEologd](https://github.com/neologd/mecab-ipadic-neologd/wiki/Home).
  
- How would you define and quantify 'famous'?
  - In this tool, it is measured by the number of times the name appears in the tweet data.
  - The user can determine the minimum number of counts to be deemed 'famous'.
  
- How do you measure your tool's performance?
  - I check it against the orbituaries of [Asahi Shimbun (Japanese newpaper site)](http://www.asahi.com/obituaries/).
  - I measure the tool's performance by the rate of Type 1 errors (missing the correct names) and Type 2 errors (including wrong names) as follows:
    - Type 1 error rate = (number of missing correct names in the returned list) / (number of correct names)
    - Type 2 error rate = (number of wrong names in the returned list) / (length of the returned list)
  - With the above data from Mar 1, the Type 1 error rate was 0, while the Type 2 error rate was large.
  - The cause of the Type 2 errors are:
    - a) The problem in the dictionary; The dictionary contains band names and group names, and also label them as person name, hencee wrongly recognizes bits of URLs or other strings such as "JP" and "Me" as a person name. You might want to eliminate these short names consisting only of alphabets and numerals, but they may well be genuine person names, so there seems to be no easy way to solve this problem.
      - I also tried to make a dictionary by scraping article pages of Wikipedia under the catergory "Japanese people", but this category also contains band and group names. 
    - b) When a famous person makes comments on the deceased person, that person's name will also come up a lot in the data.
  - To deal with the problem (b), this tool contains a pairwise cooccurrence counter. After you remove the non person names and irrelevant names as much as possible, you count the pairwise cooccurrences of the names is the list. If a name A occur almost exclusively with another name B, you can assume that A only appears in relation to the deceased person B and A is not deceased.
