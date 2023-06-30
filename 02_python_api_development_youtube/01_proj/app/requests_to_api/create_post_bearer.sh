#!/usr/bin/env bash

TOKEN=$(cat token)
TITLE=$(shuf -n1 words.txt | tr '\n' ' ')
CONTENT=$(shuf -n3 words.txt | tr '\n' ' ')
JSON_BODY=$(cat <<EOF
{
    "title": "${TITLE%?}",
    "content": "${CONTENT%?}"
}
EOF
)

curl $1 -w '\n' -L -X POST http://192.168.88.226:8888/posts \
    -H 'Content-Type: application/json' \
    -H "Authorization: Bearer ${TOKEN}" \
    -d "${JSON_BODY}"
