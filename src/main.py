import requests 
import os
import certifi

url = "https://api-comexstat.mdic.gov.br/general/details"

response = requests.get(url, verify= False)
status = response.status_code
dados = response.json()
print(dados)