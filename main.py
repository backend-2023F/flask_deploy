from flask import Flask, request
import requests
import telegram

TOKEN = "5959656588:AAFRUBI1vozVI4ScI9HCVu3YRk2qd_6PjxQ"
app = Flask(__name__)

@app.route("/webhook/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        chat_id = 5575549228
        payload = {
            "chat_id": chat_id,
            "text": "Hello World"
        }
        URL = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
        r = requests.post(URL, json=payload)

        print(r.json())
        return "OK"
    else:
        return "Not allowed GET request!"

@app.route("/arg/<number>", methods=["GET"])
def arg(number):
    print(type(number))
    return f"Number is {number}"


if __name__ == "__main__":
    app.run(debug=True)