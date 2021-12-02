import telebot
from tbconfig import config
import yahoo_parser

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.send_message(
        message.chat.id, "{0.first_name}, Send me a ticker".format(message.from_user)
    )

@bot.message_handler(func=lambda message: True)
def send_fin_info(message):
    fin_info = yahoo_parser.get_fin_info(message.text)
    bot.send_message(
        message.chat.id, fin_info
    )


# RUN
bot.polling(none_stop=True)