from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():

    return {

        "hash":"0x4b09a2e6eaf65ec118cef5cf86e486007c0e477854c74b9d49c6a8f4e098dae5",

        "wallet":"0xA3DBBF1C09d9835fD8117a913E702Cc91177B2A3",

        "amount":"20"

    }

app.run(host="0.0.0.0", port=10000)

