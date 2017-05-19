import telergram
bot = telergram.Bot(token = '358896979:AAHL7UsgmCG7vMtApcA3GFrdYFlSahiVMIM')
updates = bot.getUpdates()
for update in updates:
	print(update.massage.text)
