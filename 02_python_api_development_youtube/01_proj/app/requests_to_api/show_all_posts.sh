#!/usr/bin/env bash

curl --silent -X 'GET' \
    'http://192.168.88.226:8888/posts/' \
    -H 'accept: application/json' | jq '.'
