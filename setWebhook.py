import telegram

import os 

url = "https://backend2023f.pythonanywhere.com/webhook/"
# "5959656588:AAFRUBI1vozVI4ScI9HCVu3YRk2qd_6PjxQ"
TOKEN = "6217675093:AAFKzEEhkFi-nQqkrk7LTyyBgIyww7d8UtQ"

bot = telegram.Bot(token=TOKEN)

bot.delete_webhook()
print(bot.set_webhook(url))

print(bot.get_webhook_info())