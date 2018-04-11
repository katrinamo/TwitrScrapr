#!/bin/bash

echo "Starting tweet fetching....."
printf "MeToo" | python searcher.py
echo "\n.\n.\n.\nFETCHING DONE."
echo "Starting frequency determination..."
python frequency.py
