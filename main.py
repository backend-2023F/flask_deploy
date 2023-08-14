from flask import Flask, request
import requests
import telegram

TOKEN = "6217675093:AAFKzEEhkFi-nQqkrk7LTyyBgIyww7d8UtQ"
app = Flask(__name__)

@app.route("/webhook/", methods=["POST", "GET"])
def home():
    
    if request.method == "POST":
        data = request.get_json()
        print(data)
        chat_id = data['message']['chat']['id']
        text = data['message']['text']

        payload = {
            "chat_id": chat_id,
            "text": text
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