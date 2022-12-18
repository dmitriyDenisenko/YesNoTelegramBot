from telebot import TeleBot
import requests

bot = TeleBot('NULL FOR HAKERS')


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Я помогу тебе принять решение, да или нет. Возможно выбить "maybe", но шанс очень мал')

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if "?" in message.text:
        api_url = "https://yesno.wtf/api"
        data = requests.get(api_url).json()
        bot.send_message(message.chat.id, data.get("answer"))
        bot.send_animation(message.chat.id, data.get("image"))
    else:
        bot.send_message(message.chat.id, "Задай вопрос, я не могу ответить на предложение. НУЖНЫ ВОПРОСЫ!")

@bot.message_handler(content_types=['photo'])
def error(message):
    bot.send_message(message.from_user.id, "Нужен банальный вопрос текстом))")


@bot.message_handler(content_types=['voice'])
def error(message):
    bot.send_message(message.from_user.id, "Нужен банальный вопрос текстом))")

bot.polling(none_stop=True, interval=0)
