# Etapa 3 e 4 - Exploração e Qualidade dos Dados

> **Contexto & Decisão:** Utilizei frameworks de validação e análise via Pandas para garantir a consistência.

### Relato do Candidato

*   Para utilização de uma biblioteca robusta sobre análise e qualidade dos dados, eu tentei implementar o framework Soda para validação de Data Quality. Porém, mais uma vez, enfrentei um novo obstáculo, conflitos de dependências no pip e restrições lógicas no meu ambiente local impediram a plena execução da ferramenta.

    Porém, mais uma vez, eu não me deixei abater, assim como um bom profissional não fica apegado à ferramenta, eu recorri a biblioteca Pandas para tentar identificar possíveis problemas ou inconsistências nos dados. Eu executei os comandos (df.info() e df.describe()), provando que conheço da teoria e sei o que se deve validar ou identificar, independente da ferramenta ou biblioteca utilizada. Eu identifiquei valores negativos e inconsistências nos dados.
    
    É válido destacar que após resultados e identificação de inconsistências dos dados via pandas, foi-se descartado a possibilidade de uso de ambientes de cloud, como o google colab. Foi uma decisão de projeto para mitigar o tempo e a solução entregue, fator importante em um projeto de software.*

### Detalhes Técnicos
- **Frameworks:** Soda.Scan (tentativa) e Pandas (execução).
- **Descobertas:** Inconsistências de valores e tipos.

### 🖼️ Artefatos
* [Notebook Jupyter de Análise](Case%20DDF_Tech%20yellow-Taxi.ipynb)
* [Print: Código Soda](codigo_soda-cora.png)
* [Print: Adequação CDM](codigo_adequacao_cdm.png)
* [Print: Output df.info()](codigo_df-info.png)
* [Print: Output df.describe()](codigo_df-describe.png)
