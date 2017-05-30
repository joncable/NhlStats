import csv
import requests
import re
from bs4 import BeautifulSoup

# scrape data from player page on ESPN
url = 'http://www.espn.com/nhl/player/gamelog/_/id/3231/carey-price'
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html, "html.parser")

stat_categories = [];

# by inspecting the element, we know the class of the div is responsive-datatable
for table in soup.find_all("table", {"class" : "tablehead"}):
	# print(table.text)
	column_headers = table.findChildren(['tr', 'th'])[1]
	for ch in column_headers:
		# set column headers as stat categories
		stat_categories.append(ch.contents[0])

	for sc in stat_categories:
		print(sc)

	for row in table.findChildren(['tr', 'th']):
		for a in row.findChildren('a'):
			# update game id if this is one
			if 'gameId' in a['href']:
				game_href = a['href']
				game_id = re.search('gameId=(.+?)$', game_href).group(1)
				print("Updating new GAME_ID: %s" % game_id)
		index = 0
		# print(row.text)
		for column in row.findChildren('td'):
			# print("######### COLUMN:")
			# print(column.contents)
			stat = column.text
			print("index: " + str(index) + " stat: " + str(stat))
			index += 1


