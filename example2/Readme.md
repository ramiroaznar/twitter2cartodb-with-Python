# Example2

Using *tweet2csv.py* and *csv2cartodb.py* to generate a animated point data map about the Spanish debate
between president Mariano Rajoy and Pedro Sánchez, related to the hashtag #CaraACara.

## tweet2csv.py

I used *tweet2csv.py* with the following modifications:

- all the print statements were commented to speed up the program,
- a "try/except pass" loop was added to avoid UnicodeDecodeErrors,
- the api search cursor parameters were q = '#CaraACara', since_id = '676506085855903744'* and count = '200'.

*Id of the @el_pais [tweet](https://twitter.com/el_pais/status/676506085855903744) showing the start of the debate. 

## csv2cartodb.py

No modifcations were added to this script.

## Torque Cat

After importing the *caraacara.csv* file to CartoDB, the dataset was slightly edited. Rows with values different
from "Pedro Sanchez" and "Mariano Rajoy" within the candidate column were removed using the
filter tool. The new dataset created from this query was saved. Finally, a Torque Cat map was generated using the 
candidate column as the Category Column. 

The resulting map can be seen [here](http://bit.ly/1RLi7Fm), also a screen shot (*map.png*) has been added to this repository.

### Final thoughts

UnicodeDecodeErrors continue to appear. This was avoided using "Try/Except" loops and 'ignore' arguments. A better solution
will be needed in the future.
