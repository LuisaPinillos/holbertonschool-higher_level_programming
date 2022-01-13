#!/bin/bash
# script that displays all HTTP methods the server will accept.
curl -sI $1 | grep -i 'allow' | cut -d " " -f2
