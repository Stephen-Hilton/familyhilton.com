#!/bin/bash
. ./build.sh

# Serve the content using Python's built-in HTTP server, for local testing
python3 -m http.server 8000 --directory ${PUBPATH}
