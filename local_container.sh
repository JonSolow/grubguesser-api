set -e

docker build . \
    --tag dev-grubguesser-api \
&& docker run -it \
   --rm \
    --mount type=bind,source="$(pwd)/src",target=/opt/src \
    --env-file .env \
    -p 2000:5000 \
    dev-grubguesser-api \
    bash