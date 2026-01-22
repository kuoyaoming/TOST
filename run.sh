#!/bin/bash

echo "Starting Translategemma App..."
# Change to src directory so imports work naturally
cd src || exit 1
python3 app.py
