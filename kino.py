import requests 
from bs4 import BeautifulSoup

url = "http://kino.kz/cinema.asp?cinemaid=140"
r = requests.get(url)
html = r.text
soup = BeautifulSoup(html, "html.parser")
rows = soup.select("div.detail_content table:nth-of-type(2) tr")
tr = rows[0]
name = tr.select("td strong a")[0].text
#rate = tr.select("td:nth-of-type(1)")[0].text
timeone = tr.select("td table tr:nth-of-type(2) td")[0].text
timetwo = tr.select("td table tr:nth-of-type(3) td")[0].text
timeth = tr.select("td table tr:nth-of-type(4) td")[0].text
timef = tr.select("td table tr:nth-of-type(5) td")[0].text
print(name)
print (timeone)
print(timetwo)
print(timeth)
print(timef)

import requests 
from bs4 import BeautifulSoup
url = "http://kino.kz/cinema.asp?cinemaid=140"
r = requests.get(url)
html = r.text
soup = BeautifulSoup(html, "html.parser")
rows = soup.select("div.detail_content table:nth-of-type(2) tr:nth-of-type(3)")
tr = rows[0]
timeonef = tr.select("td table tr:nth-of-type(2) td")[0].text
#namez = trs.select("td strong a")[0].text
#timeonee = tr.select("td table tr:nth-of-type(3) td")[0].text
print(timeonef) 