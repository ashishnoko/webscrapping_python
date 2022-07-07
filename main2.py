from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://merojob.com/category/it-telecommunication/').text
soup = BeautifulSoup(html_text,'lxml')

jobs_title = soup.find('h1',class_='text-primary font-weight-bold media-heading h4').text.replace('','')
jobs = soup.find('h3',class_='h6').text
skills = soup.find('span',class_='badge badge-pill badge-light rounded text-muted').text

#for span in skills:
    #print (span.text)

print(f'''
Jobs Title : {jobs_title}
Skills Reuired : {skills}

''')





