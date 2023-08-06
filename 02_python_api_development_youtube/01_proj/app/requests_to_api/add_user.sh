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

LOGIN=$(echo ${EMAIL} | cut -d "@" -f1)

JSON_BODY=$(cat <<EOF
{
    "login": "${LOGIN}",
    "email": "${2}",
    "password": "${4}"
}
EOF
)

curl --silent -X 'POST' \
    'http://192.168.88.226:8888/users/' \
    -H 'accept: application/json' \
    -H 'Content-Type: application/json' \
    -d "${JSON_BODY}"
