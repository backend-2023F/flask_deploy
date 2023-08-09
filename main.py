from flask import Flask, request

TOKEN = "5959656588:AAFRUBI1vozVI4ScI9HCVu3YRk2qd_6PjxQ"
app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return f"Bot: {TOKEN}"

