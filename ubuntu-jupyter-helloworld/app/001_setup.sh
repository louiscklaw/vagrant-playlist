#!/usr/bin/env bash

set -x

sudo apt-get update

sudo apt-get install -qqy libnss3\
         libnspr4\
         libdbus-1-3\
         libatk1.0-0\
         libatk-bridge2.0-0\
         libcups2\
         libdrm2\
         libxkbcommon0\
         libatspi2.0-0\
         libxcomposite1\
         libxdamage1\
         libxfixes3\
         libxrandr2\
         libgbm1\
         libasound2

sudo apt-get install -qqy python3 python3-pip
