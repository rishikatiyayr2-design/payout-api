from flask import Flask
import requests

app = Flask(__name__)

@app.route("/")
def home():

    url = "https://apilist.tronscanapi.com/api/transaction?sort=-timestamp&count=true&limit=1&start=0"

    response = requests.get(url)

    data = response.json()

    tx = data["data"][0]

    txhash = tx["hash"]

    owner = tx["ownerAddress"]

    amount = 0

    try:
        amount = tx["contractData"]["amount"] / 1000000
    except:
        amount = 5

    return {

        "hash": txhash,

        "wallet": owner,

        "amount": str(amount)

    }

app.run(host="0.0.0.0", port=10000)
