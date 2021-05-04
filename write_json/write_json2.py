#!/usr/bin/env python3

import json

data = {'people':[{'name': 'Anna', 'email': 'anna@testmail.com', 'title': 'DevOps'}]}

with open('data2.json', 'w') as outfile:
    json.dump(data, outfile, indent=4)