#!/bin/bash
# Display all HTTP methods that the server will accept
curl -Is "$1" | grep Allow | cut -c 8-
