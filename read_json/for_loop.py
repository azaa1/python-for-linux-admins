# Python program to read JSON file

import json

# Opening JSON File
f = open('employee_data.json',)

# Return JSON as a dictionary
data = json.load(f)

# Iterating through the json list
for i in data['emp_details']:
    print(i)

# Closing file
f.close()