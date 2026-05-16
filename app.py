from flask import Flask
import requests

app = Flask(__name__)

@app.route("/")
def home():

    url = "https://api.trongrid.io/v1/transactions"

    r = requests.get(url)
    data = r.json()

    txs = data["data"]

    for tx in txs:

        try:
            contract = tx["raw_data"]["contract"][0]

            if contract["type"] == "TransferContract":

                value = contract["parameter"]["value"]

                amount = value["amount"] / 1000000

                wallet = value["to_address"]

                txhash = tx["txID"]

                return {
                    "amount": amount,
                    "hash": txhash,
                    "wallet": wallet
                }

        except:
            pass

    return {"error": "No TRX transaction found"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
