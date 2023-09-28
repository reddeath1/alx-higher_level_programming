#!/bin/bash
# Get request to the URL and display the body of the response
curl -sLX PUT -d "School" -H "Origin: You got me!" 0.0.0.0:5000/catch_me
