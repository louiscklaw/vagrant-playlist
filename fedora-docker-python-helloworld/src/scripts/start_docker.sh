#!/usr/bin/env bash

set -ex

docker run -it \
  -v $PWD:/app \
  -w /app \
  -p 3000:3000 \
  -p 8888:8888 \
  -u 1000:1000 \
  --rm \
  logickee/ych1990101_jupyter:latest \
  bash
