#!/usr/bin/env bash

set -x

echo "# from fedora_bootstrap.sh" >> /etc/dnf/dnf.conf
echo "max_parallel_downloads=10" >> /etc/dnf/dnf.conf
echo "fastestmirror=True" >> /etc/dnf/dnf.conf

sudo dnf update && sudo dnf upgrade -y
