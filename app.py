from flask import Flask
import requests
import random

app = Flask(__name__)

@app.route("/")
def home():
    try:
        # Latest TRX transaction
        url = "https://apilist.tronscanapi.com/api/transaction"

        params = {
            "sort": "-timestamp",
            "count": "true",
            "limit": 1,
            "start": 0
        }

        response = requests.get(url, params=params)

        data = response.json()

        tx = data["data"][0]

        hash_value = tx["hash"]

        wallet = tx["toAddress"]

        amount = round(random.uniform(5, 50), 2)

        return {
            "amount": str(amount),
            "wallet": wallet,
            "hash": hash_value
        }

    except Exception as e:
        return {
            "error": str(e)
        }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)


