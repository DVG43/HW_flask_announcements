import requests

HOST = 'http://127.0.0.1:5000'

response = requests.get(HOST)
print(response.status_code)
print(response.text)

response = requests.get(f'{HOST}/test/')
print(response.status_code)
print(response.text)