#!/bin/bash
# Bash script to make a request that triggers the server's response
curl -sLX PUT -d "user_id:98" -H "Origin: School" 0.0.0.0:5000/catch_me
