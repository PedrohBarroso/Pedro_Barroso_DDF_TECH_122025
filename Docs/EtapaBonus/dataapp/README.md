# 🚀 Guia de Instalação e Execução - DataApp (Versão GenAI)

Este documento fornece as instruções necessárias para configurar o ambiente e executar o **DataApp de Market Intelligence**, que integra análise de dados tradicional (EDA) com Inteligência Artificial Generativa (GPT-4 e DALL-E 3).

## 🛠️ Pré-requisitos
Antes de começar, certifique-se de ter instalado:
* **Python 3.9 ou superior**
* **Git** (para clonagem do repositório)
* **Ambiente Virtual (VENV):** Essencial para isolar as dependências de IA.

## 📥 Passo a Passo

### 1. Preparar o Ambiente
Caso já possua o ambiente da Etapa 9, basta ativar e atualizar as bibliotecas. Caso contrário, siga do zero:

```bash
    # Entrar na pasta do aplicativo
    cd Docs/Etapa_Bonus/dataapp/

    # Criar e ativar o ambiente virtual
    python3 -m venv env
    # No Windows: env\Scripts\activate | No Linux/macOS: source env/bin/activate

    # Instalar dependências (Incluindo OpenAI e Processamento de Imagem)
    pip install --upgrade pip
    pip install streamlit pandas plotly openai pillow python-dotenv

```

### 2. Configuração da Open AI API Key (Opcional)
Para habilitar o modo real do Market Intelligence, você precisa da API Key da Open AI. É válido destacar que não é necessário a adição da Open AI para a demonstração de funcionamento do DataAPP. No modo de demonstração, é simulado todo o funcionamento do app.

#### Linux
```bash
    # 1. Criação do arquivo .env 
    # Certifique de estar na pasta dataapp do projeto.

    # Abra o terminal e execute o comando
    touch .env

    # 2. Adição da API Key
    
    # Abra o terminal e execute o comando
    nano .env

    # Com a interface aberta, cole o comando abaixo utilizando a **estrutura CTRL + SHIFT + V**
    OPENAI_API_KEY=sua_chave_aqui 

    # Para salvar Aperte CTRL + X, após, y

    # Execução da Aplicação
    streamlit run app.py
```
#### Windows
```bash
    # 1. Criação do arquivo .env (windows)
    # Certifique de estar na pasta dataapp do projeto.

    # Abra o terminal e execute o comando
    type nul > .env

    # 2. Adição da API Key
    
    # Abra o arquivo .env com um editor (Bloco de Notas, VS Code, etc.) e adicione
    OPENAI_API_KEY=sua_chave_aqui 

    # Execução da Aplicação
    streamlit run app.py
```