import requests
from bs4 import BeautifulSoup 
url = 'http://kazhydromet.kz/ru/almaty'
r = requests.get(url)
html = r.text
soup = BeautifulSoup(html, "html.parser")
wtext = soup.select(".w_map span")[0].text
print(wtext)

xtext = soup.select(".p_data span br")[0].text

if "без осадков" in xtext:
	print("Зонт не нужен")
else:
	print("Бери зонт")
if "снег" in xtext:
	print("Одевай шапку")
else:
	print("Можно без шапки")
if "ясно" in xtext:
	print("Будет солнечно, бери очки")
else:
	pass

url = 'http://kazhydromet.kz/ru/aktau'
r = requests.get(url)
html = r.text
soup = BeautifulSoup(html, "html.parser")
wtext = soup.select(".w_map span")[0].text
print(wtext)

xtext = soup.select(".p_data span br")[0].text

if "без осадков" in xtext:
	print("Зонт не нужен")
else:
	print(" ")
if "снег" in xtext:
	print("Одевай шапку")
else:
	print(" ")
if "Ясно" or "ясно" in xtext:
	print("Будет солнечно, бери очки")
else:
	print(" ")



