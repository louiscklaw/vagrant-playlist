#!/usr/bin/env bash

set -x

sudo dnf remove docker \
  docker-client \
  docker-client-latest \
  docker-common \
  docker-latest \
  docker-latest-logrotate \
  docker-logrotate \
  docker-selinux \
  docker-engine-selinux \
  docker-engine

sudo dnf -y install dnf-plugins-core
sudo dnf config-manager --add-repo https://download.docker.com/linux/fedora/docker-ce.repo

sudo dnf -y install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

sudo systemctl start docker

sudo docker run hello-world

id
sudo usermod -aG docker vagrant
sudo usermod -aG dialout vagrant
id

echo "docker install done"

# # #docker compose
sudo curl -L "https://github.com/docker/compose/releases/download/2.26.1/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose

sudo systemctl enable docker

sudo reboot

# sudo apt-get install -y resolvconf
# sudo chmod 777 /etc/resolvconf/resolv.conf.d/head
# cat << EOF >> /etc/resolvconf/resolv.conf.d/head
# nameserver 8.8.4.4
# nameserver 8.8.8.8
# EOF
# sudo service resolvconf restart

