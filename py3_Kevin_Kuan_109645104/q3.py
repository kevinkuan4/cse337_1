# CSE337
# Kevin Kuan
# 109645104
from bs4 import BeautifulSoup

import urllib.request 

f = open("top10articles.txt","w")

site_url = "https://finance.google.com/finance/market_news"
r = urllib.request.urlopen(site_url).read()

soup = BeautifulSoup(r, "html.parser")
print(soup.prettify())