#MOOFI assingment
#webstuff 
'''import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'http://www.occupationalhealth.co.uk/WeightConversion.htm'

uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()


movie_house = list()
page_soup = soup(page_html, "html.parser")
stat_table = page_soup.findAll('table')
stat_table = stat_table[0]

with open ('weights.csv', 'w') as f1:
	for row in stat_table.findAll('tr'):
		for cell in row.findAll('td'):
			print(cell.text)
			f1.write(cell.text)
			f1.write(',')
		f1.write('\n')

print(type(stat_table))'''


import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'http://www.boxofficemojo.com/studio/?view2=yearly&view=company&p=.htm'

uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

movie_list = list()

page_soup = soup(page_html, "html.parser")
stat_table = page_soup.findAll('table')
stat_table = stat_table[2]
row = 8
with open ('moofiz.txt', 'w') as f1:
	for row in stat_table.findAll('tr'):
		for cell in row.findAll('td'):
			for i in cell.findAll('font', {'size': 2}):	
				print(i.text)
				f1.write(i.text)
				f1.write(',')
				f1.write('\t')
		f1.write('\n')
		f1.write('\n')














