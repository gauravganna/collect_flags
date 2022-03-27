import requests
from bs4 import BeautifulSoup

BASE_URL = 'https://meaprotocol.nic.in/'
ROOT_EXT = '?a19'
page = requests.get(BASE_URL+ROOT_EXT)
soup = BeautifulSoup(page.content, "html.parser")
job_els = soup.find_all("p", class_="focucHomDisc")

with open('countriesEmbassyDetails.csv', 'w') as f:
    f.write('Country, URL\n')
    for job_el in job_els:
        country = job_el.find('a').text
        print('Getting Email for Country: ' + country)
        try:
            NEW_URL = BASE_URL + job_el.find('a')['href'].replace("./", "")
            page = requests.get(NEW_URL)
            soup = BeautifulSoup(page.content, "html.parser")
            els = soup.find_all("span", class_="contactIcon")
            f.write(country + ', ' + els[-1].find('img').previousSibling +
                    '@'+els[-1].find('img').text+'\n')
        except:
            print("Failed for Counttry: ", country)
