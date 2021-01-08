#!/bin/bash

PYTHON_INTERPRETER=python3

if [ ! -d .venv ]; then
    $PYTHON_INTERPRETER -m pip install virtualenv
    $PYTHON_INTERPRETER -m virtualenv .venv
fi

./.venv/bin/pip install -r requirements.txt
