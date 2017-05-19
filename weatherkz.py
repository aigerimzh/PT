import telegram
bot = telegram.Bot(token = '304915544:AAHaEOQ-QBbIISFzuJ9eUlpAH3xusYnlfOc')

from telegram.ext import Updater
updater = Updater(token='304915544:AAHaEOQ-QBbIISFzuJ9eUlpAH3xusYnlfOc')
dispatcher = updater.dispatcher

def say_start(bot, update):
	bot.sendMessage(chat_id = update.message.chat_id, text="Привет! Выбери свой город. Введи /")

from telegram.ext import CommandHandler
start_handler = CommandHandler('start', say_start)
dispatcher.add_handler(start_handler)

def almaty (bot, update):
	import requests
	from bs4 import BeautifulSoup 
	url = 'http://kazhydromet.kz/ru/almaty'
	r = requests.get(url)
	html = r.text
	soup = BeautifulSoup(html, "html.parser")
	wtext = soup.select(".w_map span")[0].text
	#print(wtext)
	s = wtext
	integ = ''
	for n in s:
		if n.isdigit():
			integ = integ + n
		else:
			integ = integ + ' '
	if "+" in s:
		ww = "+"+integ
		www = ww.replace(' ', ' ')
		bot.sendMessage(chat_id = update.message.chat_id, text=www)
	else:
		zz = "-"+integ
		zzz = zz.replace(' ', '')
		bot.sendMessage(chat_id = update.message.chat_id, text=zzz)

	s = wtext
	if "+"  in s:
		h = "Можно одеться полегче"
		bot.sendMessage(chat_id = update.message.chat_id, text=h)
	elif "0" in s:
		hh = "Можно одеться полегче"
		bot.sendMessage(chat_id = update.message.chat_id, text=hh)
	else: 
		hhh = "Оденься потеплее"
		bot.sendMessage(chat_id = update.message.chat_id, text=hhh)

	xtext = soup.select(".p_data span br")[0].text
	if "без осадков" in xtext:
		q = "Зонт не нужен"
		bot.sendMessage(chat_id = update.message.chat_id, text=q)
	else:
		qq = "Бери зонт"
		bot.sendMessage(chat_id = update.message.chat_id, text=qq)
	if "снег" in xtext:
		r = "Одевай шапку"
		bot.sendMessage(chat_id = update.message.chat_id, text=r)
	else:
		rr = "Можно без шапки"
		bot.sendMessage(chat_id = update.message.chat_id, text=rr)
	if "ясно" in xtext:
		t = "Будет солнечно, бери очки"
		bot.sendMessage(chat_id = update.message.chat_id, text=t)
	else:
		pass
	if "осадки" in xtext:
		tt = "Обещают дождик, захвати зонт"
		bot.sendMessage(chat_id = update.message.chat_id, text=tt)
	else:
		pass

almaty_handler = CommandHandler('almaty', almaty)
dispatcher.add_handler(almaty_handler)

def aktau (bot, update):
	import requests
	from bs4 import BeautifulSoup 
	url = 'http://kazhydromet.kz/ru/aktau'
	r = requests.get(url)
	html = r.text
	soup = BeautifulSoup(html, "html.parser")
	wtext = soup.select(".w_map span")[0].text
	#print(wtext)
	s = wtext
	integ = ''
	for n in s:
		if n.isdigit():
			integ = integ + n
		else:
			integ = integ + ' '
	if "+" in s:
		ww = "+"+integ
		www = ww.replace(' ', ' ')
		bot.sendMessage(chat_id = update.message.chat_id, text=www)
	else:
		zz = "-"+integ
		zzz = zz.replace(' ', '')
		bot.sendMessage(chat_id = update.message.chat_id, text=zzz)

	s = wtext
	if "+"  in s:
		h = "Можно одеться полегче"
		bot.sendMessage(chat_id = update.message.chat_id, text=h)
	elif "0" in s:
		hh = "Можно одеться полегче"
		bot.sendMessage(chat_id = update.message.chat_id, text=hh)
	else: 
		hhh = "Оденься потеплее"
		bot.sendMessage(chat_id = update.message.chat_id, text=hhh)

	xtext = soup.select(".p_data span br")[0].text
	if "без осадков" in xtext:
		q = "Зонт не нужен"
		bot.sendMessage(chat_id = update.message.chat_id, text=q)
	else:
		pass
		# qq = "Бери зонт"
		# bot.sendMessage(chat_id = update.message.chat_id, text=qq)
	if "снег" in xtext:
		r = "Одевай шапку"
		bot.sendMessage(chat_id = update.message.chat_id, text=r)
	else:
		rr = "Можно без шапки"
		bot.sendMessage(chat_id = update.message.chat_id, text=rr)
	if "Ясно" in xtext:
		t = "Будет солнечно, бери очки"
		bot.sendMessage(chat_id = update.message.chat_id, text=t)
	else:
		pass
	if "осадки" in xtext:
		tt = "Обещают дождик, захвати зонт"
		bot.sendMessage(chat_id = update.message.chat_id, text=tt)
	else:
		pass
aktau_handler = CommandHandler('aktau', aktau)
dispatcher.add_handler(aktau_handler)


def karaganda (bot, update):
	import requests
	from bs4 import BeautifulSoup 
	url = 'http://kazhydromet.kz/ru/aktau'
	r = requests.get(url)
	html = r.text
	soup = BeautifulSoup(html, "html.parser")
	wtext = soup.select(".w_map span")[0].text
	#print(wtext)
	s = wtext
	integ = ''
	for n in s:
		if n.isdigit():
			integ = integ + n
		else:
			integ = integ + ' '
	if "+" in s:
		ww = "+"+integ
		www = ww.replace(' ', ' ')
		bot.sendMessage(chat_id = update.message.chat_id, text=www)
	else:
		zz = "-"+integ
		zzz = zz.replace(' ', '')
		bot.sendMessage(chat_id = update.message.chat_id, text=zzz)

	s = wtext
	if "+"  in s:
		h = "Можно одеться полегче"
		bot.sendMessage(chat_id = update.message.chat_id, text=h)
	elif "0" in s:
		hh = "Можно одеться полегче"
		bot.sendMessage(chat_id = update.message.chat_id, text=hh)
	else: 
		hhh = "Оденься потеплее"
		bot.sendMessage(chat_id = update.message.chat_id, text=hhh)

	xtext = soup.select(".p_data span br")[0].text
	if "без осадков" in xtext:
		q = "Зонт не нужен"
		bot.sendMessage(chat_id = update.message.chat_id, text=q)
	else:
		pass
		# qq = "Бери зонт"
		# bot.sendMessage(chat_id = update.message.chat_id, text=qq)
	if "снег" in xtext:
		r = "Одевай шапку"
		bot.sendMessage(chat_id = update.message.chat_id, text=r)
	else:
		rr = "Можно без шапки"
		bot.sendMessage(chat_id = update.message.chat_id, text=rr)
	if "Ясно" in xtext:
		t = "Будет солнечно, бери очки"
		bot.sendMessage(chat_id = update.message.chat_id, text=t)
	else:
		pass
	if "осадки" in xtext:
		tt = "Обещают дождик, захвати зонт"
		bot.sendMessage(chat_id = update.message.chat_id, text=tt)
	else:
		pass

karaganda_handler = CommandHandler('karaganda',karaganda)
dispatcher.add_handler(karaganda_handler)




updater.start_polling()