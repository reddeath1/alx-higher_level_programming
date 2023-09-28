#!/bin/bash
# Bash script to send a request and display the status code

# Check if an argument (URL) is provided
if [ $# -ne 1 ]; then
  echo "Usage: $0 <URL>"
  exit 1
fi

# Use curl to send the request and display the status code
curl -s -I -o /dev/null -w "%{http_code}" "$1"
