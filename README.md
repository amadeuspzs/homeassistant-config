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

## Tasmota [config](https://tasmota.github.io/docs/Commands/)

1. `TelePeriod 1` == `TelePeriod 300`
2. `PowerDelta 110` = report on 10W change
3. `SetOption65 1` = disable reset on power cycle
4. `SetOption19 0` = tasmota discovery, 1 = mqtt (deprecated)

Latch timer for "boosts":

1. `Rule1 1` - enable the rule we're about to create
2. `SwitchTopic 0` - disable MQTT messages about this switch (seems to prevent the rule working)
3. `SwitchMode 2` - inverted switch - sends an on signal when released (falling edge)
4. The rule itself - when the switch is on, turn on and set a 1800 second timer (30 mins). When the timer runs out, turn off. Note if activated again the timer is reset to 30 mins:
```
Rule1
  ON Switch1#state=1 DO Backlog Power1 on; RuleTimer1 1800 ENDON
  ON Rules#Timer=1 DO Power1 off ENDON
  ON Switch1#state=0 DO ENDON
```

## Backups

1. Daily backups through automation
2. Remove backups older than 30 days (crontab): `find /home/homeassistant/.homeassistant/backups -type f -mtime +30 -delete`
