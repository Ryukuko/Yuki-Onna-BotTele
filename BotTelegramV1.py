import telebot

bot = telebot.TeleBot('5851421698:AAHVQ49EVYvca4gPZKqTrz2rOhlC2uBXAP4')

# Menghandle Pesan /Start
@bot.message_handler(commands=['start'])
def welcome(message):
    #membalas pesan
    bot.reply_to(message, "Halo bro, ada apa?")

while True :
    try:
        bot.polling()
    except :
        pass
