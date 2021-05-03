# Python program to read JSON file

import json

# Opening JSON File
f = open('employee_data.json',)

# Return JSON as a dictionary
data = json.load(f)

# Iterating through the json list and find "john" in "emp_name"
for i in data['emp_details']:
    if i["emp_name"] == "john":
        print ('Found')


# Closing file
f.close()