# import libraries

#Imports for PyQt
import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl	
from PyQt5.QtWebEngineWidgets import QWebEnginePage

#Imports for beautiful Soup
from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup

#Imports for Excel Datasets
from datetime import datetime
import csv


#Class to contain site specific parsing. 

class lookUpHtml:
	def __init__(self, level1, attr1, level2, attr2, level3, attr3):
		self.jobContainerClass = jobContainerClass
		self.jobContainerElement = jobContainerElement
		self.jobClass = jobClass
		self.jobElement = jobElement


class Client(QWebEnginePage):

	def __init__(self, url):
		self.app = QApplication(sys.argv)
		QWebEnginePage.__init__(self)
		self.loadFinished.connect(self.on_page_load)
		self.load(QUrl(url))
		self.app.exec_()

	#Quit application after load
	def on_page_load(self):
		self.html = self.toHtml(self.Callable)
		print('Load finished')

	def Callable(self, html_str):
		self.html = html_str
		self.app.quit()


#bookbub = ParseCode('jv-job-list', 'table', 'jv-job-list-name', 'td')
#specify the url
#webpage = 'https://simplisafe.com/careers#open-positions-full'
#query the website and return the html to the variable 'page'
#page = requests.get(webpage).text
#parse the html using beautiful soup and store in variable 'soup'
#soup = BeautifulSoup (page, 'html.parser')

url = 'https://carbonite.taleo.net/careersection/ex/jobsearch.ftl?lang=en&portal=101430233'
client_response = Client(url)
source = client_response.html
soup = BeautifulSoup (source, 'html.parser')
#print(soup)
#Get Job URLS from Site# Path

MainContainer = soup.findAll("table", attrs={'id':'jobs'})

print(MainContainer)

for sub in MainContainer:
	subContainer = sub.findAll('tbody')
	for jobs in subContainer:
		theJobs = jobs.findAll('tr')
		for jobInfo in theJobs:
			jobInfo1 = jobInfo.findAll('th')
			print(jobInfo)

'''
for jobContainer in MainContainer:
	body = jobContainer.findAll('tbody')

	for job in body:
		tr = job.findAll('tr')
		for urls in tr:
			jobUrl = urls.get('data-href')
			print(str(jobUrl))

'''

'''
table = soup.findAll("table", attrs={'id':"open-positions"})

for mytable in table:
	table_body = mytable.findAll('tbody')

	for tr in table_body:
		row = tr.findAll('tr')
		for td in row:
			col = td.findAll('td')
			department = col[0]
			job = col[1]

			print(job.get_text())

rows = table_body.find('tr')
				for tr in rows:
					cols = tr.findAll('td')
					print(tr.text)'''



#position = soup.findAll(bookbub.jobElement, attrs={'class':bookbub.jobClass})
#newpos = position[0].findAll('a')
#print(position)

#location = soup.find_all('div', attrs={'class':'careers-positions-list-location'})








'''
position = soup.findAll('p', attrs={'class':'job'})
location = soup.find_all('div', attrs={'class':'careers-positions-list-location'})
x = 0
data = []
for careers in position:
	positions = position[x].get_text()
	print(positions)
	#locations = location[x].get_text()

	#data.append((positions, locations))
	x += 1
	#exporting to Excel CSV
	

with open ('careers.csv', 'a') as csvfile:
	writer = csv.writer(csvfile)
	for positions, locations in data:
		writer.writerow([positions, locations, datetime.now()])
'''



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