FROM python:latest

RUN apt update && \
      apt install -y git && \
      useradd -m docker_user && \
      chown -R docker_user: /home/docker_user

RUN mkdir -p /home/docker_user/.local
RUN mkdir -p /home/docker_user/.local/bin
RUN mkdir -p /home/docker_user/.local/lib
RUN mkdir -p /home/docker_user/.cache
ENV PATH="/home/docker_user/.local/bin:${PATH}"

RUN chown 1000:1000 -R /home/docker_user

RUN apt-get update && apt-get install -qqy libnss3\
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

USER docker_user
WORKDIR /app

