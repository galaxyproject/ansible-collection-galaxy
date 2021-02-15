# Ansible Collection - galaxyproject.galaxy

Documentation for the collection.

# WIP how to use

```console
$ git clone https://github.com/galaxyproject/ansible-collection-galaxy.git
$ cd ansible-collection-galaxy
$ ansible-galaxy collection build ansible-collection-galaxy
$ mkdir collection-test
$ cd collection-test
$ ansible-galaxy collection install -p ./collections ../galaxyproject-galaxy-1.0.0.tar.gz
```

Make a playbook like:

```yaml
- hosts: all
  roles:
    - galaxyproject.galaxy.user
```

And a suitable inventory for wherever you want to deploy. Run your playbook for fun and profit.
