# Etapa 7 - Analisar os Dados na Plataforma (BI)

> **Contexto & Decisão:** Contornei problemas de qualidade de dados herdados usando SQL no Metabase, focando em gerar valor a partir de dados imperfeitos.

### Relato Pessoal

*   A próxima etapa, embora não siga uma sequência lógica exata, faz parte dos requisitos mínimos do teste.

    Na etapa 7, foi utilizado o Módulo de "Visualização" dos dados, nele, somos redirecionados para a plataforma de BI e visualização de dados Metabase. Foi nesta etapa que a "ajuda" do Google Sheets foi realmente afetada, pois, é nítido que caso, os dados obtidos possuam inconsistências ou falhas graves, como a alteração dos tipos das variáveis, acarretará em gráficos inconsistentes ou problemas na geração de gráficos com maior qualidade.
    
    Neste sentido, os dados chegaram como texto (via sheets), o motor do BI não era capaz de extrair ou realizar eixos temporais e soma. Neste momento, veio a incerteza e o sentimento que "nada estava saindo como planejado ou como ideal", considerando inclusive, a falta dos gráficos como falha pessoal. Porém, após refletir e repensar o cenário, ao invés de começar do zero, eu tentei fazer a manipulação na estrutura do Metabase via SQL bruto e corrigindo as inconsistências.
    
    Após muito pesquisar e estudar, eu elaborei uma query robusta contendo o uso do TRY_TO_DOUBLE para forçar as strings em dados numéricos, utilizar do TO_DATE E LEFT para reconstruir a integridade temporal, filtros WHERE para remover o faturamento negativo identificado via Pandas. O Resultado obtido foi que o dado "quebrado" foi transformado em uma tabela de indicadores executivos, com as colunas calculadas manualmente como "Receita Total", "Distância Média" e "Volume de viagens".
    
    Honestamente, eu gostaria que nesta etapa fossem criados muitos gráficos, gráficos bonitos, uma dashboard legal, mas dada todas as dificuldades, transtornos e nuances, eu consegui contornar todas elas e construir ainda que apenas em uma tabela, mas que demonstra valor e corrige todas as imperfeições e defeitos. Nem sempre teremos o cenário perfeito ou o ambiente perfeito com tudo funcionando, mas saber lidar com cada dificuldade, apoiado no conhecimento técnico e suporte das ferramentas de IA + artigos e posts em blogs disponíveis, faz total diferença nesta jornada.
    
    A entrega desta etapa não é exatamente diversos gráficos e uma dashboard bonita, mas o resultado que perseverança, resiliência e proatividade em busca de uma solução fazem a diferença.*


### 🛠️ Resumo Técnico
- **Ferramenta:** Metabase (SQL Nativo)
- **Desafio:** Dados tipados como VARCHAR (Texto) pelo Google Sheets.
- **Solução:** Implementação de Casting (`TRY_TO_DOUBLE`, `TO_DATE`).

### 🖼️ Artefatos e Evidências
* [Pergunta Central no BI](pergunta_bi.png)
* [Consulta SQL de Correção](consulta_sql.png)
* [Tabela Final de Indicadores](tabela_gerada.png)
