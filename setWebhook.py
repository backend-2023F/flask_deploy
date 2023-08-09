import telegram

import os 

url = "https://backend2023f.pythonanywhere.com/webhook/"
TOKEN = "5959656588:AAFRUBI1vozVI4ScI9HCVu3YRk2qd_6PjxQ"

bot = telegram.Bot(token=TOKEN)


bot.delete_webhook()
bot.set_webhook(url)
print(bot.get_webhook_info())