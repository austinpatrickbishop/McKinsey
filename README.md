# README.md
### Austin Bishop, Copywrite 2013

##

`./sorter.py`

>>This function recieves an array (I used a list in python) of 10000 integers, ranging in value from 0 to 20 and then
sorts them by frequenecy of occurance, from most frequent to least frequent.


`./searchHash.py arg`

>>`arg` should be a string that begins with a letter, and contains no special characters.
This function will find the 100 most recent tweets that contain the hashtag #arg. It then
finds all URLs that are mentioned in the tweets, and prints only unique copies.

>>This function handles incorrect argument passing.
It is important to note that this current version, the 100 most recent tweets may include retweets.

The regular expression used to detect URLs has never failed in testing, but this is more due to Twitter's
regularization of URLs rather than innate robustness of the regex.

