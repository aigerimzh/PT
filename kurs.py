import requests 
from bs4 import BeautifulSoup

url = "https://mig.kz/"
r = requests.get(url)
html = r.text
soup = BeautifulSoup(html, "html.parser")
tr = soup.select("div.informer table tr")[0]
rate = tr.select("td")[0].text
name = tr.select("td")[1].text
print(name  + " "+ rate)
# for tr in rows:
# 	name = tr.select("td a")[0].text
# 	rate = float(tr.select("td span.today")[0].text.replace(",", "."))
# 	print("%s\t%f" % (name, rate))


