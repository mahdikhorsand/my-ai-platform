import requests

url = "http://127.0.0.1:8000/wallet/topup"
headers = {"x-tenant-apikey": "27d4543d2aad689e4ac0a83d2d1788a4"}
data = {"amount": 50}

response = requests.post(url, json=data, headers=headers)
print(response.json())
