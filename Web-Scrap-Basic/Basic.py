import requests 
import bs4

res = requests.get('https://en.wikipedia.org/wiki/Web_scraping')

soup = bs4.BeautifulSoup(res.text , 'html.parser')

# print(soup.prettify())
# print(soup.title)

# select tag
title = soup.select('title')

# select class 
select_class = soup.select('.toctext')

# for i in select_class:
#   print(i.text)

# output

# History
# Techniques
# Human copy-and-paste
# Text pattern matching
# HTTP programming
# HTML parsing
# DOM parsing
# Vertical aggregation
# Semantic annotation recognizing
# Computer vision web-page analysis
# Software
# Legal issues
# United States
# European Union
# Australia
# India
# Methods to prevent web scraping
# See also
# References