#!/bin/bash

export PKG_DIR="python"

rm -rf ${PKG_DIR} && mkdir -p ${PKG_DIR}

poetry export --format=requirements.txt --without-hashes --output=${PWD}/requirements.txt
docker run --platform=linux/arm64 --rm -v $(pwd):/foo -w /foo \
  mlupin/docker-lambda:python3.9-build /bin/bash -c \
  "pip install -r requirements.txt -t ${PKG_DIR}"

rm -rf ./python/*dist-info/
zip -r lambda_layer.zip .

rm -rf ${PKG_DIR}