#!/bin/bash
# flake8: noqa

python3 -m pip install --upgrade pip black flake8 && \
python3 -m black --check . && \
python3 -m flake8 .