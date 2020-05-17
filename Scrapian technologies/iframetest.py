#For Testing purposes.


from selenium import webdriver
import time
CHROME_PATH = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
CHROMEDRIVER_PATH = r"C:\Users\lawalo\Desktop\chromedriver_win32\chromedriver.exe"



driver = webdriver.Chrome(CHROMEDRIVER_PATH)

driver.get("https://careers-enernoc.icims.com/jobs/search?ss=1")
time.sleep(5) 
iframe = driver.find_element_by_xpath("""//*[@id="icims_content_iframe"]""")
 
driver.switch_to.default_content()
 
driver.switch_to.frame(iframe)
 
iframe_source = driver.page_source
 
print(driver.find_elements_by_xpath("""/html/body/div[3]/ul/li[1]/div[5]/div/dl[2]/dd/span"""))
#print(iframe_source) #returns iframe source
 
print(driver.current_url) #returns iframe URL

print("done")