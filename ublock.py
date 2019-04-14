#!/usr/bin/env python
# Import Modules
import os
import io
import time
import json

# Define Global Variables
timestamp = time.strftime('%H:%M')
file = '/tmp/config.json'


# Define Functions
def loadConfig(file):
    # Globals
    global config_dict
    with open(file, 'r') as f:
        config_dict = json.load(f)

def block(input, type):
    # Check for block type
    if type == "exact":
        string = "-b"
    elif type == "wildcard":
        string = "--wild"
    elif type == "regex":
        string = "--regex"
    else:
        print("ERROR")
    # Build the Command
    cmd = "pihole " + string + " " + input
    print(cmd)

# def unblock(domain, type):


# Initialize Arrays
config = []

# Load the Configuration
loadConfig(file)

# Append all lines to an array
for line in config_dict:
    config.append(line)

# Configure Time-based Blocking
for section in config:
    domain = section['domain']
    blockType = section['type']
    startTime = section['start']
    stopTime = section['stop']

class PPC:
    @staticmethod
    def delete(domain):
        try:
            for section in config:
                    find = section['domain']
                    if find == domain:
                        print("Match Found: " + domain)
                        print("Deleting" + " " + domain)
                        config.remove(section)
                        global conf
                        conf = json.dumps(config)
                        parsedJSON = json.loads(conf)
                        prettyJSON = json.dumps(parsedJSON, indent=4, sort_keys=True, ensure_ascii=False)
                        with io.open(file, 'w', encoding='utf-8') as f:
                            f.write(prettyJSON)
        except:
            print("ERROR")
PPC = PPC()
PPC.delete("nigil.com")