import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/italia/covid19-opendata-vaccini/master/dati/vaccini-summary-latest.csv", sep=',')
print(df.head())
dfNord = df[df['codice_regione_ISTAT']<=8]
print(dfNord)