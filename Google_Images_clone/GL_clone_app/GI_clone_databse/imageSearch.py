from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import pandas as pd
import xlsxwriter
import csv


websites = ["https://willdotboston.com/", "https://www.google.com/", "http://books.toscrape.com/", "https://pixabay.com/en/photos/?order=popular"]
#create a images array to store all images url
images = []
#Find image urls from any website
def find_images(url):
	#go to first website for scraping
	main_page_url = url
	source_code = requests.get(main_page_url)
	plain_text = source_code.text
	soup = BeautifulSoup(plain_text, "html.parser")

	#loop through DOM to find all instances of "images"
	for img in soup.findAll('img'):
		img_src = str(img.get("src"))
		alt_text = str(img.get("alt"))

		for bad_char in [',', '.', ':', '-', '(', ')', '[', ']', '=', '+', '#']:
			if bad_char in alt_text:
				alt_text = alt_text.replace(bad_char, " ")
				
		if img_src != "None":
			if "//static1" not in img_src:
				if "https" not in img_src:
					img_src = url + img_src
					images.append((img_src, alt_text))
				else:
					images.append((img_src, alt_text))
			else:
				images.append((img_src, alt_text))



def deleteFile(file_name):
	f = open(file_name, "w+")
	f.close


def store_images():
	with open ('images_urls.csv', 'a') as csvfile:
		writer = csv.writer(csvfile)

		data_num = 1
		for img, alt_text in images:
			writer.writerow([img, alt_text, data_num])
			data_num += 1

		writer.writerow(["End Data Range", data_num])

for urls in websites:
	deleteFile('images_urls.csv')
	find_images(urls)
	print(images)
	store_images()

	print("done")

#img = []
#for x in images:
#	img.append(x)
	
#print(img[1])

#for x in range(10):
#	df = pd.DataFrame({'ImageLinks': [img[x]]})
#	writer = pd.ExcelWriter('imageUrls.xlsx', engine='xlsxwriter')
#	df.to_excel(writer, sheet_name='Sheet1')

#	x += 1

#writer.save()