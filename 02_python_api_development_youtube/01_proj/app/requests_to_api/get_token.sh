#!/usr/bin/env bash

if [[ -z "$1" || "$#" -ne 4 ]]; then
    echo "Use option -e email@email.com -p password."
    exit 1
fi


while getopts "e:p:" opt; do
    case $opt in
    e)
        EMAIL=${OPTARG};;
    p)
        PASSWORD=${OPTARG};;
    *)
        echo "Invalid option! Use -e email@email.com -p password."
        exit 1;;


    esac
done


curl --silent -L -X POST http://192.168.88.226:8888/auth \
    -H 'accept: application/json' \
    -H 'Content-Type: application/x-www-form-urlencoded' \
    -d "grant_type=&username=${EMAIL}&password=${PASSWORD}" \
    | jq -r '.token' > token
