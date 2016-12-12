#  rest is a url based API
from flask import Flask, json, request
app = Flask(__name__)

@app.route("/mivtzaim")
def mivtzaim_shelanu():
    miv = {'milk':5.0, 'bread':7.9}
    return json.dumps(miv)

prices = {1111:5.0, 2222:7.9}
@app.route("/price/<int:barcode>")
def price(barcode):
    return str(prices[barcode])


@app.route("/price/<int:barcode>", methods=["POST"])
def price_chang(barcode):
    prices[barcode] = request.form["price"]
    return prices[barcode]


if __name__ == "__main__":
    app.run()