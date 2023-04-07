# RotorHazard Ansible Setup

This ansible project is designed to set up a Raspberry Pi to run the RotorHazard application for managing FPV drone
racing events. It has been tested only on Raspbian 32-bit operating system.

## Features

* `/boot/config.txt` setup
* Custom `rotorhazard.local` hostname for easy access through local network
* `hostapd` and `dnsmasqd` setup
* RTC Clock sync service
* Fan control - dynamic, temperature based for optimal cooling
* RotorHazard server installation & setup

## Installation

At this time this project is oriented towards advanced users who are already familiar with ansible.

You can find configuration options in [./playbooks/rotorhazard.yml](./playbooks/rotorhazard.yaml)

Available `make` commands:

* `make install` - install ansible dependencies from ansible galaxy
* `make ping` - ping all hosts from [./inventory.yml](./inventory.yaml) to test connectivity
* `make setup` - Run all Ansible playbooks required to set up the RotorHazard environment on Raspberry Pi

Note: we change the default hostname from `raspberrypi.local` to `rotorhazard.local` using ansible. After the initial
setup, to connect to the raspberrypi change the hostname to `rotorhazard.local` in `./inventory.yml`.

## Credits

https://github.com/RomkaV/RotorHazard-ansible

## License

This project is licensed under the GPL V3 License. Please see the [LICENSE](./LICENSE) file for more information.
