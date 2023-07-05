#!/usr/bin/env bash

if [[ -z "$1" || "$#" -ne 4 ]]; then
    echo "Use option -p post_id -v 0|1"
    exit 1
fi


while getopts "p:v:" opt; do
    case $opt in
    p)
        POST_ID=${OPTARG};;
    v)
        VOTE=${OPTARG};;
    *)
        echo "Use option -p post_id -v 0|1"
        exit 1;;
    esac
done

TOKEN=$(cat token)
JSON_BODY=$(cat <<EOF
{
    "post_id": ${POST_ID},
    "vote": ${VOTE}
}
EOF
)

curl --silent -L -X POST http://192.168.88.226:8888/votes \
    -H 'Content-Type: application/json' \
    -H "Authorization: Bearer ${TOKEN}" \
    -d "${JSON_BODY}" | jq
