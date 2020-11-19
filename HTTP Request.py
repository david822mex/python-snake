import requests
import json

URL = "http://127.0.0.1:8080/auth/login"
credentials = {
    "email": "david822@me.com",
    "password": "12345678"
}
res = requests.post(URL, credentials)

data = res.json()
with open("data/token.json", "w") as file:
    json.dump(data["user"], file, indent=4)
print(data)
