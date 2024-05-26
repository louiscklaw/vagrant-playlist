#!/usr/bin/env bash
# Tomado del enlace --> https://docs.docker.com/engine/install/ubuntu/
#
# Fecha: 2021-03-25
#
if [ "" == "${1}" ]; then
  USUARIO="${USER}"
else
  USUARIO="${1}"
fi

echo ${USUARIO}

# sudo apt-get update

for pkg in docker.io docker-doc docker-compose docker-compose-v2 podman-docker containerd runc; do 
  sudo apt-get remove $pkg; 
done

sudo apt-get update
sudo apt-get install -y ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add the repository to Apt sources:
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update

sudo apt-get install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
sudo docker run hello-world

# echo "Adicionando el usuario [${USUARIO}] al grupo [docker]"
sudo usermod -aG docker ${USUARIO}

echo "docker install done"

# #docker compose
sudo curl -L "https://github.com/docker/compose/releases/download/2.26.1/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose


sudo apt-get install -y resolvconf
sudo chmod 777 /etc/resolvconf/resolv.conf.d/head
cat << EOF >> /etc/resolvconf/resolv.conf.d/head
nameserver 8.8.4.4
nameserver 8.8.8.8
EOF
sudo service resolvconf restart

