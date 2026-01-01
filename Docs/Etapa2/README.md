# Etapa 2 - Integrar e Pré-analisar os Dados

> **Contexto & Decisão:** Utilizei um script Python para conversão e o Google Sheets para integração inicial.

### Relato do Candidato
	*   Inicialmente, para realizar o processo de integrar e pré-analisar os dados escolhidos na plataforma Dadosfera, foi construído um script em python para converter os dados do tipo .Parquet para o tipo .CSV.

    No script, disponível na pasta de dataset, eu inicialmente limitei o arquivo à 101 mil registros e transformei a base de dados em um dataframe utilizando a biblioteca pandas, após, eu converti o dataframe para .csv e exportei o arquivo .csv.

    Após ter exportado a base de dados no formato .csv, eu importei o arquivo .csv na plataforma Google Sheets, inicialmente, não me apresentou falha ou erro grave, porém, ao final, na etapa 7, eu percebi que iria enfrentar mais um obstáculo. Em resumo, o Google Sheets ao tentar "ajudar", aplicou uma formatação automática nos dados e esta formatação descaracterizou os tipos dos dados originais, como por exemplo, ao importar a base de dados na plataforma Dadosfera através do módulo de "Conexão" e ingestão de dados via o módulo de "Pipelines", algumas colunas que deveriam vir no formato FLOAT ou TIMESTAMP, foram transformadas em VARCHAR (texto).

    Eu identifiquei que a facilidade de integração via ferramenta Sheets pode corromper a integridade de dados e me atrapalhar nas etapas seguintes, porém, não me deixei abater por este desafio e perseverei tentando entregar sempre o meu melhor resultado e tentando aprender ou ter uma visão crítica sobre cada etapa.

    A pré-análise dos dados ocorreu dentro da plataforma da Dadosfera, no próprio módulo de Catálogo, após a execução da Pipeline para ingestão dos dados na plataforma, é criado um catálogo sobre estes dados, neste módulo de catálogo, é possível realizar a etapa de análise descritiva dos dados, como identificar o número de linhas, o número de colunas, quais são as colunas, o tipo das colunas, uma prévia dos dados de cada coluna, além disso pode-se gerar um conjunto de relatórios automaticamente sobre estes dados e analisar a tabela (Será informado na etapa de análise, como ocorreu esta análise).*

### Detalhes Técnicos
- **Script Conversão de Dados:** Script para converter os dados do formato .Parquet > .csv.
- **Plataforma Google Sheets | Dadosfera:** Integração dos dados na plataforma Dadosfera via Google Sheets.

### 🖼️ Artefatos e Scripts
* [Script de Conversão (Python)](convert_parquet_csv.py)
* [Print: Tabela no Google Sheets](tabela_google_sheets.png)
* [Print: Ingestão na Dadosfera](import_base-dados_dadosfera.png)
* [Print: Pipeline de Dados](pipeline_dados_dadosfera.png)
* [Print: Análise Descritiva](analise_descritiva2.png)
