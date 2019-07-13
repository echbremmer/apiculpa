#!/bin/bash
host=$1
port=$2


while true
do
    echo "hitting $host at port $port"
    echo "Press ctrl+c to stop"
    curl $host:$port
    echo "--- call completed ---"
done

