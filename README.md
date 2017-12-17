# Spatial-and-Textual-searching-on-MongoDB

Implemented two functions, which will perform some textual and spatial searching on MongoDB.

**FindBusinessBasedOnCity(cityToSearch, saveLocation1, collection)**

  This function searches the ‘collection’ given to find all the business present in the city provided in ‘cityToSearch’ and     save it to ‘saveLocation1’. For each business you found, you should store name Full address, city, state of business in the   following format.
  
  Each line of the saved file will contain, Name$FullAddress$City$State. ($ is the separator and must be present)

**FindBusinessBasedOnLocation(categoriesToSearch, myLocation, maxDistance, saveLocation2, collection)**

  This function searches the ‘collection’ given to find name of all the business present in the ‘maxDistance’ from the given     ‘myLocation’ (please use the distance algorithm given below) and save them to ‘saveLocation2’.
  
  Each line of the output file will contain the name of the business only.
  
# testData.json  
**This is the json file which is used as a document to put inside MongoDb. The structure of one record of this file is < Key value pair>: -**

{
'type': 'business',
'business_id': (encrypted business id), 'name': (business name), 'neighborhoods': [(hood names)], 'full_address': (localized address),
'city': (city),
'state': (state),
'latitude': latitude,
'longitude': longitude,
'stars': (star rating, rounded to half-stars), 'review_count': review count,
1
 
'categories': [(localized category names)]
'open': True / False (corresponds to permanently closed, not business hours), }

**Example:**

{"city": "Ahwatukee",
"review_count": 3,
"name": "McDonald's",
"neighborhoods": [],
"type": "business",
"business_id": "LNdwp-9Isnd6xmBKUz4K_A", "full_address": "10823 S 51st St\nAhwatukee, AZ 85044", "state": "AZ",
"longitude": -111.975004, "stars": 2.0,
"latitude": 33.348560900000003, "open": true,
"categories": ["Burgers", "Fast Food", "Restaurants"]}

Note: - The order of key value pair does not matter.
