import os
import pandas as pd

# Define o limite
LIMITE = 101000

# Detecta o diretório onde o arquivo atual (.py ou .ipynb) está
diretorio_atual = os.getcwd() 

# Se o arquivo estiver dentro de Docs/Etapa2/, precisamos subir 2 níveis para chegar na raiz
raiz_do_projeto = os.path.abspath(os.path.join(diretorio_atual, "..", ".."))

# Agora, para acessar o dataset, você monta o caminho assim:
caminho_dataset = os.path.join(raiz_do_projeto, "dataset", "yellow_trip.csv")

# Carregamento seguro
df = pd.read_csv(caminho_dataset)
df_limitado = df.head(LIMITE)

print(f"Salvando {LIMITE} registros em CSV...")
df_limitado.to_csv('~/Documentos/case_tecnico/dataset/yellow_trip.csv', index=False, encoding='utf-8')

print("Concluído!")
