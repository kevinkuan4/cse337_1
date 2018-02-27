# CSE337
# Kevin Kuan
# 109645104
from bs4 import BeautifulSoup

import urllib.request 

f = open("top10articles.txt","w")

site_url = "https://finance.google.com/finance/market_news"
r = urllib.request.urlopen(site_url).read()

soup = BeautifulSoup(r, "html.parser")

articles = soup.find_all(class_="g-section news sfe-break-bottom-16")

for i in articles:
	name=(i.find(class_="name").get_text()).strip("\n")

	src=(i.find(class_="src").get_text())
	date=(i.find(class_="date").get_text())
	f.write(name+","+src+","+date+"\n")

f.close()