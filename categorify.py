#!/usr/bin/env python3
import requests, json

## Global Variables
baseurl = 'https://categorify.org/api?website='

def lookup(domain):
    url = '{}{}'.format(baseurl, domain)
    response = requests.get(url)

    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else:
        return None