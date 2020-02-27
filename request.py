# import requests module
import requests

# Making a get request
response = requests.get('https://api.github.com')

# print response
print(response)

# print encoding time
print(response.encoding)
