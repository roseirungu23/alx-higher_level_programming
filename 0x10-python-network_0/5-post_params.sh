#!/bin/bash
# Script that send POST request to url
curl -sX POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
