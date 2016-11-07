#!/bin/bash

# [ -f /vagrant/provision/ansible.sh ] && bash /vagrant/provision/ansible.sh
[ -f /vagrant/provision/keys.sh ] && bash /vagrant/provision/keys.sh

yum -d0 -y install vim telnet

: Installing OSE all-in-one with ADB
while ! /usr/bin/sccli openshift ; do sleep 5 ; done

docker version
docker ps
oc version
