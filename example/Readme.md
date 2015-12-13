# Example

Using *tweet2csv.py* and *csv2cartodb.py* to generate a animated point data map about the #AccordDeParis.

## tweet2csv.py

I used *tweet2csv.py* with the following modifications:

- all the print statements except the new "Print '---Tweet saved---' were commented to speed up the program,
- a "try/except pass" loop was added to avoid UnicodeDecodeErrors,
- the api search cursor parameters were q = '#AccordDeParis', since_id = '675745969141600256'* and count = '100'.

*Id of the @COP21 [tweet](https://twitter.com/COP21/status/675745969141600256) announcing the Paris Agreement. 

## csv2cartodb.py
