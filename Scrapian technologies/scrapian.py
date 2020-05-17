''' 
Copyright © Scrapian Technologies, Inc - All Rights Reserved 
Unauthorized copying of this file, via any medium is strictly prohibited 
Proprietary and confidential 
Written by Olakunle Lawal <olawal196@gmail.com>, 2018

'''

#import libraries

#import libraries for selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#Imports for beautiful Soup
from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup

#Imports for Excel Datasets
from datetime import datetime
import csv

#create chrome window to handle all the web urls
CHROME_PATH = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
CHROMEDRIVER_PATH = r"C:\Users\lawalo\Desktop\chromedriver_win32\chromedriver.exe"
WINDOW_SIZE = "1920,1080"

#Custom option to stop chrome window from opening
chrome_options = Options()  
# chrome_options.add_argument("--headless")  
chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
chrome_options.binary_location = CHROME_PATH

driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, chrome_options=chrome_options)

#Website we are scrpaing
page_url = "https://twitter.com/login"

#Variable for possible information about the job
jobType = ["JOB TYPE"]
jobTitle = ["JOB TITLE"]
location = ["LOCATION"]
datePosted = ["DATE POSTED"]
jobDescription = ["JOB DESCRIPTION"]
jobDuration = ["JOB DURATION"]

login_email = """//*[@id="page-container"]/div/div[1]/form/fieldset/div[1]/input"""
login_pass = """//*[@id="page-container"]/div/div[1]/form/fieldset/div[2]/input"""
login_button = """//*[@id="page-container"]/div/div[1]/form/div[2]/button"""

info_needed_arr = [jobType, jobTitle, location, datePosted, jobDescription, jobDuration]

#Function for getting the xPath for all the information needed. Get xPath from function parameters, get the information based on the xPath from the website append the information into the appropriate inofrmation array. 
def scrape_with_Xpath(jobType_xpath, jobTitle_xpath, location_xpath, datePosted_xpath, jobDescription_xpath, jobDuration_xpath):
	the_jobType = driver.find_elements_by_xpath(jobType_xpath)
	the_jobTitle = driver.find_elements_by_xpath(jobTitle_xpath)
	the_location = driver.find_elements_by_xpath(location_xpath)
	the_datePosted = driver.find_elements_by_xpath(datePosted_xpath)
	the_jobDescription = driver.find_elements_by_xpath(jobDescription_xpath)
	the_jobDuration = driver.find_elements_by_xpath(jobDuration_xpath)
	info_recieved_arr = [the_jobType, the_jobTitle, the_location, the_datePosted, the_jobDescription, the_jobDuration]

	x = 0
	for info_recieved in info_recieved_arr:
		for info in info_recieved:
			info_needed_arr[x].append(info.text)
		x += 1

#Function for scraping iframe data
def get_iFrame_url(url):
	driver.get(url)
	iframe = driver.find_element_by_tag_name("iframe")
	driver.switch_to.default_content()
	driver.switch_to.frame(iframe)
	iframe_source = driver.page_source

	return driver.current_url

#Function to input information into input element
def input_info(info, xPath): 
	driver.find_element_by_xpath(xPath).send_keys(info);

#Function to click buttons on page
def click_button(button_xpath):
	driver.find_element_by_xpath(button_xpath).click()

#Add extra values to each dataset if the length does not match the largest dataset
def equalize_dataset(datasets):
	largest_dataset = largest_val_in_arr(datasets)

	for info in datasets:
		for x in range(largest_dataset - len(info)):
			info.append("N/A")

#Set the main array equal to a new one suited for storing info onto excel	
def restructure_dataset(datasets):
	largest_dataset = largest_val_in_arr(datasets)

	newinfo = []
	for x in range(largest_dataset):
		newinfo.append((jobType[x], jobTitle[x], location[x], datePosted[x], jobDescription[x], jobDuration[x]))
	return newinfo

#Store data into an excel sheet.
def store_scraped_info(csvFileName):
	with open ('exceldata/' + csvFileName + '.csv', 'a') as csvfile:
		writer = csv.writer(csvfile)

		data_num = 0
		for a, b, c, d, e, f in info_needed_arr:
			writer.writerow([a, b, c, d, e, f])
			data_num += 1

		writer.writerow(["End Data Range", data_num])

#get the largest value in the array
def largest_val_in_arr(arr):
	prev_max = 0
	curr_max = 0
	for x in arr:
		curr_max = 0
		for y in x:  	
			curr_max += 1
		if curr_max > prev_max: prev_max = curr_max

	return prev_max

def deletePost(): 
	x = 2
	delete = """//*[@id="react-root"]/div/div/div[1]/div/div/div[2]/div[3]/div/div/div/div[1]"""
	final_delete = """//*[@id="react-root"]/div/div/div[1]/div/div/div/div/div[2]/div[2]/div[3]/div[2]"""
	wait = WebDriverWait(driver, 10)
	# element = wait.until(EC.element_to_be_clickable((By.XPATH, dropdown)))
	# element.click()
	# driver.implicitly_wait(100)
	# click_button(dropdown)

	# # delete_ = wait.until(EC.presence_of_element_located((By.XPATH, delete)))
	# click_button(delete)

	# # final_delete_ = wait.until(EC.presence_of_element_located((By.XPATH, final_delete)))
	# click_button(final_delete)

	while x < 4:
		dropdown = """//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div/div[2]/div/div/div[2]/section/div/div/div/div[{}]/div/article/div/div[2]/div[2]/div[1]/div[2]""".format(x)
		element = wait.until(EC.element_to_be_clickable((By.XPATH, dropdown)))
		element.click()

		element2 = wait.until(EC.element_to_be_clickable((By.XPATH, delete)))
		element2.click()

		element3 = wait.until(EC.element_to_be_clickable((By.XPATH, final_delete)))
		element3.click()
		x += 1
	else:
		driver.refresh()
		x = 1
		deletePost()
