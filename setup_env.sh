#!/bin/sh
# Simple environment setup script for the dodgeball game
python3 -m venv .venv
. .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

echo "Environment ready. Activate with: . .venv/bin/activate"
