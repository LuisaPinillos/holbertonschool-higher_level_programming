#!/bin/bash
# script that sends a POST request to the passed URL with some variables.
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" $1
