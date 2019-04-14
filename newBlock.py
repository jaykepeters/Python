#!/usr/bin/env python
import time, os, re, json

class Block:
    # Initialize the Object
    originalDef = ""
    def __init__(self):
        self.didInput = False
        self.definition = {
                "domain": "",
                "type": "",
                "start": "",
                "stop": ""
            }
        self.blockChoices = ["exact", "wildcard", "regex"]
        self.substitution = {"wildcard":"wild"}

    def printJSON(self):
        JSON = json.dumps(self.definition)
        parsedJSON = json.loads(JSON)
        prettyJSON = json.dumps(parsedJSON, indent=4, sort_keys=True, ensure_ascii=False)
        print(prettyJSON)

    def printInfo(self):
        print("Blocking Information")
        for key in self.definition:
            print(key.title() + ": " + self.definition[key])

    # Modifies the Template 
    def setVals(self):
        nullCounter = 0
        while True:
            domain_input = self.definition['domain'] = raw_input("Enter Domain: ")
            type_input = self.definition['type'] = raw_input("Enter Block Type: ")
            start_input = self.definition['start'] = raw_input("Enter Start Time: ")
            stop_input = self.definition['stop'] = raw_input("Enter Stop Time: ")
            for key in self.definition:
                val = self.definition[key]
                if val == "":
                    nullCounter = nullCounter + 1
                    domain_input
                    print(key + " is null")
            print(nullCounter)
            nullCounter = 0

# New Instance 
newObject = Block()

newObject.setVals()
newObject.printJSON()

# All done, delete
del newObject


def validate():
    string = ""
    if not re.match(r"([0-9]|0[0-9]|1[0-9]|2[0-3]):([0-5][0-9])\s*([AaPp][Mm])", string):
        return 1
    else:
        return 0

validate()