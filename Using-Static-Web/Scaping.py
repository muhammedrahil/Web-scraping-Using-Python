import requests 
from bs4  import BeautifulSoup
import lxml

with open('index.html',encoding="utf8") as html_file:
  soup = BeautifulSoup(html_file , 'lxml')
  
# print(soup.header)

toggler = soup.find('button' ,class_='navbar-toggler')
print(toggler)


for image in soup.find_all('img'):
  print(image)
  print(image['src'])