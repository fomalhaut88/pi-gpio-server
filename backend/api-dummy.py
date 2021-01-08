from random import choice

from flask import Flask, jsonify, request
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


@app.route('/pins/<int:pin>', methods=["GET", "POST"])
def pins(pin):
    if request.method == "GET":
        value = choice([0, 1])
        return jsonify(value=value, direction='out')
    elif request.method == "POST":
        print(pin, request.json)
        return jsonify(success=True)


if __name__ == "__main__":
    app.run()
