import requests 
from bs4 import BeautifulSoup

url = "http://www.kino.kz/cinema/index.asp" 
r = requests.get(url)
html = r.text
soup = BeautifulSoup(html, "html.parser")
rows = soup.select("div.wrappeer table td:nth-of-type(2)")
td = rows[0]
namecinima = td.select("div.move_detail table tr td:nth-of-type(2) div.title_red")[0].text
print(namecinima)