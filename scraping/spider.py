from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup

def trade_spider(max_pages):
	page = 1
	while page <= max_pages:
		main_page_url = "http://books.toscrape.com/"
		source_code = requests.get(main_page_url)
		plain_text = source_code.text
		soup = BeautifulSoup(plain_text, "html.parser")
		for h3 in soup.findAll('h3'):
			for link in h3.findAll('a'):
				title = link.get("title")
				book_url = main_page_url + link.get('href')
				get_single_item_data(book_url)
		page += 1

def get_single_item_data(item_url):
	source_code = requests.get(item_url)
	plain_text = source_code.text
	soup = BeautifulSoup(plain_text, "html.parser")
	item_name = soup.findAll('p')
	print(item_name[3].get_text())

trade_spider(0)