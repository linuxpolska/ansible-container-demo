#!/usr/bin/env python

# based on https://raw.githubusercontent.com/ansible/ansible/devel/contrib/inventory/ssh_config.py

import argparse
import os.path
import sys
import collections
import subprocess

from collections import MutableSequence

try:
    import json
except ImportError:
    import simplejson as json

AZ_CONF = 'az acs list'

_key = 'acs'

_az_to_ansible = [('linuxProfile_adminUsername', 'ansible_ssh_user'),
                  ('location', 'ansible_az_location'),
                  ('vmSize', 'ansible_az_vmsize'),
                  ('resourceGroup', 'ansible_az_group'),
                  ('provisioningState', 'ansible_az_provision'),
                  ('masterProfile_fqdn', 'ansible_host')]

def flatten(d, parent_key='', sep='_'):
    items = []
    for k, v in d.items():
        new_key = parent_key + sep + k if parent_key else k
        if isinstance(v, collections.MutableMapping):
            items.extend(flatten(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)

def get_config():

    data = subprocess.Popen(AZ_CONF, shell=True, stdout=subprocess.PIPE).stdout.read()
    dict = json.loads(data)
    new_dict = {}

    for entry in dict:
        #new_dict[entry['masterProfile']['fqdn']] = flatten(entry)
        new_dict[entry['name']] = flatten(entry)

    return new_dict

def print_list():
    cfg = get_config()
    meta = {'hostvars': {}}
    for alias, attributes in cfg.items():
        tmp_dict = {}
        for az_opt, ans_opt in _az_to_ansible:
            if az_opt in attributes:
                # If the attribute is a list, just take the first element.
                # Private key is returned in a list for some reason.
                attr = attributes[az_opt]
                if isinstance(attr, MutableSequence):
                    attr = attr[0]
                tmp_dict[ans_opt] = attr
        if tmp_dict:
            meta['hostvars'][alias] = tmp_dict

    print(json.dumps({_key: list(set(meta['hostvars'].keys())), '_meta': meta}))


def print_host(host):
    cfg = get_config()
    print(json.dumps(cfg[host]))


def get_args(args_list):
    parser = argparse.ArgumentParser(
        description='ansible inventory script parsing az acs list')
    mutex_group = parser.add_mutually_exclusive_group(required=True)
    help_list = 'list all hosts from az acs list'
    mutex_group.add_argument('--list', action='store_true', help=help_list)
    help_host = 'display variables for a host'
    mutex_group.add_argument('--host', help=help_host)
    return parser.parse_args(args_list)


def main(args_list):

    args = get_args(args_list)
    if args.list:
        print_list()
    if args.host:
        print_host(args.host)


if __name__ == '__main__':
    main(sys.argv[1:])
