import requests

url = "http://127.0.0.1:8000/api/ask"
headers = {"x-tenant-apikey": "27d4543d2aad689e4ac0a83d2d1788a4"}
data = {"user_id": "1", "prompt": "سلام"}

response = requests.post(url, json=data, headers=headers)
print(response.json())
