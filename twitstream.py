# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 17:21:08 2019

@author: NMuppala
"""

import tweepy
consumer_key = "TnhzzruWDWnQbWGJM3c2hKMio"
consumer_secret = "SVLbIbw2ZdNAwcqWg0EanP5P6JW7xG6LS2VU6mv02dMuGTxJgy"
access_token = "365327162-G0w2QNVyaMSOdwGt71acRhDP8WpkwPSx2op8iFvF"
access_token_secret = "hO6sspgzy2KF3pjiXr8Pa1ehsgZb0P4D98x8kCPaIjm91"


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# Setting your access token and secret
auth.set_access_token(access_token, access_token_secret)
# Creating the API object while passing in auth information
api = tweepy.API(auth)

twit = api.search("IPL")

for tweet in twit:
   print(twit)       
    
#with open("follwers.txt","w+") as f:
#    f.write(twit.)
    
stk = open("follwers.txt","r")
r=stk.read()
print(r) 
print("end of program")
print("trying to get it right this time")