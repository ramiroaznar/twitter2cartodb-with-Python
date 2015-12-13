# Example

Using *tweet2csv.py* and *csv2cartodb.py* to generate a animated point data map about the #AccordDeParis.

## tweet2csv.py

I used *tweet2csv.py* with the following modifications:

- all the print statements except the new "Print '---Tweet saved---'" were commented to speed up the program,
- a "try/except pass" loop was added to avoid UnicodeDecodeErrors,
- the api search cursor parameters were q = '#AccordDeParis', since_id = '675745969141600256'* and count = '100'.

*Id of the @COP21 [tweet](https://twitter.com/COP21/status/675745969141600256) announcing the Paris Agreement. 

## csv2cartodb.py

No modifcations were added to this script.

## Torque Cat

After importing the *AccordDeParis.csv* file to CartoDB, the dataset was slightly edited. Rows with values different
from "Negative", "Neutral" and "Positive" within the sentiment column were removed using the filter tool. The new 
dataset created from this query was saved. Finally, a Torque Cat map was generated using the sentiment column as the
Category Column. 

The resulting map can be seen [here](http://bit.ly/1RLi7Fm), also a screen shot (*map.png*) has been added to this repository.

### Final thoughts

UnicodeDecodeErrors continue to appear. This was avoided using "Try/Except" loops and 'ignore' arguments. A better solution
will be needed in the future. 
