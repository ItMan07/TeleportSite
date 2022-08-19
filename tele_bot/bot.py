from telebot import telebot, types
from user import User
from tele_bot.config import *

bot = telebot.TeleBot(BOT_TOKEN)
user = User()


@bot.message_handler(commands=['start'])
def cmd_start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    btn1 = types.KeyboardButton('Сделать заказ')
    btn2 = types.KeyboardButton('Тех поддержка')
    markup.add(btn1, btn2)

    bot.send_message(message.chat.id, START_MESSAGE, parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def new_order1(message):
    if message.text == 'Сделать заказ':
        msg = bot.send_message(message.chat.id, '☎ Укажите пожалуйста номер телефона для связи')
        bot.register_next_step_handler(msg, new_order2)


def new_order2(message):
    user.number = message.text
    msg = bot.send_message(message.chat.id, '👤 Как к вам можно обращаться?')
    bot.register_next_step_handler(msg, new_order3)


def new_order3(message):
    user.name = message.text
    msg = bot.send_message(message.chat.id, '📬 Email-адрес')
    bot.register_next_step_handler(msg, new_order4)


def new_order4(message):
    user.email = message.text
    msg = bot.send_message(message.chat.id, '🕓 В какое время вам будет удобно говорить?')
    bot.register_next_step_handler(msg, new_order5)


def new_order5(message):
    user.time = message.text
    bot.send_message(message.chat.id, '✅ Отлично. Ваш запрос записан. \n\nОжидайте ответ от оператора')
    send_order(user)


def send_order(user_obj=None):
    bot.send_message(ADMIN_ID, f'🔔 Пришел новый заказ! Параметры заказа: \n\n'
                               f'👤 Имя: {user_obj.name}\n'
                               f'☎ Номер телефона: {user_obj.number}\n'
                               f'📬 Email: {user_obj.email}\n'
                               f'🕓 Время: {user_obj.time}')

# def main():
#     bot.infinity_polling()
#
#
# if __name__ == '__main__':
#     main()
