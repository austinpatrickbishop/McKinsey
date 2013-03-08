#!/usr/bin/env python
#Austin Bishop 03/05/2013
import re
import sys
import urllib
import simplejson

def searchTweets(query):
 query = parseArgs(query)
 search = urllib.urlopen("http://search.twitter.com/search.json?q=%23"+query+"&rpp=100")
 dict = simplejson.loads(search.read())
 L = []
 for result in dict["results"]: # result is a list of dictionaries
  URLs = re.findall(r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+", result["text"])
  for x in range(0,len(URLs)):
   addToList(L,URLs[x])
 print("\n".join(L))

def addToList(self, str_to_add):
 if str_to_add not in self:
  self.append(str_to_add)

def parseArgs(theArg):
 if(len(theArg)<2):
  result = ""
  print("\nPlease enter a hashtag (without the # sign)")
  sys.exit(0)
 elif(len(theArg)>2):
  result = theArg[1]
  print("\nNo spaces allowed. Searching for #"+theArg[1])
  print("URLs in the most recent tweets containing the hashtag #"+theArg[1])
 else:
  result = theArg[1]
  print("\nURLs in the most recent tweets containing the hashtag #"+theArg[1])
 return(result)
searchTweets(sys.argv)
