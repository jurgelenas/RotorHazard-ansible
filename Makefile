.PHONY: ping
ping:
	ansible all -i inventory.yaml -m ping

.PHONY: setup
setup:
	ansible-playbook -i inventory.yaml ./playbooks/rotorhazard.yaml

.PHONY: install
install:
	ansible-galaxy install infothrill.rpi_boot_config,4.3.0
