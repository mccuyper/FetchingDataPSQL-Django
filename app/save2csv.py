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

    