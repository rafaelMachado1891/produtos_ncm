import requests
import pandas as pd
import json

url = "https://api-comexstat.mdic.gov.br/general"

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
            "filter": "economicBlock",
           "values": [111]
        },
        
        {
            "filter": "ncm",
            "values": ["94051190"]
            
        }
    ],
    "details": ["country", "state","ncm"],
    "metrics": [
        "metricFOB",
        "metricKG",
        "metricStatistic",
        "metricFreight",
        "metricInsurance",
        "metricCIF"
    ]
}

response = requests.post(url, headers=headers, json=payload, verify=False)

dados = response.json()

lista = dados["data"]["list"]

pd.set_option('display.max_columns', None)

df = pd.DataFrame(lista)


print(response.status_code)
print(df)  
print(df.dtypes)