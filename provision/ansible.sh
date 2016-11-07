#!/bin/bash

yum -d0 -y install epel-release
yum -d0 -y install ansible python-pip python-devel libevent-devel python-setuptools

pip install --upgrade pip
pip install --upgrade setuptools

git clone https://github.com/ansible/ansible-container.git
git clone https://github.com/ansible/ansible-container-examples.git

chown vagrant:vagrant -R ansible-container ansible-container-examples

cd ansible-container
pip install .
cd ..

ansible --version
ansible-container version
