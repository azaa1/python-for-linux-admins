import os, os.path

folder = r'/c/Users/ahmad/Desktop/aKumoTechnology/python-for-linux-admins'
file = 'ls.py'

if os.path.exists(os.path.join(folder, file)):
    print('File exists')
else:
    print('File does not exist')