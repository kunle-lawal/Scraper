# import libraries
from urllib.request import urlopen
from bs4 import BeautifulSoup
from datetime import datetime
import csv

#specify the url
quote_page = 'https://www.brightcove.com/en/company/careers/open-positions?location=Boston'

#query the website and return the html to the variable 'page'
page = urlopen(quote_page)

#parse the html using beautiful soup and store in variable 'soup'
soup = BeautifulSoup (page, 'html.parser')

position = soup.find_all('div', attrs={'class':'careers-positions-list-title'})
location = soup.find_all('div', attrs={'class':'careers-positions-list-location'})
x = 0
data = []
for careers in location:
	positions = position[x].get_text()
	locations = location[x].get_text()

	data.append((positions, locations))
	x += 1
	#exporting to Excel CSV
	

with open ('careers.csv', 'a') as csvfile:
	writer = csv.writer(csvfile)
	for positions, locations in data:
		writer.writerow([positions, locations, datetime.now()])

"""
#open a csv file with append, so old data will not be erased

print(location_arr)

career_position_list = soup.find('div', attrs={'class':'careers-positions-list'})
sub_career_position = list(career_position_list.children)[0]
career_position = list(sub_career_position)[1]
position = list(career_position)[0]

data = career_position_list.text.strip()
print (position.get_text())

#print (data)


#exporting to Excel CSV
with open ('careers.csv', 'a') as csvfile:
	writer = csv.writer(csvfile)
	for data in 
	writer.writerow([data, datetime.now()])


#open a csv file with append, so old data will not be erased
"""


