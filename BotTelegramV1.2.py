import telebot

bot = telebot.TeleBot('5851421698:AAHVQ49EVYvca4gPZKqTrz2rOhlC2uBXAP4')

# Menghandle Pesan /Start
@bot.message_handler(commands=['hai'])
def welcome(message):
    #membalas pesan
  bot.reply_to(message, "Halo bro, ada apa?")

@bot.message_handler(commands=['image','foto'])
def image(message):
    chat = message.chat.id
    bot.send_photo(chat, open('pxfuel.jpg','rb'))

@bot.message_handler(commands= ['start','help'])
def help(message):
    bot.reply_to(message, "KATA PERINTAH YANG DAPAT DIGUNAKAN PADA BOT INI : \n1./help = Untuk memberikan bantuan.\
                \n2. /hai = untuk menyapa anda.\n3./foto atau /image = bot akan mengirim foto kepada anda.")
print("Bot Berjalan")
    


while True :
    try:
        bot.polling()
    except :
        pass
