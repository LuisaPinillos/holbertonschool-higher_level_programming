#!/bin/bash
# script that sends a DELETE request to the URL
curl -sI -X OPTIONS $1 | grep -i 'allow' | cut -d " " -f2
