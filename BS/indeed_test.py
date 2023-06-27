import requests
from bs4 import BeautifulSoup

url = 'https://ca.indeed.com/jobs?q=sql+developer&l=&from=searchOnHP&vjk=756ff149acd25cee'
res = requests.get(url)
html = res.text
soup = BeautifulSoup(html, 'lxml', multi_valued_attributes=None)
jobs = soup.find('ul', {'class': 'jobsearch-ResultsList css-0'})
print(soup)
# jbs = jobs.findAll('li')
# for job in jbs:
#     row = job.find('div', {'class': 'job_seen_beacon'})
#     print(row)
