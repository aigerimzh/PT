import telegram
bot = telegram.Bot(token = '358896979:AAHL7UsgmCG7vMtApcA3GFrdYFlSahiVMIM')
# updates = bot.getUpdates()
# for update in updates:
# 	print(update.message.text)
# 	print(update.message.from_user.id)
# 	print(update.message.from_user.first_name)
# 	print()
from telegram.ext import Updater
updater = Updater(token='358896979:AAHL7UsgmCG7vMtApcA3GFrdYFlSahiVMIM')
dispatcher = updater.dispatcher

def say_start(bot, update):
	bot.sendMessage(chat_id = update.message.chat_id, text="Привет!")

from telegram.ext import CommandHandler
start_handler = CommandHandler('start', say_start)
dispatcher.add_handler(start_handler)

# def echo(bot, update):
# 	if "рубль" in update.message.text.lower():
		
# 	elif "евро" in update.message.text.lower():
# 		def tengee(bot, update):
# 			import requests 
# 			from bs4 import BeautifulSoup
# 			url = "https://mig.kz/"
# 			r = requests.get(url)
# 			html = r.text
# 			soup = BeautifulSoup(html, "html.parser")
# 			tr = soup.select("div.informer table tr")[1]
# 			rate = tr.select("td")[0].text
# 			name = tr.select("td")[1].text
# 			wtext = name  + " "+ rate
# 			print(wtext)
# 			tengee_handler = CommandHandler('tengee', tengee)
# 			dispatcher.add_handler(tengee_handler)
		
# 	bot.sendMessage(chat_id=update.message.chat_id, text=wtext)

def tenged(bot, update):
	import requests 
	from bs4 import BeautifulSoup
	url = "https://mig.kz/"
	r = requests.get(url)
	html = r.text
	soup = BeautifulSoup(html, "html.parser")
	tr = soup.select("div.informer table tr")[0]
	rate = tr.select("td")[0].text
	name = tr.select("td")[1].text
	wtext = name  + " "+ rate
	print(wtext)
	bot.sendMessage(chat_id = update.message.chat_id, text=wtext)

tenged_handler = CommandHandler('tenged', tenged)
dispatcher.add_handler(tenged_handler)

def tengee(bot, update):
	import requests 
	from bs4 import BeautifulSoup
	url = "https://mig.kz/"
	r = requests.get(url)
	html = r.text
	soup = BeautifulSoup(html, "html.parser")
	tr = soup.select("div.informer table tr")[1]
	rate = tr.select("td")[0].text
	name = tr.select("td")[1].text
	wtext = name  + " "+ rate
	print(wtext)
	bot.sendMessage(chat_id = update.message.chat_id, text=wtext)

tengee_handler = CommandHandler('tengee', tengee)
dispatcher.add_handler(tengee_handler)

def tenger(bot, update):
	import requests 
	from bs4 import BeautifulSoup
	url = "https://mig.kz/"
	r = requests.get(url)
	html = r.text
	soup = BeautifulSoup(html, "html.parser")
	tr = soup.select("div.informer table tr")[2]
	rate = tr.select("td")[0].text
	name = tr.select("td")[1].text
	wtext = name  + " "+ rate
	print(wtext)
	bot.sendMessage(chat_id = update.message.chat_id, text=wtext)

tenger_handler = CommandHandler('tenger', tenger)
dispatcher.add_handler(tenger_handler)






updater.start_polling()
