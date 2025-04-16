import requests
import pandas as pd
import json

url = "https://api-comexstat.mdic.gov.br/cities"

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}

payload = {
    "flow": "import",
    "monthDetail": True,
    "period": {
        "from": "2023-01",
        "to": "2024-12"
    },
    "filters": [
        {
      "filter": "state",
      "values": [
        26
      ]
    }
    ],
    "details": ["country", "state"],
    "metrics": [
        "metricFOB",
        "metricKG"
    ]
}

response = requests.post(url, headers=headers, json=payload, verify=False)

dados = response.json()

print(dados)

lista = dados["data"]["list"]

pd.set_option('display.max_columns', None)

df = pd.DataFrame(lista)


print(response.status_code)
print(df)  
print(df.dtypes)