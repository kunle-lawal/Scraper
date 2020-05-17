#For testing purposes.

'''
from selenium import webdriver
driver = webdriver.PhantomJS(executable_path="C:/Users/lawalo/Documents/Sublime text/scraper/Scrapian technologies/phantomjs-2.1.1-windows")
driver.get(my_url)
p_element = driver.find_element_by_id(id_='intro-text')
print(p_element.text)
# result:
'Yay! Supports javascript'
'''

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

CHROME_PATH = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
CHROMEDRIVER_PATH = r"C:\Users\lawalo\Desktop\chromedriver_win32\chromedriver.exe"
WINDOW_SIZE = "1920,1080"

chrome_options = Options()  
chrome_options.add_argument("--headless")  
chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
chrome_options.binary_location = CHROME_PATH

driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, chrome_options=chrome_options)

driver.get("https://simplisafe.com/careers#open-positions-full")

#//*[@id="job19082"]/th/div/div/span/a


job = driver.find_element_by_xpath("""//*[@id="23370"]/tr[2]/td[1]""")
job2 = driver.find_element_by_xpath("""//*[@id="23368"]/tr[1]/td[1]""")

print(job2.text)

'''
driver.get("https://www.google.com")
#driver.get_screenshot_as_file("capture.png")
driver.close()
'''