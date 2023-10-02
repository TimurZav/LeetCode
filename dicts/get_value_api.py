import json
import requests


header = {
    "Authorization": "Token 943297fcddf785fc56da07c131e20e9d1d449629"
}

response = requests.get("https://jetlend.ru/lend/api/export/1c/payments", headers=header)
print(response)

data = json.loads(response.text)

print(data)
print('')