# //*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div/div[2]/div/div/div[2]/section/div/div/div/div[1]/div/article/div/div[2]/div[2]/div[3]/div[2]/div/div/div[1]
# //*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div/div[2]/div/div/div[2]/section/div/div/div/div[1]/div/article/div/div[2]/div[2]/div[3]/div[2]/div/div/div[1]
# //*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div/div[2]/div/div/div[2]/section/div/div/div/div[2]/div/article/div/div[2]/div[2]/div[4]/div[2]/div/div/div[1]
# //*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div/div[2]/div/div/div[2]/section/div/div/div/div[3]/div/article/div/div[2]/div[2]/div[4]/div[2]/div/div/div[1]
# //*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div/div[2]/div/div/div[2]/section/div/div/div/div[4]/div/article/div/div[2]/div[2]/div[4]/div[2]/div/div/div[1]
# //*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div/div[2]/div/div/div[2]/section/div/div/div/div[21]/div/article/div/div[2]/div[2]/div[4]/div[2]/div/div/div[1]

def unretweet():
	x = 1
	wait = WebDriverWait(driver, 10)

	undoRetweet = """//*[@id="react-root"]/div/div/div[1]/div/div/div[2]/div[3]/div/div/div/div"""
	while x < 4:
		retweet = """//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div/div[2]/div/div/div[2]/section/div/div/div/div[{}]/div/article/div/div[2]/div[2]/div[4]/div[2]/div/div/div[1]""".format(x)
		element = wait.until(EC.element_to_be_clickable((By.XPATH, retweet)))
		element.click()

		element2 = wait.until(EC.element_to_be_clickable((By.XPATH, undoRetweet)))
		element2.click() 
		x += 1
	else:
		driver.refresh()
		x = 1
		unretweet()

# //*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div/div[2]/div/div/div[2]/section/div/div/div/div[1]/div/article/div/div[2]/div[2]/div[3]/div[3]/div/div/div[1]
# //*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div/div[2]/div/div/div[2]/section/div/div/div/div[2]/div/article/div/div[2]/div[2]/div[4]/div[3]/div/div/div[1]
# //*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div/div[2]/div/div/div[2]/section/div/div/div/div[3]/div/article/div/div[2]/div[2]/div[4]/div[3]/div/div/div[1]

# //*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div/div[2]/div/div/div[2]/section/div/div/div/div[1]/div/article/div/div[2]/div[2]/div[4]/div[3]/div/div/div[1]
# //*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div/div[2]/div/div/div[2]/section/div/div/div/div[3]/div/article/div/div[2]/div[2]/div[3]/div[3]/div/div/div[1]
def unlike():
	x = 1
	wait = WebDriverWait(driver, 10)

	 hile x < 2:2		like = """//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div/div[2]/div/div/div[2]/section/div/div/div/div[{}]/div/article/div/div[2]/div[2]/div[4]/div[3]/div/div/div[1]""".format(x)
		element = wait.until(EC.element_to_be_clickable((By.XPATH, like)))
		element.click()

		x += 1
	else:
		driver.refresh()
		x = 1
		unlike() 

#Run main py code Here
def main():
	# global info_needed_arr 
	# #Provide the xpath to scrpae for
	# #job type, job name, location, date posted, description, duration
	# jobType_path = """/html/body/div[3]/ul/li[1]/div[5]/div/dl[2]/dd/span"""
	# jobTitle_path = """/html/body/div[3]/ul/li[1]/div[3]/a/span[2]"""
	# jobLocation_path = """/html/body/div[3]/ul/li[1]/div[5]/div/dl[1]/dd/span"""
	# datePosted_path = """/html/body/div[3]/ul/li[1]/div[2]/span[2]/span"""
	# jobDescription_path = """/html/body/div[3]/ul/li[1]/div[4]"""
	# jobDuration_path = """//*[@id=""]/div"""


	driver.get(page_url)

	# scrape_with_Xpath(jobType_path, jobTitle_path , jobLocation_path, datePosted_path, jobDescription_path, jobDuration_path)
	# equalize_dataset(info_needed_arr)
	# info_needed_arr = restructure_dataset(info_needed_arr)
	# store_scraped_info('simplisafetest')

	# print('Done')
	# wait = WebDriverWait(driver, 10)
	# wait.until(EC.presence_of_element_located((By.XPATH, login_email)))
	next_value = 2;
	profile = """//*[@id="react-root"]/div/div/div/header/div/div/div/div/div[{}]/nav/a[7]""".format(next_value)
	tweets = """//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div/div[2]/div/div/nav/div[2]/div[1]/a""" 
	replies = """//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div/div[2]/div/div/nav/div[2]/div[2]/a"""
	likes = """//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div/div[2]/div/div/nav/div[2]/div[4]/a"""


	input_info('aplayerwahted@gmail.com', login_email)
	input_info('rWE2@_/*3jSdb2x', login_pass)
	click_button(login_button)
	driver.implicitly_wait(10)
	click_button(profile)
	click_button(likes)
	
	# for x in range(10):
	# deletePost();
	unlike();
	# unretweet();

if __name__ == "__main__":
	main()


#driver.find_element_by_id('jsb_form_submit_i').click()
#click_button("""//*[@id="jsb_form_submit_i"]""")

'''wait = WebDriverWait(driver, 10)
element = wait.until(EC.presence_of_element_located((By.XPATH, """//*[@class="iCIMS_JobsTable"]/li[1]/div[5]/div/dl[2]/dd/span""")))'''
