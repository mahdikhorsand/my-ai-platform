import requests

url = "http://127.0.0.1:8000/auth/register"
data = {"name": "Mahdi", "contact": "mahdi@example.com"}

response = requests.post(url, json=data)
print(response.json())
