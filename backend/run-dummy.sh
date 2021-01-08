#!/bin/bash

export FLASK_ENV=production
export FLASK_SECRET_KEY=zahx4IleireiYou4edochee5vooh5Eij5Choqu4aiqueiShuY0
export FLASK_APP=api-dummy.py
export FLASK_PORT=5000

flask run --port $FLASK_PORT
