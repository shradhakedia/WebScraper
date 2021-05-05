from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#  firstly you need to choose path as chromedriver that you installed
PATH = 'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(PATH)

# loading the page
driver.get("https://web.whatsapp.com/")

# searching the span tag that cpntains title as the name of the person in contact list
# user = driver.find_element_by_xpath("//span[@title='{}']".format("Ankit"))
# user.click()


# OR explictly wait for the page to load and this element that is search tab to appear
# user = WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.CLASS_NAME, "_2_1wd")))
# user.send_keys("9899519848")
# user.send_keys(Keys.RETURN)


# OR use time.sleep and let it wait to load, best approach is using explicit wait
time.sleep(10)
user = driver.find_element_by_class_name("_2_1wd")
user.send_keys("9899519848")
user.send_keys(Keys.RETURN)


time.sleep(2)

# finding msg bar area
msg = driver.find_element_by_class_name("_2A8P4")
time.sleep(2)
for i in range(5):
    msg.send_keys("Hello, This is webautomation done by me 5 times in a loop.")
    time.sleep(2)
    # use time.sleep everywhere or use Explicit wait
    #finding the send button 
    button = driver.find_element_by_class_name("_1E0Oz")

    # button = WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.CLASS_NAME, "_1E0Oz")))
    button.click()
    time.sleep(2)

