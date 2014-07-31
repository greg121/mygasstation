import mechanize
from urllib import urlencode
from pygeocoder import Geocoder
import sys
from xml.dom import minidom

#retrieve lat&lng from city name from command line args
results = Geocoder.geocode(sys.argv[1])

lat = results[0].coordinates[0]
lng = results[0].coordinates[1]

opener = mechanize.build_opener()
data = {"lat":str(lat),"lng":str(lng),"radius":"3","fuels":sys.argv[2]}
d = urlencode(data)
url = 'http://tanken.t-online.de/api/v1/search.xml'
stuff = opener.open(url,d)
xml = stuff.read()

with open("temp/output.xml", "w") as text_file:
    text_file.write(xml)

xmldoc = minidom.parse('temp/output.xml')

names = list()
streets = list()
prices = list()

itemlist = xmldoc.getElementsByTagName('gasStation')
for s in itemlist :
    names.append(s.attributes['name'].value)
    streets.append(s.attributes['street'].value)

itemlist2 = xmldoc.getElementsByTagName('fuel')
for s in itemlist2:
    prices.append(s.attributes['price'].value)

for i in range(0,len(names)):
    print names[i] + ": " + prices[i] + " " + "(" + streets[i] + ")"
