import pandas as pd

# Define o limite
LIMITE = 101000

print("Carregando arquivo...")
# O Pandas carrega o arquivo e o .head() seleciona apenas as primeiras linhas
df = pd.read_parquet('~/Documentos/case_tecnico/dataset/yellow_tripdata_2025-01.parquet')
df_limitado = df.head(LIMITE)

print(f"Salvando {LIMITE} registros em CSV...")
df_limitado.to_csv('~/Documentos/case_tecnico/dataset/yellow_trip.csv', index=False, encoding='utf-8')

print("Concluído!")
