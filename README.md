# Case Técnico - Yellow Taxi (Processo Seletivo - Eng. Dados Junior DadosFera)
**Candidato:** Pedro Henrique Barroso
**Sistema Operacional:** Linux | **Linguagem:** Python, SQL | **Bibliotecas:** Pandas, Numpy, soda-Cora
**Base de Dados:** [Yellow Taxi Trip Records (PARQUET)](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page)

---

## 🗺️ Visão Geral das Etapas
O objetivo é percorrer todo o ciclo de vida dos dados. Abaixo, a lista completa das etapas, com **as realizadas destacadas**:
- ✅ **Etapa 0:** Organização e Planejamento *(Concluída)*
- ✅ **Etapa 1:** Definir o Dataset *(Concluída)*
- ✅ **Etapa 2:** Integrar e pré-analisar os dados à plataforma *(Concluída)*
- ✅ **Etapa 3:** Explorar os dados seguindo boas práticas *(Concluída)*
- ✅ **Etapa 4:** Identificar e produzir relatório sobre Qualidade dos Dados *(Concluída)*
- ⏳ Etapa 5: Avaliar a capacidade de transformação de dados brutos em features
- ⏳ Etapa 6: Propor uma solução de modelagem de dados
- ✅ **Etapa 7:** Analisar os dados na plataforma *(Concluída)*
- ⏳ Etapa 8: Criar uma pipeline para processamento
- ⏳ Etapa 9: Criar um DataApp com Streamlit
- ⏳ Etapa 10: Apresentação do Case Completo

*Nota: Este documento detalha as etapas concluídas (0, 1, 2, 3, 4 e 7), que compõem os requisitos mínimos.*

---

## 📝 Relato Detalhado por Etapa

### Etapa 0 - Organização e Planejamento
> **Contexto & Decisão:** Com um prazo de 7 dias, o planejamento foi fundamental para uma entrega consistente.

* Com o prazo de 7 dias para entrega do case técnico, planejamento e organização são fundamentais para uma entrega completa, consistente e de qualidade.

    Para isso, eu criei um quadro no Jira, neste quadro, eu dividi as tarefas a serem entregues em grupos e subgrupos. Cada grupo, contem um ou mais subgrupos. 
    
    Estes grupos foram organizados de maneira estratégica para permitir a entrega completa e mitigar perdas de tempo ou falhas de planejamento.

    A sua estrutura segue a lógica de avaliação, contendo os grupos: mínimo necessário,
                        Intermediário, 
                        Avançado, 
                        Excelente 
                        e Bônus.

    O grupo Mínimo aborda as tarefas mínimas para serem avaliadas, o intermediário aborda as tarefas mínimas + a intermediária e assim, subsequente, até o bônus. *

**Ferramenta Utilizada:** Jira
**Estrutura Criada:** Grupos (Mínimo, Intermediário, Avançado, Excelente, Bônus)
**Artefatos Gerados:** Quadro de tarefas (disponível na pasta `/docs`)

---

### Etapa 1 - Definir o Dataset
> **Contexto & Decisão:** Pivotei de um dataset complexo (`product-search-corpus`) para um mais estruturado (`Yellow-Taxi`), priorizando a viabilidade dentro do cronograma.

*   O processo seletivo iniciou com a tentativa de uso do dataset "product-search-corpus", este dataset é uma base de dados sobre anuncios de diversos produtos, porém organizados de maneira desestruturadas ou semi-estruturadas. O formato do arquivo é JsonL. 
    
    O obstaculo observado ao utilizar este dataset foi que devido a natureza desestruturada dos dados, a complexidade para realizar a étapa de ETL séria muito alto, demandaria um tempo extra para estudo, estruturação, organização e definição de uma abordagem que, no meu ponto de vista, é incompativel com o cronograma da entrega.

    A minha decisão, foi de pivotar para um dataset mais simples e melhor estruturado, dessa forma, eu escolhi o dataset "Yellow-Taxi-Trip_NY", este dataset é uma base de dados sobre as viágens de taxi realizadas em New York pela linha amarela. 
    
    Vale ressaltar que ao insistir em um dataset inviável ou com um custo de transformação maior para o tempo e cronograma proposto, pode-se considerar um erro grave de gestão de projetos.*

