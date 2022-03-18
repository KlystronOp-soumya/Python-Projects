"""
api: https://pokeapi.co/api/v2/pokemon/{id or name}/
"""
import requests
import re

api = r'https://pokeapi.co/api/v2/pokemon/{pokemon}/'
pokemon="clefairy"

try:

    url=re.sub(r"{pokemon}",pokemon,api)
    print("After substitution: ",url)

    response = requests.get(url)
    print(response.url)
    print(response.status_code)
    print(response.json())
except Exception as e:
    print(e)