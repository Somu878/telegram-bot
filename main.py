import time
import telebot

bot = telebot.TeleBot('2095775339:AAFHeNVYW9s6JbSuM4m_4D4NOcUUQc3EX7I')




@bot.message_handler(commands="time")
def helljkk(message):
    bot.send_message(message.chat.id, time.ctime())


@bot.message_handler(commands="hello")
def fhj(message):
    bot.reply_to(message, "hello!,how may i help u?")


@bot.message_handler(commands="whatcanudo")
def fhyd(message):
    bot.reply_to(message, "Send me anything, I will revert u..KINDA FUN!!")


@bot.message_handler(commands="whatisurname")
def fhdiyj(message):
    bot.reply_to(message, "I was a testBot, U can call me whatever u want... ")


@bot.message_handler(commands="start")
def helllmjkk(message):
    bot.send_message(message.chat.id , "hey! there, You are chatting with TEST_BOT45")

@bot.message_handler(func=lambda m: True)
def repeat(message):
    bot.send_message(message.chat.id, message.text)

bot.polling()
