#!/bin/bash
docker build -t police_auction_watch:latest . #> /dev/null
# Pipe stdin into docker run, mount the state folder to persist runs
docker run -v "$(pwd)/state:/home/app/code/state" -i police_auction_watch <&0
