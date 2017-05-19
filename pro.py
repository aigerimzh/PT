import requests
from bs4 import BeautifulSoup 
url = 'http://www.kino.kz/thisweek.asp?city=2&type=1&day=0#top'
r = requests.get(url)
html = r.text
soup = BeautifulSoup(html, "html.parser")
wtext = soup.select(".wrappeer table td:nth-of-type(2) .mov_week mov span")[0].text
print(wtext)