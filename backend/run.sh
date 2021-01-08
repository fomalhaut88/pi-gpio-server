#!/bin/bash

export FLASK_ENV=production
export FLASK_SECRET_KEY=zahx4IleireiYou4edochee5vooh5Eij5Choqu4aiqueiShuY0
export FLASK_APP=api.py
export FLASK_PORT=5000

source ./.venv/bin/activate
flask run --port $FLASK_PORT
