# Twitter to CartoDB with Python

These three Python scripts (timeline2csv.py, tweet2csv.py and csv2cartodb.py) allows you to
import tweets from a certain hashtag to csv and then to CartoDB in order to visualize them.

## timeline2csv.py

This program prints and imports to a csv file the time, user, text, sentiment, question, place, 
latitude and longitude of all the tweets from a certain hashtag in real time (time line). 

## tweets2csv.py

This program prints and imports to a csv file the time, user, text, sentiment, question, place, 
latitude and longitude of all the tweets from a certain hashtag of a past event. 

## csv2cartodb.py

This program imports from a csv file the twitter information to a CartoDB dataset. It also contains
the instructions to generate a animated point data map using Torque.

### Requisites:

In order to run these programs you must download and install the following modules:

- Tweepy: https://github.com/tweepy/tweepy
- Geopy: https://github.com/geopy/geopy
- TextBlob: https://github.com/sloria/TextBlob
- CartoDB: https://github.com/CartoDB/cartodb-python

### Aknowledgements:

I would like to thanks Paisaje Transversal to give me the opportunity and support to develop this program. I also
wanted to thanks Alberto Santos and the Master GIS Programming with Python in which this project has been hosted.
Finally, many thanks to the StackOverflow community to their altruistic help.
