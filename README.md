![Python Version](https://img.shields.io/badge/Python-3.10.9-blue.svg)
![Pip Version](https://img.shields.io/badge/Pip-22.3.1-yellow.svg)
![HA Version](https://img.shields.io/badge/HA-2023.1.7-green.svg)

[![Check HA config](https://github.com/amadeuspzs/homeassistant-config/actions/workflows/config-check.yaml/badge.svg)](https://github.com/amadeuspzs/homeassistant-config/actions/workflows/config-check.yaml)

# Homeassistant core configuration

> Linux nuc 4.15.0-202-generic #213-Ubuntu SMP Thu Jan 5 19:19:12 UTC 2023 x86_64 x86_64 x86_64 GNU/Linux

```
DISTRIB_ID=Ubuntu
DISTRIB_RELEASE=18.04
DISTRIB_CODENAME=bionic
DISTRIB_DESCRIPTION="Ubuntu 18.04.6 LTS"
```

## Getting started

1. Setup HA as per https://www.home-assistant.io/installation/linux#install-home-assistant-core (accessed Feb 2023)
2. Login as homeassistant user: `sudo -u homeassistant -s -H`
3. Activate virtualenv: `source /srv/homeassistant/bin/activate`
4. Add recent sqlite path: `export LD_LIBRARY_PATH=/srv/sqlite/lib`
5. Run `hass`

## Manual items

These do not appear to be stored in configuration files:

1. User configuration
2. MQTT integration
3. Tasmota integration
4. [HACS](https://hacs.xyz/docs/setup/download)
5. [Lovelace auto-entities](https://github.com/thomasloven/lovelace-auto-entities)
6. Naming of some entities e.g. attic radiators
7. [Rointe integration](https://github.com/tggm/rointe-hacs)

Config for sensors, where sensors are stored in `sensors.json` is generated via https://github.com/amadeuspzs/ha-config
