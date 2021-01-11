#!/bin/bash

python -m pip install --upgrade pip black flake8

python -m black --check .

python -m flake8 .