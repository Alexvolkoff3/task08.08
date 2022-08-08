import telebot
from config import token
from telebot.types import Message

bot = telebot.TeleBot(token)

@bot.message_handler()
def echo(message: Message):
    bot.send_message(message.chat.id, message.text)

bot.infinity_polling(skip_pending=True)