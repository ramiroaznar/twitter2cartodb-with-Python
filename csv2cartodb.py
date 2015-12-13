'''
Author: Ramiro Aznar
Web: www.ramiroaznar.com
Language: Python
Date: December 12th 2015
Code: import csv files (timeline.csv and/or tweets.csv) from previous scripts to CartoDB
Note: see below to know how to create an animated or torque map with the imported data
'''

#Import modules
from cartodb import CartoDBAPIKey, CartoDBException, FileImport

#api configuration
API_KEY ='API_KEY'
cartodb_domain = 'USER_DOMAIN'
cl = CartoDBAPIKey(API_KEY, cartodb_domain)
 
#import csvs
fi = FileImport("C://timeline.csv", cl)
#fi = FileImport("C://tweets.csv", cl) comment last line, and uncomment this to use the code
fi.run()

'''
How to create animated map with point data using Torque in CartoDB*:

Torque is a visualization that allows you to visualize geographic data over time. You can access 
it just like you would other Visualization Wizards, from the pull-out tray on the right of your 
screen, under the Visualization Wizard.

Once you select Torque, you’ll notice that the column that CartoDB picked to visualize is the cartodbid 
column. This column is just an arbitrarily assigned ID number that CartoDB uses and assigns based on the 
order of the data in your spreadsheet. In terms of mapping, it’s usually fairly meaningless, so you will 
want to change it to something more meaningful, as it’s just the order that the data is in in the table. 
We should go ahead and select the column labeled date [note: change your column Time data type from 
string to date in your dataset view] since that makes the most sense here.

As with the other visualizations, you can change the stroke and fill of the markers. In our demo, we brought 
the opacity down, and played with the color until we were happy with it. We also removed the marker stroke, 
but you can change things as you see fit.

There are new parameters in the Torque visualization as well. Steps is the number of bins that the data is 
broken up in to when it’s visualized. In future lessons, we’ll talk about CartoCSS, which gives you more control 
over steps than the current presets included in the wizard.

You can also change the duration of the visualization, which changes the length of the entire animation from 
beginning to end.

Finally, you can change the trails setting for your visualization. These are the burst effects that happen after 
the point first appears, and leave a visual “trail” after the point disappears.

In the standard Torque visualization, data points disappear after they appear on the map. If you switch the “cumulative” 
toggle on, points will stay on the map, and build upon each other. Often, it’s best to bring down the opacity of your 
markers when you’re using the cumulative visualization so that the effect of points layering over one another is noticable.

Ultimately, it’s up to you when to use the cumulative function, and when to allow your points to disappear. When you are 
highlighting accumulation or intensity over time, the cumulative function may be very helpful. Other times, it may not 
make sense with your data.

*Info estracted from CartoDB's Map Academy: http://academy.cartodb.com/courses/beginners-course/animated-maps-with-point-data/
'''
