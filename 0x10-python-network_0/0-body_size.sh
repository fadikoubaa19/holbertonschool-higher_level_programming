#!/bin/bash
# the size of content
curl -sI "$1" | grep "Content-Length:" | cut -d " " -f 2
