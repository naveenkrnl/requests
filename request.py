import requests

# Making a get request
r = requests.get('https://httpbin.org/get', data={'key':'value'})

#check status code for response recieved
# success code - 200
print(r)

# print headers of request
print(r.headers)

# checking if request contains any content
print(r.content)