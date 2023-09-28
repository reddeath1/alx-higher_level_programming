#!/bin/bash
# Bash script to extract the HTTP status code from a previous curl request

# Check if an argument (the previous response) is provided
if [ $# -ne 1 ]; then
  echo "Usage: $0 <previous_response>"
  exit 1
fi

# Extract the HTTP status code using awk
http_code=$(echo "$1" | awk '{print $NF}')

# Display the status code
echo "Status code: $http_code"
