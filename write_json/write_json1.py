#!/usr/bin/env python3

import json

data = {}
data['people'] = []

data['people'].append({
    'name': 'anna',
    'email': 'anna@testmail.com',
    'title': 'CloudEngineer'
})
data['people'].append({
    'name': 'bob',
    'email': 'bob@testmail.com',
    'title': 'SystemEngineer'
})

with open('data.json', 'w') as outfile:
    json.dump(data, outfile, indent=4)