**Dataset Inicial:** `product-search-corpus` (JSONL, semiestruturado)
**Desafio Identificado:** Complexidade de ETL incompatível com o prazo
**Dataset Escolhido:** `Yellow-Taxi-Trip_NY` (Parquet, bem estruturado)
**Insight Chave:** "Ao insistir em um dataset inviável... pode-se considerar um erro grave de gestão de projetos."

---

### Etapa 2 - Integrar e Pré-analisar os Dados
> **Contexto & Decisão:** Utilizei um script Python para conversão e o Google Sheets para integração inicial, o que gerou um aprendizado posterior sobre integridade de dados.

*	Inicialmente, para realizar o processo de integrar e pré-analisar os dados escolhidos na plataforma Dadosfera, foi construído um script em python para converter os dados do tipo .Parquet para o tipo .CSV.

    No script, disponível na pasta de dataset, eu inicialmente limitei o arquivo à 101 mil registros e transformei a base de dados em um dataframe utilizando a biblioteca pandas, após, eu converti o dataframe para .csv e exportei o arquivo .csv.

    Após de exportado a base de dados no formato .csv, eu importei o arquivo .csv na plataforma Google Sheets, inicialmente, não me apresentou falha ou erro grave, porém, ao final, na etapa 7, eu percebi que iria enfrentar mais um obstaculo. Em resumo, o Google Sheets ao tentar "ajudar", aplicou uma formatação automática nos dados e esta formatação descaracterizou os tipos dos dados originais, como por exemplo, ao importar a base de dados na plataforma Dadosfera através do módulo de "Conexão" e ingestão de dados via o módulo de "Pipelines", algumas colunas que deveriam vir no formato FLOAT ou TIMESTAMP, foram transformadas em VARCHAR (texto).

    Eu identifiquei que a facilidade de integração via ferramenta Sheets pode corromper a integridade de dados e me atrapalhar nas etapas seguintes, porém, não me deixei abater por este desafio e perseverei tentando entregar sempre o meu melhor resultado e tentando aprender ou ter uma visão crítica sobre cada étapa.

    A pré-analise dos dados ocorreu dentro da plataforma da Dadosfera, no próprio módulo de Catalogo, após a execução da Pipeline para ingestão dos dados na plataforma, é criado um catalogo sobre estes dados, neste módulo de catalogo, é possível realizar a etapa de análise descritiva dos dados, como identificar o número de linhas, o número de colunas, quais são as colunas, o tipo das colunas, uma prévia dos dados de cada coluna, além disso pode-se gerar um conjunto de relatórios automaticamente sobre estes dados e analisar a tabela (Será informado na etapa de análise, como ocorreu esta análise).*

**Ação 1:** Script Python para conversão de Parquet para CSV (limite: 101k registros)
**Ação 2:** Importação do CSV para Google Sheets
**Problema Identificado (Futuro):** Formatação automática do Sheets alterou tipos de dados (ex: FLOAT → VARCHAR)
**Análise Inicial:** Realizada no catálogo da plataforma após ingestão via pipeline

---

### Etapa 3: Explorar os dados seguindo boas práticas & 
### Etapa 4:Identificar e produzir relatório sobre Qualidade dos Dados
> **Contexto & Decisão:** Utilizei um framework para validação de qualidade dos dados soda.Scan, o que gerou um aprendizado e experiência posterior.

*	Para utilização de uma biblioteca robusta sobre análise e qualidade dos dados, eu tentei implementar o framework Soda para validação de Data Quality. Porém, mais uma vez, enfrentei um novo obstaculo, conflitos de depêndencias no pip e restrições lógicas no meu ambiente local impediram a plena execução da ferramenta.

    Porém, mais uma vez, eu não me deixei abater, assim como um bom profissional não fica apegado à ferramenta, eu recorri a biblioteca Pandas para tentar identificar possíveis problemas ou inconsistências nos dados. Eu executei os comandos (df.info() e df.describe()), provando que conheço da teoria e sei o que se deve validade ou identificar, independente da ferramenta ou biblioteca utilizada. Eu identifiquei valores negativos e inconsistências nos dados.
    
    É válido destacar que após resultados e identificações de inconsistencias dos dados via pandas, foi-se descartado a possibilidade de uso de ambientes de cloud, como o google colab. Foi uma decisão de projeto para mitigar o tempo e a solução entregue, fator importante em um projeto de software.*

