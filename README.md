# dashboard-bot3
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Dashboard du bot Discord actif 🚀"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
