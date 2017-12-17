
from pymongo import MongoClient
import os
import sys
import json
import re
import codecs
import math

# calculated the dsitance from the given formula
def DistanceFunction(lat2, long2, lat1, long1):
   R=3959;
   phi2 = math.radians(lat2)
   phi1 = math.radians(lat1)
   latDelta = math.radians(lat2-lat1);
   longDelta = math.radians(long2-long1);
   
   a = math.sin(latDelta/2) * math.sin(latDelta/2) + math.cos(phi2) * math.cos(phi1) * math.sin(longDelta/2) * math.sin(longDelta/2); 
   c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a));
   d = R * c;
   return d;


def FindBusinessBasedOnCity(cityToSearch, saveLocation1, collection):
    f =open(saveLocation1, 'w')				# opening saved location 1
    entries = set()	
    for i in collection.find({'city':cityToSearch.capitalize()}):	# city search
	string_value = i['name']+"$"+i['full_address'].replace('\n',' ')+"$"+i['city']+"$"+i['state']  # Name$FullAddress$City$State.
	entries.add(string_value)				# adding the found values
    for val in entries:
	f.write(val.upper().encode('utf-8')+"\n")	# writing the output file
    f.close()
    
    
def FindBusinessBasedOnLocation(categoriesToSearch, myLocation, maxDistance, saveLocation2, collection):
	f = open(saveLocation2, 'w')
	entries = {}
	# check the distance function for all elements in categories to search  adn stores the result
	for i in collection.find():
		if all(x in i['categories'] for x in categoriesToSearch):
			if DistanceFunction(float(i['latitude']), float(i['longitude']), float(myLocation[0]), float(myLocation[1])) <= maxDistance:
				entries[i['name'] + "=" + str(i['latitude']) + "$" + str(i['longitude'])] = i['name']

	for key,val in entries.items():
		f.write(val.upper().encode('utf-8')+"\n")	# saved in location 2
	f.close()
