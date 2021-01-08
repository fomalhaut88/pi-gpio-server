from flask import Flask, jsonify, request
from flask_cors import CORS
import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BOARD)
DIRECTIONS = {}


app = Flask(__name__)
CORS(app)


@app.route('/pins/<int:pin>', methods=["GET", "POST"])
def pins(pin):
    if request.method == "GET":
        value = GPIO.input(pin)
        direction = DIRECTIONS[pin]
        return jsonify(value=value, direction=direction)

    elif request.method == "POST":
        direction = request.json.get('direction')
        value = request.json.get('value')

        if direction is not None:
            if direction != DIRECTIONS[pin]:
                gpio_direction = getattr(GPIO, direction.upper())
                GPIO.seput(pin, gpio_direction)
                DIRECTIONS[pin] = direction

        if value is not None:
            if DIRECTIONS[pin] == 'out':
                GPIO.output(pin, value)

        return jsonify(success=True)


def configure_gpio(direction):
    global DIRECTIONS
    for pin in range(1, 41):
        gpio_direction = getattr(GPIO, direction.upper())
        GPIO.seput(pin, gpio_direction)
        DIRECTIONS[pin] = direction


if __name__ == "__main__":
    configure_gpio('out')
    app.run()