**Ação 1:** Estudar e aplicar o framework soda.Scan
**Ação 2:** Após identificado conflitos de dependencia, foi utilizado a biblioteca pandas
**Problema Identificado (Futuro):** Conflito no ambiente local por conta de dependencias lógicas das bibliotecas pip e soda.Scan
**Análise Inicial:** Utilizar a biblioteca pandas através dos comandos df.describe() e df.info()
**Análise Posterior:** Conforme resultado positivo apartir da análise via pandas, foi-se descartado a possibilidade de execução do código em ambiente de cloud, como o google colab.
**Principal Insight:** Na próxima vez, utilizar um ambiente de cloud como o Google Colab, facilita e mitiga falhas em ambientes locais. 

---

### Etapa 7 - Analisar os Dados na Plataforma
> **Contexto & Decisão:** Contornei problemas de qualidade de dados herdados usando SQL no Metabase, focando em gerar valor a partir de dados imperfeitos.

*A próxima etapa, embora não siga uma sequência lógica exata, ela faz parte dos requisitos mínimos do teste.

    na etapa 7, foi utilizado o Módulo de "Visualização" dos dados, nele, somos redirecionados para a plataforma de BI e visualização de dados Metabase.

    Foi nesta etapa que a "ajuda" do Google Sheets foi realmente afetada, pois, é nítido que caso, os dados obtidos possuam inconsistências ou falhas graves, como a alteração dos tipos das variáveis, acarretará em gráficos incosistentes ou problemas na geração de gráficos com maior qualidade.

    Neste sentido, os dados chegaram como texto (via sheets), o motor do BI não era capaz de extrair ou realizar eixos temporais e soma. Neste momento, veio a incerteza e o sentimento que "nada estava saindo como planejado ou como ideal", considerando inclusive, a falta dos gráficos como falha pessoal. Porém, após refletir e repensar o cenário, ao invés de começar do zero, eu tentei fazer a manipulação na estrutura do Metabase via SQL bruto e corrigindo as inconsistências.

    Após muito pesquisar e estudar, eu elaborei uma query robusta contendo o uso do TRY_TO_DOUBLE para forçar as strings em dados númericos, utilizar do TO_DATE E LEFT para reconstruir a integridade temporal, filtros WHERE para reomver o faturamento negativo identificado via Pandas. O Resultado obtido foi que o dado "quebrado" foi transformado em uma tabela de indicadores executivos, com as colunas calculadas manualmente como "Receita Total", "Distância Média" e "Volume de viagens".

    Honestamente, eu gostaria que nesta etapa fossem criados muitos gráficos, gráficos bonitos, uma dashboard legal, mas dada todas as dificuldades, transtornos e nuances, eu consegui contornar todas elas e construir ainda que apenas em uma tabela, mas que demonstra valor e corrige todas as imperfeições e defeitos. Nem sempre teremos o cenário perfeito ou o ambiente perfeito com tudo funcionando, mas saber lidar com cada dificuldade, apoiado no conhecimento técnico e suporte das ferramentas de IA + artigos e posts em blogs disponíveis, faz total diferença nesta jornada.

    A entrega desta etapa não é exatamente diversos gráficos e uma dashboard bonita, mas o resultado que perseverãnça, resiliencia e proatividade em busca de uma solução fazem a diferença.*

**Ferramenta:** Módulo de Visualização (Metabase)
**Problema Herdado:** Dados chegando como texto (VARCHAR)
**Solução Técnica:** Query SQL com `TRY_TO_DOUBLE`, `TO_DATE`, `LEFT`, filtros `WHERE`
**Resultado Final:** Tabela de indicadores executivos com "Receita Total", "Distância Média", "Volume de viagens"
**Principal Insight:** "Nem sempre teremos o cenário perfeito... saber lidar com cada dificuldade... faz total diferença."

---
