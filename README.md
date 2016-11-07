## Red Hat Forum 2016 Warsaw Ansible+Docker Workshops

Event will be held at 2016-11-08 14:20 CET.

Discover how Ansible and Docker enables the process of container
life cycle. Deploy and manage your infrastructure and applications
from single management workstation. Participants will learn how
to effectively use Ansible playbooks for reliable automation and
compliance.

Bring your own laptop with VirtualBox installed - this interactive
workshop will employ Ansible, Vagrant and Red Hat Container Development
Kit to bootstrap test invironments in just a few minutes!

### Vagrant Plug-ins

This project requires the Vagrant vagrant-hostmanager plugin to be
installed. The Vagrantfile uses the vagrant-hostmanager plugin to
automatically ensure all DNS entries are consistent between guests as
well as the host, in the `/etc/hosts` file. An example of the modified
`/etc/hosts` file is shown below.

You can manually run `vagrant hostmanager` to update `/etc/hosts` at
anytime.

```sh
vagrant plugin install vagrant-hostmanager
```

This might as well be handy to not to get asked for password repeatedly:
```
echo "$LOGNAME ALL=(ALL) NOPASSWD: $(which cp) $HOME/.vagrant.d/tmp/hosts.local /etc/hosts" | sudo tee /etc/sudoers.d/vagrant-hostmanager
```

### Lab Replay

Replay this lab at home by following easy steps:

1. Register free account on Docker Hub: https://hub.docker.com/
2. Install Vagrant: https://www.vagrantup.com/downloads.html
3. Add vagrant-hostmanager plugin: ```vagrant plugin install vagrant-hostmanager```
4. Download this repository (green button in top right corner of github page)
5. Setup your environment and provision lab VMs in one step: ```vagrant up```
6. Login onto "developement" VM: ```vagrant ssh docker.lab.example.com```
   1. We will use example Wordpress (app+database) docker set: ```cd ansible-container-examples/wordpress```
   2. Examine set of containers (```container.yml```) and provided ansible playbook (```main.yml```)
   3. First we build our images: ```ansible-container build```
   4. Now we can run them (interactively, or with ```-d``` option - in backgroud): ```ansible-container run [-d]```
   5. (Point your browser to http://docker.lab.example.com and play with Wordpress demo)
   6. Login from your developement to Docker Hub: ```docker login```
   7. Push your applications to Docker Hub: ```ansible-container push```
   8. Examine pushed images (check "Tags" tab) on Docker Hub: https://hub.docker.com/
   9. Create production-ready recipes for Openshift: ```ansible-container shipit openshift --save-config```
   10. Transfer created recipes to your "production" server: ```sudo rsync -a ansible/shipit_config/openshift vagrant@openshift.lab.example.com:```
7. Now login onto "production" VM: ```vagrant ssh openshift.lab.example.com```
   1. Create services: ```oc create -f openshift/```
   2. Get services information: ```oc get service```
   3. Get pods information: ```oc get pods```
   4. Notice how application and database images has been pulled from Docker Hub repository.
   5. Get instance information (Your instance ID will differ slightly): ```oc describe pod wordpress-1-k7a5e```
   6. (Point your browser to https://openshift.lab.example.com:8443/ (l/p: admin/admin) and check service status, find link to Your Wordpress instance and play with it)
8. Once complete cleanup your lab environment: ```vagrant destroy```
9. Try other examples by yourself, explore, research and... have fun!

### References

- https://raw.githubusercontent.com/projectatomic/adb-atomic-developer-bundle/master/components/centos/centos-k8s-singlenode-setup/Vagrantfile
- http://alesnosek.com/blog/2016/09/12/first-impressions-about-ansible-container/

