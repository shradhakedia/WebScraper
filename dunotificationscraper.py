'''
from selenium import webdriver
PATH = 'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(PATH)
driver.get('http://cs.du.ac.in/')
print(driver.title)
news = driver.find_elements_by_tag_name('div')
for latestnews in news:
    header = latestnews.find_element_by_class_name('content')
    print(header.text)
#driver.close()
driver.quit()

'''
from bs4 import BeautifulSoup
import requests
html_text = requests.get('http://cs.du.ac.in/').text
html_text = html_text.replace("<!-->", "")
soup = BeautifulSoup(html_text,'lxml')
print(soup.prettify())
table1 = soup.find_all('table',id="whatsnew")
print(table1)