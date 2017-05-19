import requests
import io
url = "https://m.tengrinews.kz/ru/ajax/GetLatestNews?page=%d"
with open("output.txt", "wb") as file:
	for page in range(1,2):
		r = requests.get(url % page)
	    file.write(r.text.encode('utf-8'))
	    file.write("\n".encode('utf-8')) 
