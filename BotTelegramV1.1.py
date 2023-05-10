import telebot

bot = telebot.TeleBot('5851421698:AAHVQ49EVYvca4gPZKqTrz2rOhlC2uBXAP4')

# Menghandle Pesan /Start
@bot.message_handler(commands=['hai'])
def welcome(message):
    #membalas pesan
  bot.reply_to(message, "Halo bro, ada apa?")

@bot.message_handler(commands=['foto'])
def image(message):
    chat = message.chat.id
    bot.send_photo(chat, open('pxfuel.jpg','rb'))


print("Bot Berjalan")
    


while True :
    try:
        bot.polling()
    except :
        pass
