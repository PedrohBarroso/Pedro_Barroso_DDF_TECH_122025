# Case Técnico - Yellow Taxi (Processo Seletivo - Eng. Dados Junior Dadosfera)

Candidato: Pedro Henrique Barroso

- Sistema Operacional Utilizado: Linux
- Linguagem de Programação Utilizada: Python, SQL 
- Bibliotecas Utilizadas: Pandas, Numpy, soda-Cora
- Base de Dados utilizada: Yellow Taxi Trip Records- (PARQUET) Link: https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page

## Etapas do Processo Seletivo

O objetivo do processo seletivo é percorrer todo o ciclo de vida dos dados, para isto, cada etapa será descrita de maneira resumida abaixo.

- Etapa 0: Organização e Planejamento
- Etapa 1: Definir o Dataset;
- Etapa 2: Integrar e pré-analisar os dados escolhidos à plataforma da Dadosfera;
- Etapa 3: Explorar os dados na plataforma da Dadosfera seguindo as boas práticas e estrutura de Datalake;
- Etapa 4: Identificar e produzir um relatório sobre Qualidade dos Dados observados;
- Etapa 5: Avaliar a capacidade de transformação de dados brutos em features;
- Etapa 6: Propor uma solução de modelagem de dados;
- Etapa 7: Analisar os dados na plataforma da Dadosfera;
- Etapa 8: Criar uma pipeline para processamento de dados anteriores;
- Etapa 9: Criar um DataApp utilizando a estrutura do Streamlit;
- Etapa 10: Apresentação do Case Completo.

### Etapa 0 - Organização e Planejamento:

    Com o prazo de 7 dias para entrega do case técnico, planejamento e organização são fundamentais para uma entrega completa, consistente e de qualidade.

    Para isso, eu criei um quadro no Jira, neste quadro, eu dividi as tarefas a serem entregues em grupos e subgrupos. Cada grupo, contem um ou mais subgrupos. 
    
    Estes grupos foram organizados de maneira estratégica para permitir a entrega completa e mitigar perdas de tempo ou falhas de planejamento.

    A sua estrutura segue a lógica de avaliação, contendo os grupos: mínimo necessário,
                        Intermediário, 
                        Avançado, 
                        Excelente 
                        e Bônus.

    O grupo Mínimo aborda as tarefas mínimas para serem avaliadas, o intermediário aborda as tarefas mínimas + a intermediária e assim, subsequente, até o bônus.

    OBS: Imagens, prints e informações que detalhem cada etapa do processo estaram inclusas na pasta docs.

### Etapa 1 - Definir o Dataset:

    O processo seletivo iniciou com a tentativa de uso do dataset "product-search-corpus", este dataset é uma base de dados sobre anuncios de diversos produtos, porém organizados de maneira desestruturadas ou semi-estruturadas. O formato do arquivo é JsonL. 
    
    O obstaculo observado ao utilizar este dataset foi que devido a natureza desestruturada dos dados, a complexidade para realizar a étapa de ETL séria muito alto, demandaria um tempo extra para estudo, estruturação, organização e definição de uma abordagem que, no meu ponto de vista, é incompativel com o cronograma da entrega.

    A minha decisão, foi de pivotar para um dataset mais simples e melhor estruturado, dessa forma, eu escolhi o dataset "Yellow-Taxi-Trip_NY", este dataset é uma base de dados sobre as viágens de taxi realizadas em New York pela linha amarela. 
    
    Vale ressaltar que ao insistir em um dataset inviável ou com um custo de transformação maior para o tempo e cronograma proposto, pode-se considerar um erro grave de gestão de projetos. 

