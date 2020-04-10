import telegram

bot = telegram.Bot(token = '1181502709:AAESeEpf46yrKkyKdIvTH2cUdbtDgySAM-w')

# for i in bot.getUpdates():
#     print(i.message)

bot.sendMessage(chat_id=1053225234, text="test.")
