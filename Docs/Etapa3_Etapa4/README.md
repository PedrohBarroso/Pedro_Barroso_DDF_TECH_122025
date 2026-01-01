# Etapa 3 e 4 - Exploração e Qualidade dos Dados

> **Contexto & Decisão:** Utilizei frameworks de validação e análise via Pandas para garantir a consistência.

### Relato do Candidato

*   Para utilização de uma biblioteca robusta sobre análise e qualidade dos dados, eu tentei implementar o framework Soda para validação de Data Quality. Porém, mais uma vez, enfrentei um novo obstáculo, conflitos de dependências no pip e restrições lógicas no meu ambiente local impediram a plena execução da ferramenta.

    Porém, mais uma vez, eu não me deixei abater, assim como um bom profissional não fica apegado à ferramenta, eu recorri a biblioteca Pandas para tentar identificar possíveis problemas ou inconsistências nos dados. Eu executei os comandos (df.info() e df.describe()), provando que conheço da teoria e sei o que se deve validar ou identificar, independente da ferramenta ou biblioteca utilizada. Eu identifiquei valores negativos e inconsistências nos dados.
    
    É válido destacar que após resultados e identificação de inconsistências dos dados via pandas, foi realizado a tentativa de utilização do ambiente de cloud Google Colaboratory, porém ainda sim, permaneceu a inconsistência e conflito entre versões. Foi realizado a tentativa de utilização do framework great-expectations, mas sem sucesso também. Como o Google Colaboraty utiliza as versões atuais do python + bibliotecas, assim como meu ambiente local. Houve um conflito entre versões.*

### Detalhes Técnicos
- **Frameworks:** Soda.Scan (tentativa), Great-Expectations (Tentativa) e Pandas (execução).
- **Ambientes de Execução:** Google Colaboratory (Tentativa) e Ambiente Local (Jupyter Notebook)
- **Descobertas:** Inconsistências de valores e tipos.

### 🖼️ Artefatos
* [Notebook Jupyter de Análise](Case%20DDF_Tech%20yellow-Taxi.ipynb)
* [Print: Código Soda](codigo_soda-cora.png)
* [Print: Adequação CDM](codigo_adequacao_cdm.png)
* [Print: Output df.info()](codigo_df-info.png)
* [Print: Output df.describe()](codigo_df-describe.png)
