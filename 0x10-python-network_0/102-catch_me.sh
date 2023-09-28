#!/bin/bash
# Bash script to make a request that triggers the server's response

curl -s -X PUT -H "Origin: HolbertonSchool" -d "user_id=98" "0.0.0.0:5000/catch_me"
