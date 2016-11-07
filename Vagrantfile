# -*- mode: ruby -*-
# vi: set ft=ruby :

# read vm and chef configurations from JSON files
nodes_config_all = (JSON.parse(File.read("nodes.json")))['nodes']
nodes_config = nodes_config_all.select { |k,v| v['enabled'] == 'true' }

VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  nodes_config.each do |node|
    node_name   = node[0] # name of node
    node_values = node[1] # content of node

    config.vm.synced_folder ".", "/vagrant", type: "rsync", rsync__exclude: ".git/"

    config.vm.box = node_values[':box']

    config.hostmanager.enabled = true
    config.hostmanager.manage_host = true
    config.hostmanager.ignore_private_ip = false
    config.hostmanager.include_offline = true

    config.ssh.forward_x11 = true

    config.vm.define node_name do |config|
      config.vm.hostname = node_name
      config.vm.network :private_network, ip: node_values[':ip']

      config.vm.provider :virtualbox do |vb|
        vb.customize ["modifyvm", :id, "--memory", node_values[':memory']]
        vb.customize ["modifyvm", :id, "--name", node_name]

        # Enable use of more than one virtual CPU in a virtual machine.
        vb.customize ["modifyvm", :id, "--ioapic", "on"]
      end

      config.vm.provision :shell, :path => "provision/#{node[0]}.sh"
    end
  end
end
