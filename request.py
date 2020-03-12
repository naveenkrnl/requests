# import requests module
import requests

# create a session object
s = requests.Session()

# set username and password
s.auth = ('user', 'pass')

# update headers
s.headers.update({'x-test': 'true'})

# both 'x-test' and 'x-test2' are sent
s.get('https://httpbin.org/headers', headers={'x-test2': 'true'})

# print object
print(s)