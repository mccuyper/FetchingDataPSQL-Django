# # Importing the required modules
# import os
# import sys
# import pandas as pd
# from bs4 import BeautifulSoup

# path = 'localhost:8000/index.html'

# # empty list
# data = []

# # for getting the header from
# # the HTML file
# list_header = []
# soup = BeautifulSoup(open(path),'html.parser')
# header = soup.find_all("table")[0].find("tr")

# for items in header:
# 	try:
# 		list_header.append(items.get_text())
# 	except:
# 		continue

# # for getting the data
# HTML_data = soup.find_all("table")[0].find_all("tr")[1:]

# for element in HTML_data:
# 	sub_data = []
# 	for sub_element in element:
# 		try:
# 			sub_data.append(sub_element.get_text())
# 		except:
# 			continue
# 	data.append(sub_data)

# # Storing the data into Pandas
# # DataFrame
# dataFrame = pd.DataFrame(data = data, columns = list_header)

# # Converting Pandas DataFrame
# # into CSV file
# dataFrame.to_csv('Geeks.csv')


from bs4 import BeautifulSoup
import urllib.request
import csv

url = 'http://127.0.0.1:8000/?item_name=domain2.gcpbx.cloud&month='
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html)
table = soup.select_one("table")
# python3 just use th.text
headers = [th.text for th in table.select("tr th")]

with open("out.csv", "w") as f:
    wr = csv.writer(f)
    wr.writerow(headers)
    wr.writerows([[td.text for td in row.find_all("td")] for row in table.select("tr + tr")])