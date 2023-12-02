#!/bin/bash
# Sends a request to URL and return the status code
curl -so /dev/null -w "%{http_code}" "$1"
