#!/bin/bash

[ -f /vagrant/provision/ansible.sh ] && bash /vagrant/provision/ansible.sh
[ -f /vagrant/provision/keys.sh ] && bash /vagrant/provision/keys.sh

yum -d0 -y install docker

docker version
docker ps
