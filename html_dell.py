import urllib.request
from bs4 import BeautifulSoup

page = urllib.request.urlopen("https://www.dell.com/support/home/en-us/product-support/servicetag/C60D5Q2/overview")

soup = BeautifulSoup(page.content, 'html.parser')
print(soup.prettify())


#doctype = 0, newline = 1,
# html = list(soup.children)[2]
# head = list(html.children)[1]
# title = list(head.children)[1]
# print(title)

