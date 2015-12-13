#Import modules
from cartodb import CartoDBAPIKey, CartoDBException, FileImport

#Api config
API_KEY ='API_KEY'
cartodb_domain = 'USER_NAME'
cl = CartoDBAPIKey(API_KEY, cartodb_domain)
 
#Import csv
fi = FileImport("C:/...", cl)
fi.run()
