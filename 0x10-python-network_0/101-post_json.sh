#!/bin/bash
# Post json
curl -sL -X POST "$1" -H "Content-Type: application/json" -d @"$2"
