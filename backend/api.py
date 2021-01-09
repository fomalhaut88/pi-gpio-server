from flask import Flask, jsonify, request
from flask_cors import CORS
import RPi.GPIO as GPIO


RESERVED_PINS = [1, 2, 4, 6, 9, 14, 17, 20, 25, 27, 28, 30, 34, 39]
GPIO.setmode(GPIO.BOARD)
DIRECTIONS = {}


app = Flask(__name__)
CORS(app)


@app.route('/pins/<int:pin>', methods=["GET", "POST"])
def pins(pin):
    if pin in RESERVED_PINS:
        return "Reserved pin", 403

    if request.method == "GET":
        value = GPIO.input(pin)
        direction = DIRECTIONS[pin]
        return jsonify(value=value, direction=direction)

    elif request.method == "POST":
        direction = request.json.get('direction')
        value = request.json.get('value')

        if direction is not None:
            if direction != DIRECTIONS[pin]:
                set_pin_direction(pin, direction)

        if value is not None:
            if DIRECTIONS[pin] == 'out':
                GPIO.output(pin, value)

        return jsonify(success=True)


def configure_gpio(direction):
    for pin in range(1, 41):
        if pin not in RESERVED_PINS:
            set_pin_direction(pin, direction)


def set_pin_direction(pin, direction):
    if direction == 'in':
        GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    elif direction == 'out':
        GPIO.setup(pin, GPIO.OUT, initial=0)
    else:
        raise ValueError(f"Invalid direction: {direction}")
    DIRECTIONS[pin] = direction


configure_gpio('out')


if __name__ == "__main__":
    app.run()
