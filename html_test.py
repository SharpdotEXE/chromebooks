import requests
from bs4 import BeautifulSoup

session = requests.Session()
response = session.get('https://www.dell.com/support/home/en-us/product-support/servicetag/C60D5Q2/overview',
           headers={'User-Agent': 'Chrome/93.0.4577.63', 'cache-control': 'no-cache'})

#print(response.status_code)

soup = BeautifulSoup(response.content, 'html.parser')
#print(soup.prettify())
html = list(soup.children)[0]

print(list(html.children)[3])


