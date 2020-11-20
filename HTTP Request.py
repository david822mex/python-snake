import requests
import json

URL = "http://127.0.0.1:8080/auth/login"
credentials = {
    "email": "david822@me.com",
    "password": "12345678"
}
token = "alñkjdlajkñdlkña"
headers = {
    "Authorization": "Bear " + token
}
#  post requests
res = requests.post(url=URL, json=credentials, headers=headers)

data = res.json()
with open("data/token.json", "w") as file:
    json.dump(data["user"], file, indent=4)
print(data)


# get requests
params = {
    "name": "aldjlas",
    "apikey": "asjdlñajdl"
}
res2 = requests.get(url=URL, params=params, headers=headers)
