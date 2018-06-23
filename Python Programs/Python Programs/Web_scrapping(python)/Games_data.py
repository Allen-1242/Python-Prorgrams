#webstuff 
import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://store.steampowered.com/tags/en/Action/'

uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

filename = 'free_games.csv'
f = open(filename, "w")

headers = "product name"
f.write(headers)



page_soup = soup(page_html, "html.parser")

#print(page_soup.h2)
#print(page_soup.body.span)
contain = page_soup.findAll("div", {"class":"tab_item_top_tags"})
num = (len(contain))
#print(contain[5])
con = contain[0]
for i in range(num):
	con = contain[i]
	print(con)

#container = contain[5]
print(con.findAll('span')[0].text)
#for con in range(len(contain)):
	#tag = con.span
f.close()

