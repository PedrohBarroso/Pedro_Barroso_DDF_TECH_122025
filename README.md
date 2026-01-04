# 🚀 Case Técnico: Yellow Taxi NYC
### Pipeline de Dados End-to-End | Processo Seletivo Dadosfera**

**Candidato:** Pedro Henrique Barroso

**Stack Principal:** Python | SQL | Pandas | Dadosfera | Metabase | Linux

---

## 📌 Visão Geral do Projeto

Este repositório contém a **Prova de Conceito (PoC)** do ciclo de vida de dados dos Táxis Amarelos de Nova York. O projeto demonstra a capacidade de ingerir, tratar, validar e visualizar dados em um ambiente de nuvem, superando desafios reais de integração e tipagem.

---

## 🗺️ Status das Etapas

- ✅ **Mínimo Avaliado:** Etapas 0, 1, 2, 3, 4, 7 e 9 *(Concluídas)*

- ✅ **Nível Outlier:** Etapas 5 e 6 *(Modelagem e Processamento GenAI)*

- ✅ **Nível Excelente:** Item Bônus - GenAI & Market Intelligence *(Concluído)*

- ⏳ **Próximos Passos:** Etapa 10 *(Vídeo de Apresentação)*

--- 

## 📂 Estrutura de Documentação Detalhada

Para entender as decisões técnicas, desafios e aprendizados de cada fase, acesse os relatórios específicos abaixo:

### 📁 [Etapa 0: Organização e Planejamento](Docs/Etapa0/README.md)

* **Destaque:** Gestão ágil via **Jira**.

* **Foco:** Mitigação de riscos e cumprimento de prazos.

### 📁 [Etapa 1: Definição do Dataset](Docs/Etapa1/README.md)

* **Destaque:** Decisão estratégica de **Pivotagem**.

* **Foco:** Substituição do dataset `product-search` pelo Yellow-Taxi` para viabilidade técnica.

### 📁 [Etapa 2: Ingestão e Integração](Docs/Etapa2/READMR.md)

* **Destaque:** Pipeline de dados via **Google Sheets** e **Dadosfera**.

* **Aprendizado:** Identificação de corrupção de tipos (VARCHAR vs FLOAT).

### 📁 [Etapas 3 e 4: Exploração e Data Quality](Docs/)

* **Destaque:** Análise via **Pandas** (diagnóstico de inconsistências).

* **Insight:** Resiliência técnica após conflitos de dependência com a ferramenta Soda.

### 📁 [Etapa 7: Analytics e Visualização](Docs/Etapa7/README.md)

* **Destaque:** Camada Gold construída via **SQL Nativo**.

* **Solução:** Uso de `TRY_TO_DOUBLE` e `TO_DATE` para sanitarização e geração de KPIs financeiros.

### 📁 [Etapa 9: Desenvolvimento de um DataApp](Docs/Etapa9/README.md)

* **Destaque:** Desenvolvimento de um DataApp interativo e **portável** via **Streamlit**.

* **Solução:** Dashboard interativo sobre KPIs financeiros e operacionais.

### [📁 Item Bônus: GenAI + Data Apps](Docs/EtapaBonus/README.md)

* **Destaque:** Transformação de dados em ativos de marketing via LLMs.

* **Solução:** Integração com **GPT-4** e **DALL-E 3** para geração automática de pitches e banners publicitários.

### 📁 [Etapa 6: Modelagem de Dados](Docs/Etapa6/README.md)

* **Destaque:** Arquitetura de **`Data-Warehouse`**.

* **Solução:** Implementação de um **Kimball Star Schema** (Fatos e Dimensões) para otimização de performance e escalabilidade.

### 📁 [Etapa 5: Processamento GenAI e LLMs](Docs/Etapa5/README.md)

* **Destaque:** Extração de Features via IA.

* **Nota:** As competências de processamento de dados via LLMs foram integradas ao módulo de **Market Intelligence** desenvolvidos na **Etapa Bônus**, aplicando GPT-4 para converter contexto operacional em ativos de negócio.


---

## 💡 Principais Aprendizados Técnicos

* **Resiliência no Pipeline:** Nem sempre o dado chegará perfeito. A capacidade de corrigir tipos via SQL (Casting) salvou a entrega dos indicadores.

* **Visão de Negócio:** A modelagem Kimball permitiu transformar dados brutos em uma estrutura legível, reduzindo drasticamente o tempo de resposta das consultas.

* **IA como Alavanca:** O uso de GenAI provou que a Engenharia de Dados pode ir além do processamento, gerando ativos diretamente para o time de Marketing e Vendas.

---

## 🛠️ Como reproduzir

1. Os scripts de conversão estão em `Docs/Etapa2/`.

2. As queries de visualização estão documentadas em `Docs/Etapa7/`.

3. O Notebook de análise exploratória encontra-se em `Docs/Etapa3_Etapa4/`.

4. O esquema da modelagem dimensional está disponível em `Docs/Etapa6/`.

5. As instruções para execução do DataApp e módulos de IA estão disponíveis em `Docs/EtapaBonus/`.