import requests

HOST = 'http://127.0.0.1:5000'

response = requests.get(HOST)
print(response.status_code)
print(response.text)

# response = requests.post(f'{HOST}/announsments/', json={'headline': 'car',
#                                                        'description': 'new BMW',
#                                                        'owner': 'Sasha',
#                                                        })
# print(response.status_code)
# print(response.text)

response = requests.get(f'{HOST}/announsments/2')
print(response.status_code)
print(response.text)

# response = requests.delete(f'{HOST}/announsments/2')
# print(response.status_code)
# print(response.text)