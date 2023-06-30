#!/usr/bin/env bash

curl $1 -w '\n' -L -X POST http://192.168.88.226:8888/auth \
    -H 'accept: application/json' \
    -H 'Content-Type: application/x-www-form-urlencoded' \
    -d 'grant_type=&username=igrik82@gmail.com&password=123456'
