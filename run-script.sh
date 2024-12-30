#!/bin/bash

python3 -m http.server&

while true; do
    python3 simple-parse.py
    sleep 3600  # Sleep for one hour
done
