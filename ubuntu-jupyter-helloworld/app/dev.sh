#!/usr/bin/env bash

set -x

jupyter notebook \
  --allow-root \
  --ip=0.0.0.0 \
  --NotebookApp.token='' \
  --NotebookApp.password='' \
  --notebook-dir=notebook
