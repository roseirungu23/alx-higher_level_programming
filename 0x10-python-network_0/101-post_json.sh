#!/bin/bash
# Sends a JSON POST request to url
curl -sLH "content-type:application/json" -d @"$2" -X POST "$1"
