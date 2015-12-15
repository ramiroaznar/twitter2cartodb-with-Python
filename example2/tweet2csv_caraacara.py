#import modules
import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

import geopy
from geopy.geocoders import Nominatim
geolocator = Nominatim()

from textblob import TextBlob

#declare variables
ckey = "SyTW5RSIptIAfl9CeWorlA9QT"
csecret = "tR2o8yJVzzIfrUmJfWjXwLoVmfGAEhBXcbZniXlcjNhk4mfr2x"
atoken = "32976838-QtWFoGnGC4Mjb49I75Ef2OBkmis80dHAtdnUFGhQr"
asecret = "0C1oROu5YDVfmAtSQHKMQGFXNUeoldK4dzILiNNzUKPLm"

OAUTH_KEYS = {'consumer_key':ckey, 'consumer_secret':csecret, 'access_token_key':atoken, 'access_token_secret':asecret}
auth = tweepy.OAuthHandler(OAUTH_KEYS['consumer_key'], OAUTH_KEYS['consumer_secret'])
api = tweepy.API(auth)

#open file
print "---#CaraACara---"
saveFile = open('caraacara.csv', 'a')
headers = 'Time; User; Text; Sentiment; Candidate; Place; Latitude; Longitude;'
saveFile.write(headers + '\n')

##print tweets
for tweet in tweepy.Cursor(api.search, q ='#CaraACara', count = '100', since_id = '676506085855903744', until = '2015-12-15').items():
    '''
    Parameters (*required):
    q*: word, hashtag of interest [#CaraACara]
    geocode: returns tweets by users located within a given radius of the given latitude/longitude [37.781157,-122.398720,1km]
    lang: language [es]
    result_type: [mixed, popular or recent]
    count: [15-100]
    until: YYYY-MM-DD, 7-day limit [2015-12-5]
    since_id: returns results with an ID greater than (that is, more recent than) the specified ID [12345]
    '''
    try:
        if tweet.coordinates:
            #print "==========="
            #date & time
            moment = tweet.created_at
            #print 'Date & Time: ', moment
            #text
            string = tweet.text.replace('|', ' ')
            string = tweet.text.replace('\n', ' ')
            #print 'Text: ', string.encode('utf8')
            #user
            user = tweet.author.name.encode('utf8')
            #print 'User: ', user
            #sentiment
            text = TextBlob(string)
            if text.sentiment.polarity < 0:
                sentiment = "negative"
            elif text.sentiment.polarity == 0:
                sentiment = "neutral"
            else:
                sentiment = "positive"
            #print 'Sentiment: ', sentiment
            #candidate
            mariano = ['@marianorajoy', 'Mariano', 'Rajoy']
            pedro = ['@sanchezcastejon', 'Pedro', 'Sanchez']
            if any(x in string for x in mariano):
                if any(x in string for x in pedro):
                    candidate = "Ambos"
                else:
                    candidate = "Mariano Rajoy"
            if any(x in string for x in pedro):
                candidate = "Pedro Sanchez"
            else:
                candidate = "Ninguno"
            #print 'Candidate: ', candidate
            #location    
            place = geolocator.reverse(str(tweet.coordinates))
            #print 'Place: ', place
            latitude = tweet.coordinates[0]
            longitude = tweet.coordinates[1]
            #print 'Coords:', tweet.coordinates
            #print "==========="

            #save tweets
            saveThis = str(moment) + '; ' + str(string.encode('ascii', 'ignore')) + '; ' + user + '; ' + sentiment + '; ' + candidate + '; ' + place + '; ' + str(latitude) + '; ' + str(longitude) + '; '
            saveFile.write(saveThis + '\n')
            print "---Tweet saved---"

        if tweet.place:
            #print "==========="
            #date & time
            moment = tweet.created_at
            #print 'Date & Time: ', moment
            #text
            string = tweet.text.replace('|', ' ')
            string = tweet.text.replace('\n', ' ')
            #print 'Text: ', string.encode('utf8')
            #user
            user = tweet.author.name.encode('utf8')
            #print 'User: ', user
            #sentiment
            text = TextBlob(string)
            if text.sentiment.polarity < 0:
                sentiment = "negative"
            elif text.sentiment.polarity == 0:
                sentiment = "neutral"
            else:
                sentiment = "positive"
            #print 'Sentiment: ', sentiment
            #Candidate
            mariano = ['@marianorajoy', 'Mariano', 'Rajoy']
            pedro = ['@sanchezcastejon', 'Pedro', 'Sanchez']
            if any(x in string for x in mariano):
                if any(x in string for x in pedro):
                    candidate = "Ambos"
                else:
                    candidate = "Mariano Rajoy"
            if any(x in string for x in pedro):
                candidate = "Pedro Sanchez"
            else:
                candidate = "Ninguno"
            #print 'Candidate: ', candidate
            #location
            place = tweet.place.full_name
            #print 'Place:', place
            location = geolocator.geocode(place)
            latitude = location.latitude
            longitude = location.longitude
            #print 'Coords: ', location.latitude, location.longitude
            #print "==========="

            #save tweets
            saveThis = str(moment) + '; ' + str(string.encode('ascii', 'ignore')) + '; ' + user + '; ' + sentiment + '; ' + candidate + '; ' + place + '; ' + str(latitude) + '; ' + str(longitude) + '; '
            saveFile.write(saveThis + '\n')
            print "---Tweet saved---"
    except:
        pass
#close file
saveFile.close()
print "---The End---"
