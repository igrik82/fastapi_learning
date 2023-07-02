
#!/usr/bin/env bash

if [[ -z "$1" || "$#" -ne 2 ]]; then
    echo "Use option -n 1"
    exit 1
fi


while getopts "n:" opt; do
    case $opt in
    n)
        POST_NUM=${OPTARG};;
    *)
        echo "Invalid option! Use option -n 1"
        exit 1;;


    esac
done

TOKEN=$(cat token)

curl --silent -w '\n' -L -X DELETE http://192.168.88.226:8888/posts/${POST_NUM} \
    -H 'accept: */*' \
    -H "Authorization: Bearer ${TOKEN}" \
