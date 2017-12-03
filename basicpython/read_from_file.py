import geopy
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt


print mpl_toolkits.basemap

world = Basemap()
cities, years = [], []

# for each line in the text file
for game in open('games.txt','r'):
	# split the current line at the spaces
	words = game.split()
	
	# Join strings except the last item
	city = ' '.join(words[:-1])
	
	# Strip the parentheses from the last string
	year = words[-1].strip('()')
	
	cities.append(city)
	years.append(year)

geolocator = geopy.geocoders.Nominatim()
locations = {}
for city in cities:
	print "Locating " + city
	locations[city] = geolocator.geocode(city.split('/')[0])
	
plt.Figure(figsize = (10, 5))
world = Basemap()
world.drawcoastlines( linewidth = 0.25 )
world.drawcountries( linewidth = 0.25)

