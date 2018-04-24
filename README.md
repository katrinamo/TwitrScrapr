# TwitrScrapr
A twitter scraper that searches for tweets with certain keywords.

Powered by tweepy!


## TO USE:
1. Gather tweets by first doing ```python searcher.py```

This will then prompt for search terms. The output file will be your
specified terms + Tweets.txt. For example this may looke like 
MeTooTweets.txt.

2. Use frequency counter to find most common terms 
```./frequency_counter <FILENAME>```

The terms and their frequency sorted from most to least used is output
in sorted.txt.

3. Use gender.py to determine the gender breakdown of the tweets 
```python gender.py <FILENAME>```

This will output the gender of each tweet line by line in a file named
<FILENAME>GenderBreakdown.txt.
