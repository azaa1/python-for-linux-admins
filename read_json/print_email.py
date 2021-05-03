# Python program to read JSON file

import json

# Opening JSON File
f = open('employee_data.json',)

# Return JSON as a dictionary
data = json.load(f)

# Iterating through the json list and find "anna" in "emp_name"
# and print email for "anna"
for i in data['emp_details']:
    if i["emp_name"] == "anna":
        print (i["email"])


# Closing file
f.close()