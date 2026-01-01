# 🚀 Case Técnico: Yellow Taxi NYC
### Pipeline de Dados End-to-End | Processo Seletivo Dadosfera

**Candidato:** Pedro Henrique Barroso  
**Stack Principal:** `Python` | `SQL` | `Pandas` | `Dadosfera` | `Metabase` | `Linux`

---

## 📌 Visão Geral do Projeto
Este repositório contém a **Prova de Conceito (PoC)** do ciclo de vida de dados dos Táxis Amarelos de Nova York. O projeto demonstra a capacidade de ingerir, tratar, validar e visualizar dados em um ambiente de nuvem, superando desafios reais de integração e tipagem.

---

## 🗺️ Status das Etapas
- ✅ **Mínimo Avaliado:** Etapas 0, 1, 2, 3, 4 e 7 *(Concluídas)*
- ⏳ **Próximos Passos:** Etapas 5, 6, 8, 9 e 10 *(Pipeline, IA e DataApp)*

---

## 📂 Estrutura de Documentação Detalhada
Para entender as decisões técnicas, desafios e aprendizados de cada fase, acesse os relatórios específicos abaixo:

### [📁 Etapa 0: Organização e Planejamento](Docs/Etapa0/README.md)
* **Destaque:** Gestão ágil via **Jira**.
* **Foco:** Mitigação de riscos e cumprimento de prazos.

### [📁 Etapa 1: Definição do Dataset](Docs/Etapa1/README.md)
* **Destaque:** Decisão estratégica de **Pivotagem**.
* **Foco:** Substituição do dataset `product-search` pelo `Yellow-Taxi` para viabilidade técnica.

### [📁 Etapa 2: Ingestão e Integração](Docs/Etapa2/README.md)
* **Destaque:** Pipeline de dados via **Google Sheets** e **Dadosfera**.
* **Aprendizado:** Identificação de corrupção de tipos (VARCHAR vs FLOAT).

### [📁 Etapas 3 e 4: Exploração e Data Quality](Docs/Etapa3_Etapa4/README.md)
* **Destaque:** Análise via **Pandas** (diagnóstico de inconsistências).
* **Insight:** Resiliência técnica após conflitos de dependência com a ferramenta Soda.

### [📁 Etapa 7: Analytics e Visualização](Docs/Etapa7/README.md)
* **Destaque:** Camada Gold construída via **SQL Nativo**.
* **Solução:** Uso de `TRY_TO_DOUBLE` e `TO_DATE` para sanitarização e geração de KPIs financeiros.

---

## 💡 Principais Aprendizados Técnicos
* **Resiliência no Pipeline:** Nem sempre o dado chegará perfeito. A capacidade de corrigir tipos via SQL (Casting) salvou a entrega dos indicadores.
* **Gestão de Prioridades:** Identificar datasets inviáveis precocemente é crucial para o sucesso de projetos com prazos rígidos.
* **Independência de Ferramenta:** Quando o framework automático (Soda) falhou, o domínio de bibliotecas base (Pandas) garantiu a continuidade da análise.

---

## 🛠️ Como reproduzir
1. Os scripts de conversão estão em `Docs/Etapa2/`.
2. As queries de visualização estão documentadas em `Docs/Etapa7/`.
3. O Notebook de análise exploratória encontra-se em `Docs/Etapa3_Etapa4/`.