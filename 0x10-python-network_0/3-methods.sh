#!/bin/bash
# script that displays all HTTP methods the server will accept.
curl -Xs OPTIONS $1 -i
