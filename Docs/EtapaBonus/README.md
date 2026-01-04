# # Item Bônus - GenAI + Data Apps (Market Intelligence)

> **Contexto & Decisão:** Decidi que o DataApp não deveria apenas "mostrar o passado", mas "gerar o futuro". A decisão técnica de criar um **Modo de Demonstração** Foi fundamental para garantir que o avaliador experimente a ferramenta sem a barreira de configurar chaves de API pagas imediatamente.

### ✍️ Relato Pessoal
*   Ao analisar os dados de mobilidade de NYC, tive um insight central: **dados de trajeto são dados de audiência**. Se milhares de pessoas veem um táxi por dia, temos um ativo de mídia. 

    Utilizei a Engenharia de Dados como alicerce para construir uma ferramenta de **Market Intelligence**. O maior desafio foi orquestrar a lógica de *Prompt Engineering* para que a IA não fosse genérica, mas sim "Data-Driven" — ou seja, o texto gerado pela IA muda conforme os filtros de data e receita que o usuário aplica no dashboard. É a união real entre Big Data e IA Generativa. Ou seja, utilizei a IA como suporte técnico e apoio ao desenvolvimento, entregando uma combinação perfeita entre ideias de negócio, pensamento estratégico e suporte ao desenvolvimento, acelerando o tempo de desenvolvimento da solução, entregando com qualidade, eficiência e segurança.

### 💡 O Insight de Negócio
Transformei as colunas de "distância" e "faturamento" em argumentos de venda. Se a distância média é alta, o pitch gerado foca em "Visibilidade de Marca". Se o valor médio da corrida é alto, o pitch foca em "Público de Alto Poder Aquisitivo". Isso é transformar engenheiro de dados em parceiro de negócios.

### 🛠️ Detalhes Técnicos
* **Integração Híbrida:** Uso de `openai` para modo real e `plotly.graph_objects` para simular banners no modo demo.
* **Contextualização Dinâmica:** Injeção de variáveis do DataFrame Pandas diretamente no prompt enviado ao GPT-4.
* **Manipulação de Imagens:** Uso de `Pillow` e `base64` para processar e exibir as artes geradas pelo DALL-E 3.

### 🖼️ Artefatos e Evidências
* [Script Completo (app.py)](dataapp/app.py)
* **Print 01:** [Dashboard Principal](dashboard_principal.png)
* **Print 02:** [Módulo Market Intelligence (Chave API *não* cadastrada)](modo_market_api_nao.png)
* **Print 03:** [Módulo Market Intelligence Opções Banner (Modo Demo)](modo_demo_banner.png)
* **Print 03:** [Módulo Market Intelligence Banner Gerado (Modo Demo)](modo_demo_banner_gerado.png)
* **Print 04:** [Módulo Market Intelligence Opções Pitch (Modo Demo)](modo_demo_pitch.png)
* **Print 05:** [Módulo Market Inteligence Pitch Gerado (Modo Demo)](modo_demo_pitch_gerado.png)


---
> **🚀 Próximo Passo:** Para rodar esta aplicação e testar as funcionalidades de IA, siga o [Guia de Instalação](dataapp/README.md).
