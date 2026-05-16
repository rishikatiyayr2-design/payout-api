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
            "limit": 50,
            "start": 0
        }

        response = requests.get(url, params=params).json()

        txs = response["data"]

        final_tx = None

        for tx in txs:

            # Sirf TRX transfer
            if tx.get("contractType") == 1:

                amount = float(tx["amount"]) / 1000000

                # 5 se 50 TRX only
                if amount >= 5 and amount <= 50:

                    final_tx = tx
                    break

        if not final_tx:
            return {"error": "No suitable TRX transaction found"}

        hash_value = final_tx["hash"]

        wallet = final_tx["toAddress"]

        amount = round(
            float(final_tx["amount"]) / 1000000,
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
