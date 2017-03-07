As you can see below, `twparse.py` alone can give you a pretty low error rate unless you have an unusually low standard for 'famous'. But even then, running `pairwise_coocc.py` can give the error rate close to zero.

# 0. List of all people who passed away in (or around) the time frame, according to the newspaper.
- Feb.28 饗庭孝男　(scholar of French literature)
- Mar. 1 横井茂   (choleographer)
- Mar. 1 林京子    (novelist)
- Mar. 1 ムッシュかまやつ (singer)
- Mar. 2 寺沢則忠 (former vice-president of a bank)


# 1. List of all names as a result of `twparse.py`

This list is sorted in the descending order by the number of counts.

All the names in the newspaper orbituaries appear in the list, although (u'饗庭孝男', 30) has a rather small count, 30, which is OK given his limited recognition outside of the circle of French literature academics.
Hence **Type 1 error rate = 0**.


The user can determine the threshold for 'famous', but it would safe to say if a famous person dies, he or she gets more than a couple of thousand mentions in a day. So, let's be generous and look at the entries with more than 1000 counts. 


> > print pp(  collections.Counter(list_names).most_common()  ) 


>[   (u'ムッシュかまやつ', 119955),
    (u'JP', 4036),
    (u'釜萢', 2406),
    (u'スパイダース', 2369),
    (u'かまやつひろし', 2035),
    (u'Me', 2018),
    (u'弘', 1801),
    (u'ひろし', 1476),
    (u'綾小路翔', 1235),
    (u'堺正章', 1144),
    (u'森山良子', 1081),
    (u'TERU', 1056),
    (u'いとうまい子', 1054),
    (u'林京子', 1039),]
    
- (u'ムッシュかまやつ', 119955) Correct! A famous Japanese singer who died on Mar. 1.
- (u'JP', 4036) Wrong! Irrelevant.
- (u'釜萢', 2406) Correct! Another name of 'ムッシュかまやつ'.
- (u'スパイダース', 2369) Half-correct. The name of the band 'ムッシュかまやつ' belonged to.
- (u'かまやつひろし', 2035) Correct! Another name of 'ムッシュかまやつ'.
- (u'Me', 2018) Wrong! Irrelevant.
- (u'弘', 1801) Correct! Another name of 'ムッシュかまやつ'.
- (u'ひろし', 1476) Correct! Another name of 'ムッシュかまやつ'.
- (u'綾小路翔', 1235) Wrong! A Japanese singer who made a comment on ムッシュかまやつ's death.
- (u'堺正章', 1144) Wrong! A Japanese TV show host who made a comment on ムッシュかまやつ's death.
- (u'森山良子', 1081) Wrong! A Japanese singer who made a comment on ムッシュかまやつ's death.
- (u'TERU', 1056) Wrong! A Japanese singer who made a comment on ムッシュかまやつ's death.
- (u'いとうまい子', 1054) Wrong! A Japanese actress whose brother died in a tragedy.
- (u'林京子', 1039) Correct! A Japanese author.

**Type 2 error rate = 7.5/14 = 0.53**.
Please note that this is a tough evaluation against the tool. 
Common sense is that a famous person is someone who gets more than a couple of thousand mentions when passing away. 
If we raise the threshold to 2000, then,
**Type 2 error rate = 2/6 = 0.33**.

# 2. List of all cooccurrences of names as a result of `twparse.py` #
Again, let's be generous and look at the cooccurrences of counts more than 500.

> > print pp(  collections.Counter(list_cooccurrence).most_common()  ) 


> [   ((u'ムッシュかまやつ',), 84435),
    ((), 5235),
    ((u'ムッシュかまやつ', u'JP'), 3780),
    ((u'かまやつひろし', u'ムッシュかまやつ'), 967),
    ((u'ムッシュかまやつ', u'スパイダース', u'Shiro'), 955),
    ((u'いとうまい子',), 888),
    ((u'Me', u'釜萢', u'ムッシュかまやつ', u'ひろし', u'弘'), 835),
    ((u'ムッシュかまやつ', u'スパイダース'), 818),
    ((u'Me', u'ムッシュかまやつ'), 796),
    ((u'綾小路翔', u'TERU', u'ムッシュかまやつ'), 767),
    ((u'林京子',), 752),
    ((u'V6',), 681),
    ((u'堺正章', u'ムッシュかまやつ'), 606),
    ((u'ムッシュかまやつ', u'森山良子'), 600),
    ((u'釜萢', u'ムッシュかまやつ'), 556),
   
We then immediately realize that the appearances of 'Me' almost always coincide with 'ムッシュかまやつ', since adding the counts 
(u'Me', u'釜萢', u'ムッシュかまやつ', u'ひろし', u'弘'), 835) and (u'Me', u'ムッシュかまやつ'), 796) is close to (u'Me', 2018).
The same can be said to 'JP', '綾小路翔' etc. Now we can conlude that these are not the names of the deceased, but the friends of 'ムッシュかまやつ' or random bits of URLs and such, which gives us,
**Type 2 error rate = 0**.
Below is the systematic way of making this inference.


# 3. Counts of pair-wise cooccurrences as a result of `pair_coocc.py` #
If person A occurs mostly with person B but not with others while person B occurs with others,
then we can infer that B is the deceased person and A comes up only in relation to B, hence eliminate A from the list.

> > list_candidates = [u'ムッシュかまやつ', u'綾小路翔',u'堺正章']

> > print pp(cooccurrence)

> {   (u'ムッシュかまやつ', u'堺正章'): 944,
    (u'ムッシュかまやつ', u'綾小路翔'): 873,
    (u'堺正章', u'ムッシュかまやつ'): 944,
    (u'堺正章', u'綾小路翔'): 0,
    (u'綾小路翔', u'ムッシュかまやつ'): 873,
    (u'綾小路翔', u'堺正章'): 0}





