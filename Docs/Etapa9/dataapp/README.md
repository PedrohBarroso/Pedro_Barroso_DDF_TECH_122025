# 🚀 Guia de Instalação e Execução - DataApp

Este documento fornece as instruções necessárias para configurar o ambiente e executar o DataApp de Análise Exploratória (EDA) localmente.

## 🛠️ Pré-requisitos
Antes de começar, certifique-se de ter instalado em sua máquina:
* **Python 3.8 ou superior**
* **Git** (para clonar o repositório)
* **Ambiente Virtual (Recomendado):** Para evitar conflitos de bibliotecas.

## 🛠️ Guia de Instalação

### 1. Clonar o Repositório
    Caso ainda não tenha clonado o repositório, clone o projeto completo:

    ```bash
        git clone [https://github.com/PedrohBarroso/Pedro_Barroso_DDF_TECH_122025](https://github.com/PedrohBarroso/Pedro_Barroso_DDF_TECH_122025)
        
        # Entrar no repositório
        cd Pedro_Barroso_DDF_TECH_122025
    ```

### 2. Configuração do Ambiente Virtual
    ```bash
        # Entrar na pasta dataapp
        cd Docs/Etapa9/dataapp/

        # Criar o ambiente virtual
        python3 -m venv env

        # Ativar o ambiente virtual
        # Linux/MacOS:
        source env/bin/activate

        # Windows:
        env\Scripts\activate
    ```
### 3. Instalação das Dependências
    ``` bash
    pip install --upgrade pip
    pip install -r requirements.txt
    ```

### 4. Executar a Aplicação
    ```bash
    streamlit run app.py
    ``

## ⚠️ Observações Importantes
- **Estruturas de Pastas:** Certifique de executar o comando nas pastas exatas deste tutorial, ele foi pensando para utilização de caminhos relativos, porém, ainda necessida de arquivos que estão em estrutura acima da aplicação .py, como a base de dados. Logo, para o pleno funcionamento da aplicação, é **muito importante que faça o clone do projeto inteiro e execute o comando de execução na pasta indicada**. 