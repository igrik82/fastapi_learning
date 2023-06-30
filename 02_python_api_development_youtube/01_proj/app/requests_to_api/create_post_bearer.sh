#!/usr/bin/env bash

curl $1 -w '\n' -L -X POST http://192.168.88.226:8888/posts \
    -H 'Content-Type: application/json' \
    -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoyLCJleHAiOjE2ODgxMTU1NDh9.JZnCxJUogfL24ZsU5NUq4SyuuB01vlo2-g6ywAFcu18' \
    -d '{"title": "curl", "content": "curl"}'
