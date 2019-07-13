#!/bin/bash
host=$1
port=$2


while true
do
    printf "> hitting $host at port $port\n"
    printf "> Press ctrl+c to stop\n"
    curl $host:$port
    printf "\n> --- call completed ---\n"
done

