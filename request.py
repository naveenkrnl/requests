import requests

# Making a put request
response = requests.get('https://api.github.com')

# checking if request contains any content
print(response.content)