# import libraries
from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import csv


webpage = 'https://simplisafe.com/careers#open-positions-full'
#query the website and return the html to the variable 'page'
page = requests.get(webpage).text
#parse the html using beautiful soup and store in variable 'soup'
soup = BeautifulSoup (page, 'html.parser')


position = soup.findAll("tbody", attrs={'id':"23369"})
#newpos = position[0].findAll('a')
print(position)