### Etapa 2 - Integrar e pré-analisar os dados escolhidos à plataforma da Dadosfera

    Inicialmente, para realizar o processo de integrar e pré-analisar os dados escolhidos na plataforma Dadosfera, foi construído um script em python para converter os dados do tipo .Parquet para o tipo .CSV.

    No script, disponível na pasta de dataset, eu inicialmente limitei o arquivo à 101 mil registros e transformei a base de dados em um dataframe utilizando a biblioteca pandas, após, eu converti o dataframe para .csv e exportei o arquivo .csv.

    Após de exportado a base de dados no formato .csv, eu importei o arquivo .csv na plataforma Google Sheets, inicialmente, não me apresentou falha ou erro grave, porém, ao final, na etapa 7, eu percebi que iria enfrentar mais um obstaculo. Em resumo, o Google Sheets ao tentar "ajudar", aplicou uma formatação automática nos dados e esta formatação descaracterizou os tipos dos dados originais, como por exemplo, ao importar a base de dados na plataforma Dadosfera através do módulo de "Conexão" e ingestão de dados via o módulo de "Pipelines", algumas colunas que deveriam vir no formato FLOAT ou TIMESTAMP, foram transformadas em VARCHAR (texto).

    Eu identifiquei que a facilidade de integração via ferramenta Sheets pode corromper a integridade de dados e me atrapalhar nas etapas seguintes, porém, não me deixei abater por este desafio e perseverei tentando entregar sempre o meu melhor resultado e tentando aprender ou ter uma visão crítica sobre cada étapa.

    A pré-analise dos dados ocorreu dentro da plataforma da Dadosfera, no próprio módulo de Catalogo, após a execução da Pipeline para ingestão dos dados na plataforma, é criado um catalogo sobre estes dados, neste módulo de catalogo, é possível realizar a etapa de análise descritiva dos dados, como identificar o número de linhas, o número de colunas, quais são as colunas, o tipo das colunas, uma prévia dos dados de cada coluna, além disso pode-se gerar um conjunto de relatórios automaticamente sobre estes dados e analisar a tabela (Será informado na etapa de análise, como ocorreu esta análise).

### Etapa 3: Explorar os dados na plataforma da Dadosfera seguindo as boas práticas e estrutura de Datalake

    Para utilização de uma biblioteca robusta sobre análise e qualidade dos dados, eu tentei implementar o framework Soda para validação de Data Quality. Porém, mais uma vez, enfrentei um novo obstaculo, conflitos de depêndencias no pip e restrições lógicas no meu ambiente local impediram a plena execução da ferramenta.

    Porém, mais uma vez, eu não me deixei abater, assim como um bom profissional não fica apegado à ferramenta, eu recorri a biblioteca Pandas para tentar identificar possíveis problemas ou inconsistências nos dados. Eu executei os comandos (df.info() e df.describe()), provando que conheço da teoria e sei o que se deve validade ou identificar, independente da ferramenta ou biblioteca utilizada. Eu identifiquei valores negativos e inconsistências nos dados.

### - Etapa 7: Analisar os dados na plataforma da Dadosfera

    A próxima etapa, embora não siga uma sequência lógica exata, ela faz parte dos requisitos mínimos do teste.

    na etapa 7, foi utilizado o Módulo de "Visualização" dos dados, nele, somos redirecionados para a plataforma de BI e visualização de dados Metabase.

    Foi nesta etapa que a "ajuda" do Google Sheets foi realmente afetada, pois, é nítido que caso, os dados obtidos possuam inconsistências ou falhas graves, como a alteração dos tipos das variáveis, acarretará em gráficos incosistentes ou problemas na geração de gráficos com maior qualidade.

    Neste sentido, os dados chegaram como texto (via sheets), o motor do BI não era capaz de extrair ou realizar eixos temporais e soma. Neste momento, veio a incerteza e o sentimento que "nada estava saindo como planejado ou como ideal", considerando inclusive, a falta dos gráficos como falha pessoal. Porém, após refletir e repensar o cenário, ao invés de começar do zero, eu tentei fazer a manipulação na estrutura do Metabase via SQL bruto e corrigindo as inconsistências.

    Após muito pesquisar e estudar, eu elaborei uma query robusta contendo o uso do TRY_TO_DOUBLE para forçar as strings em dados númericos, utilizar do TO_DATE E LEFT para reconstruir a integridade temporal, filtros WHERE para reomver o faturamento negativo identificado via Pandas. O Resultado obtido foi que o dado "quebrado" foi transformado em uma tabela de indicadores executivos, com as colunas calculadas manualmente como "Receita Total", "Distância Média" e "Volume de viagens".

    Honestamente, eu gostaria que nesta etapa fossem criados muitos gráficos, gráficos bonitos, uma dashboard legal, mas dada todas as dificuldades, transtornos e nuances, eu consegui contornar todas elas e construir ainda que apenas em uma tabela, mas que demonstra valor e corrige todas as imperfeições e defeitos. Nem sempre teremos o cenário perfeito ou o ambiente perfeito com tudo funcionando, mas saber lidar com cada dificuldade, apoiado no conhecimento técnico e suporte das ferramentas de IA + artigos e posts em blogs disponíveis, faz total diferença nesta jornada.

    A entrega desta etapa não é exatamente diversos gráficos e uma dashboard bonita, mas o resultado que perseverãnça, resiliencia e proatividade em busca de uma solução fazem a diferença. 