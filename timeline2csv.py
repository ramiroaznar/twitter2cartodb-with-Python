'''
Author: Ramiro Aznar
Web: www.ramiroaznar.com
Language: Python
Date: December 12th 2015
Code: print and save time line from a certain hashtag, all tweets are categorized
according to their sentiment, question and location if they have geo tag
Note: to speed up the code, comment print statements
'''

#import modules
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

import time

import geopy
from geopy.geocoders import Nominatim
geolocator = Nominatim()

from textblob import TextBlob

#declare variables
ckey = "CONSUMER_KEY"
csecret = "CONSUMER_SECRET"
atoken = "ACCESS_TOKEN"
asecret = "ACCESS_SECRET"

#open file
saveFile = open('timeline.csv', 'a')
headers = 'Time; User; Text; Sentiment; Question; Place; Latitude; Longitude;'
saveFile.write(headers + '\n')

class listener(StreamListener):

    def on_status(self, status):
        try:
            #print & save time, user, text, sentiment, question, place and coordinates
            if status.coordinates:
                print "==========="
                #Date & Time
                print 'Date & Time: ', status.created_at
                #User
                print 'User: ', status.user.name
                #Text
                string = status.text.replace('|', ' ')
                string = status.text.replace('\n', ' ')
                print 'Text: ', string
                #Sentiment
                text = TextBlob(string)
                if text.sentiment.polarity < 0:
                    sentiment = "negative"
                elif text.sentiment.polarity == 0:
                    sentiment = "neutral"
                else:
                    sentiment = "positive"
                print 'Sentiment: ', sentiment
                #Question
                if '?' in string:
                    question = 'Yes'
                    print 'Question: ', question
                else:
                    question = 'No'
                    print 'Question: ', question
                #Geom
                place = geolocator.reverse(str(status.coordinates))
                print 'Place: ', place
                print 'Coords:', status.coordinates
                print "==========="

                #Tweet
                tweet = str(status.user.name) + "; " + str(string.encode('utf-8')) + "; " + sentiment + "; " + question + ";" + str(place) + "; " + status.coordinates['coordinates'][1] + "; " + status.coordinates['coordinates'][2] + ";"
                saveThis = str(time.strftime("%Y-%m-%d %H:%M")) + "; " + tweet
                saveFile.write(saveThis + '\n')
                
                return True

            if status.place:
                print "==========="
                #Date & Time
                print 'Date & Time: ', status.created_at
                #User
                print 'User: ', status.user.name
                #Text
                string = status.text.replace('|', ' ')
                string = status.text.replace('\n', ' ')
                print 'Text: ', string
                #Sentiment
                text = TextBlob(string)
                if text.sentiment.polarity < 0:
                    sentiment = "negative"
                elif text.sentiment.polarity == 0:
                    sentiment = "neutral"
                else:
                    sentiment = "positive"
                print 'Sentiment: ', sentiment
                #Question
                if '?' in string:
                    question = 'Yes'
                    print 'Question: ', question
                else:
                    question = 'No'
                    print 'Question: ', question
                #Geom
                print 'Place:', status.place.full_name
                location = geolocator.geocode(status.place.full_name)
                print 'Coords: ', location.latitude, location.longitude
                print "==========="

                #Tweet
                tweet = str(status.user.name) + "; " + str(string.encode('utf-8')) + "; " + sentiment  + "; " + question + ";" + str(status.place.full_name) + "; " + str(location.latitude) + "; " + str(location.longitude) + ";"
                saveThis = str(time.strftime("%Y-%m-%d %H:%M")) + "; " + tweet
                saveFile.write(saveThis + '\n')
                
                return True
            
            else:
                print "==========="
                #Date & Time
                print 'Date & Time: ', status.created_at
                #User
                print 'User: ', status.user.name
                #Text
                string = status.text.replace('|', ' ')
                string = status.text.replace('\n', ' ')
                print 'Text: ', string
                #Sentiment
                text = TextBlob(string)
                if text.sentiment.polarity < 0:
                    sentiment = "negative"
                elif text.sentiment.polarity == 0:
                    sentiment = "neutral"
                else:
                    sentiment = "positive"
                print 'Sentiment: ', sentiment
                #Question
                if '?' in string:
                    question = 'Yes'
                    print 'Question: ', question
                else:
                    question = 'No'
                    print 'Question: ', question
                print "==========="

                #Tweet
                tweet = str(status.user.name) + "; " + str(string.encode('utf-8')) + "; " + sentiment + ";" + question + ";" + "; ; ;"
                saveThis = str(time.strftime("%Y-%m-%d %H:%M")) + "; " + tweet
                saveFile.write(saveThis + '\n')
                
                return True

        except BaseException, e:
            print 'Failed ondata, ', str(e)
            time.sleep(5)

    on_event = on_status

    def on_error(self, status):
        print status

#get access
auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

#get timeline
twitterStream = Stream(auth, listener())
twitterStream.filter(track=["#hashtag"])

#close file
saveFile.close()
