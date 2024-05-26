#!/usr/bin/env bash

set -x

pip install playwright

pip install -r requirements.txt
playwright install

jupyter notebook \
  --allow-root \
  --ip=0.0.0.0 \
  --notebook-dir=notebook
