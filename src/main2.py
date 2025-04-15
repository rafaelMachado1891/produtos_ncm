import requests

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
    "details": ["country", "state", "ncm",],
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

# Verificando a resposta
print(response.status_code)
print(response.json())  # Se a resposta for JSON