import requests
from bs4 import BeautifulSoup
import time
print("Enter your unfamiliar skill")
unfamiliar_skill=input('>')
def scrap():
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=java&txtLocation=').text
    soup = BeautifulSoup(html_text,'lxml')
    print(f"Jobs with \'{unfamiliar_skill}\' as requirement:")
    jobs = soup.find_all('li',class_ = 'clearfix job-bx wht-shd-bx')
    for index,job in enumerate(jobs):
        published_date = job.find('span',class_ = 'sim-posted').span.text
        if 'few' in published_date:
            company_name = job.find('h3',class_ = 'joblist-comp-name').text.strip()
            key_skill = job.find('span',class_ = 'srp-skills').text.strip().replace(' ','')
            link_to_apply = job.find('header',class_='clearfix').h2.a['href']
            if unfamiliar_skill not in key_skill:
                with open(f'skilljobs/{index}.txt','w') as f:
                    f.write(f'Company name : {company_name}\n')
                    f.write(f'Key skills : {key_skill}\n')
                    f.write(f'Apply at : {link_to_apply}')
if __name__=="__main__":
    while True:
        scrap()
        print("Waiting 10 minutes...")
        time.sleep(600)
