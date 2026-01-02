# Etapa 9 - Desenvolvimento de Data App (Streamlit)

> **Contexto & Decisão:** A criação de uma interface interativa foi a escolha estratégica para permitir que o usuário final explore os dados de forma visual e intuitiva, sem depender de ferramentas de BI externas ou queries complexas.

### ✍️ Relato Pessoal

*   Seguindo o fluxo de desenvolvimento relacionado às etapas avaliativas e de acordo com o meu cronograma de planejamento. A Etapa 9 envolve o desenvolvimento e criação de um DataApp. Neste sentido, o DataApp que estou propondo é uma plataforma para Análise Exploratória de Dados (EDA), nesta plataforma foi construído diversos gráficos de valor envolvendo as viagens, faturamento, fornecedor dos dados, distribuição das viagens e etc..

    Na etapa de desenvolvimento, busquei apoio e estrutura na documentação e tentei utilizar uma abordagem de geração de valor semelhante a plataforma da Dadosfera, porém, construída e desenvolvida totalmente em python e tuilizando toda estrutura, frameworks e bibliotecas disponíveis. Para isto, utilizei as bibliotecas **Pandas**, **Streamlit** e **plotly**. São bibliotecas e frameworks robustos, para uma solução robusta.
    
    Ao longo do desenvolvimento, esbarrei em um problema técnico enfrentado anteriormente e recorrente na engenharia de dados **"integridade e qualidade de dados"**, assim como ocorrido anteriormente, o dataset estava com problemas de consistência e tipagem dos dados. Diferente do SQL aplicado no ambiente da Dadosfera + Metabase, busquei uma alternativa de filtrar e pré-processar estes dados via Pandas e Python. Como são linguagens e frameworks que me permite maior liberdade, conhecimento e segurança, a minha decisão foi de exclusão de todos os dados inconsistentes ou corrompidos, ao invés de trata-los, eu optei por esta abordagem agressiva para ter um parametro de diferença no volume de dados. O resultado foi uma base de aproximadamente 26 mil registros "puros" e completamente confiáveis.  
    
---
    
* Além disso, eu priorizei a **"protabilidade"** do projeto. tentei estruturar o projeto para que ele funcione de forma autonôma, para isto utilizei de caminhos relativos e uma estrutura de diretórios organizada. Desta forma, garanto que qualquer pessoa consiga clonar o repositório e rodar a aplicação.

> **Observação:** Para o pleno funcionamento deste DatAapp, da forma com que ele foi pensado e estruturado, é muito importante que você leia e acompanhe o [README](./dataapp/README.md), nele, está contido todo o passo-a-passo de instalação e execução deste DataApp

### 🛠️ Detalhes Técnicos
- **Ferramentas Utilizadas:** Python, Streamlit, Pandas e Plotly.
- **Tratamento de Dados:** Ajustes dinâmicos de tipos (Casting) e filtragem de outliers diretamente no backend da aplicação para garantir os gráficos consistentes.
- **Visualização:** Dashboards interativos contendo KPIs estratégicos de receita, volume de viagens e eficiência operacional (distância média por categoria).

### 🖼️ Artefatos e Evidências
* [Script da Aplicação (app.py)](./dataapp/app.py)
* [Arquivo de Dependências (requirements.txt)](./dataapp/requirements.txt)
* [Print: Visão Geral do Dashboard](dashboard_visao_geral.png)
* [Print: Filtros Interativos e KPIs](dashboard_kpis_detalhes.png)
* [Print: Tabela de Dados Limpa](tabela_dados_limpos.png)
* [Print: Dashboard da Análise Descritiva dos Dados](dashboard_estatistica.png)