#!/bin/bash
# Bash script to send a request and display the status code

curl -s -I -o /dev/null -w "%{http_code}" "$1"
