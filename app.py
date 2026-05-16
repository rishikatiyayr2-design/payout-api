from flask import Flask
import requests

app = Flask(__name__)

@app.route("/")
def home():
    try:
        url = "https://apilist.tronscanapi.com/api/transaction"

        params = {
            "sort": "-timestamp",
            "count": "true",
            "limit": 20,
            "start": 0
        }

        response = requests.get(url, params=params).json()

        txs = response["data"]

        trx_tx = None

        for tx in txs:

            # Sirf TRX transfer
            if tx.get("contractType") == 1:

                trx_tx = tx
                break

        if not trx_tx:
            return {"error": "No TRX transaction found"}

        hash_value = trx_tx["hash"]

        wallet = trx_tx["toAddress"]

        amount = round(
            float(trx_tx["amount"]) / 1000000,
            2
        )

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
