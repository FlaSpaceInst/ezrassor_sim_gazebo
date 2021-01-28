#!/bin/bash

python3 -m pip install --upgrade black flake8 && \
python3 -m black --check . && \
python3 -m flake8 .
