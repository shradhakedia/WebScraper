'''
this code uses Beautiful soup module, to scrap the content of Codechef i.e. specifically links to all
the past,running and future contests of codechef, and
requests module that lets you get the html text of the url provided
'''
import requests
from bs4 import BeautifulSoup
import time
html_text = requests.get('https://www.codechef.com/problems/school/?itm_medium=navmenu&itm_campaign=problems_head').text
soup = BeautifulSoup(html_text,'lxml')
#parser used is lxml
compete=soup.find('li',class_='menuparent menu-path-https--www.codechef.com-contests-itm_mediumnavmenuitm_campaignallcontests_head') #finds the compete block of CC page and under that dropdown list finds all the links of contests 
All_past_contests = compete.find('li',class_="menu-path-https--www.codechef.com-contests-itm_mediumnavmenuitm_campaignallcontests#past-contests").a['href']
All_running_contests = compete.find('li',class_="menu-path-https--www.codechef.com-contests-itm_mediumnavmenuitm_campaignallcontests#present-contests").a['href']
All_future_contests = compete.find('li',class_="menu-path-https--www.codechef.com-contests-itm_mediumnavmenuitm_campaignallcontests#future-contests").a['href']
print("Welcome to CodechefContestScraper:")
print("Waiting 5 seconds...")
time.sleep(5)
print(f'Link to all past contest is:{All_past_contests}')
time.sleep(5)
print(f'Link to all running contest is:{All_running_contests}')
time.sleep(5)
print(f'Link to all future contest is:{All_future_contests}')
time.sleep(5)