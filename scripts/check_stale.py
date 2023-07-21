#!/usr/bin/env python

import pandas as pd
import requests
import yaml
from hours_since_last_change import hours_since_last_change

# define your home assistant groups yaml location below:
yaml_file = "/home/homeassistant/.homeassistant/groups.yaml"

# define the group containing critical sensors
group_name = "critical"

# define default timeout, in hours
timeout_default = 8

timeout_override = { "sensor.hot_water" : 1, "sensor.kitchen_small_temperature": 10 }

with open(yaml_file, "r") as stream:
    try:
        data = yaml.safe_load(stream)
    except yaml.YAMLError as e:
        print(e)

if not group_name in data:
    print(f"'{group_name}' not found in {yaml_file}")
    exit(1)

sensors = (data[group_name]["entities"])

for sensor in sensors:
    last_changed = hours_since_last_change(sensor)
    timeout = timeout_override[sensor] if sensor in timeout_override else timeout_default
    if last_changed > timeout:
        response = requests.post(f"http://localhost:8124/api/webhook/-RwuPrAoOVcVGTQ505Aq_uPdA",data={'last_changed':last_changed, 'sensor':sensor})

