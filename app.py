from flask import Flask
import requests

app = Flask(__name__)

@app.route("/")
def home():
    try:
        url = "https://apilist.tronscanapi.com/api/new/token_trc20/transfers?limit=1&start=0&sort=-timestamp"

        response = requests.get(url).json()

        tx = response["token_transfers"][0]

        amount = float(tx["quant"]) / 1000000

        # Min-Max control
        if amount < 5:
            amount = 5

        if amount > 50:
            amount = 50

        wallet = tx["to_address"]
        hash_value = tx["transaction_id"]

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

