import pandas as pd

df= pd.read_csv('../dados/EXP_2024.csv',sep=";")

NCM = ['49029000''82119400''85392910''94051190''94052900''94054900''94059200']

linhas_filtradas =  df['CO_NCM'].isin(NCM)

print(linhas_filtradas)

df = df[linhas_filtradas]

print(df)