from flask import Flask, render_template, request
from tele_bot.bot import *
import os

app = Flask(__name__)
user = User()


@app.route('/', methods=['POST', 'GET'])
def main():
    if request.method == "POST":
        user.email = request.form['email']
        user.name = request.form['name']
        user.number = request.form['number']
        user.time = request.form['time']

        # print(user.email, user.name, user.number, user.time)
        send_order(user)

    return render_template('index.html')


@app.route(f"/{BOT_TOKEN}", methods=["POST"])
def redirect_message():
    json_string = request.get_data().decode("utf-8")
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200


if __name__ == '__main__':
    bot.infinity_polling()
    app.run()
    # bot.remove_webhook()
    # bot.set_webhook(url=BOT_URL)
    #
    # app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
