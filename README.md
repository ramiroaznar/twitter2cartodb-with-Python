# Twitter to CartoDB with Python

These three Python scripts (*timeline2csv.py*, *tweet2csv.py* and *csv2cartodb.py*) allows you to
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

## example

Folder file containing:
- readme.md,
- tweets2csv.py modified,
- csv2cartodb.py,
- and map.png.

### Requisites:

First, it is necessary to get your Twitter and CartoDB APIs from the following links:
- Twitter: https://apps.twitter.com/
- CartoDB: http://docs.cartodb.com/cartodb-platform/sql-api/authentication/

In addition, in order to run these programs you must download and install the following modules:

- Tweepy: https://github.com/tweepy/tweepy
- Geopy: https://github.com/geopy/geopy
- TextBlob: https://github.com/sloria/TextBlob
- CartoDB: https://github.com/CartoDB/cartodb-python

### Aknowledgements:

I would like to thanks [Paisaje Transversal](http://www.paisajetransversal.org/) to give me the opportunity and support to develop this program. I also wanted to thanks **Alberto Santos** and the [Master GIS Programming with Python](http://geospatialtraininges.com/cursos-gis/master-programacion-gis-con-python/) in which this project has been hosted.
Finally, many thanks to the **Stack Overflow** community to their altruistic help.
