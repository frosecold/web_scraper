#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 17:04:46 2017

@author: franco
"""

from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time

#consumer key, consumer secret, access token, access secret.
ckey="je1LQs78Y7cAaSri9ym6yzbo2"
csecret="AjOvkFaLul2QVEHbYZIInGoIAgpdXxVNAKmTsRo85qKMoamPu2"
atoken="120909840-thbApVBzxrfyCZNB2iLBSN2AiZpMTXs6sMgImE6e"
asecret="tuAJGb79CI0tmpjlhwPcbI2FnLFWSjAy6RXaTcWJhgqVG"

class listener(StreamListener):

    def on_data(self, data):
        try:
            #print(data)
            tweet = data.split(',"text":"')[1].split('","source":')[0]
            print(tweet)
            
            saveThis = str(time.time())+'::'+tweet
            saveFile = open('twitDB.txt', 'a')
            saveFile.write(saveThis)
            saveFile.write('\n')
            saveFile.close()
            return(True)
        except BaseException as e:
            print('failed,', str(e))
            time.sleep(5)

    def on_error(self, status):
        print (status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["accident"])