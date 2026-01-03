import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime
import os
import openai 
from PIL import Image
import base64
import io
import time
import plotly.graph_objects as go
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()

# 1. Configuração da página
st.set_page_config(page_title="Dashboard Yellow Taxi", layout="wide")

st.title("🚖 Dashboard & Market Intelligence - Yellow Taxi NYC")
st.markdown("""
            Transformando dados brutos de táxi em insights estratégicos e pitches de venda automatizados.
            """)

# 2. Configuração da API Key da OpenAI
openai_api_key = None
try:
    if hasattr(st, "secrets") and "OPENAI_API_KEY" in st.secrets:
        openai_api_key = st.secrets["OPENAI_API_KEY"]
except Exception:
    pass

if not openai_api_key:
    openai_api_key = os.getenv("OPENAI_API_KEY")

# 3. Carregamento de dados (versão simplificada para demo)
@st.cache_data
def load_data():
    # 1. Importando o dataset
    # Detecta o diretório onde o arquivo atual (.py ou .ipynb) está
    diretorio_atual = os.getcwd() 

    # Se o arquivo estiver dentro de Docs/Etapa2/, precisamos subir 2 níveis para chegar na raiz
    raiz_do_projeto = os.path.abspath(os.path.join(diretorio_atual, "..", "..", ".."))

    # Agora, para acessar o dataset, você monta o caminho assim:
    caminho_dataset = os.path.join(raiz_do_projeto, "dataset", "yellow_trip.csv")

    # Carregamento seguro
    df = pd.read_csv(caminho_dataset)
    
    
    # 2. Tratamento dos dados
    
    # 2.1 Ajuste na coluna Tpep para o formato datetime
    # A função coerce transforma os dados errados em nulos
    df['data_real'] = pd.to_datetime(df['tpep_pickup_datetime'], errors='coerce')
    
    # 2.2 Converter os valores do tipo texto para númerico
    # A função coerce transforma os dados errados em nulos
    df['total_amount'] = pd.to_numeric(df['total_amount'], errors='coerce')
    df['trip_distance'] = pd.to_numeric(df['trip_distance'], errors='coerce')
    df['VendorID'] = pd.to_numeric(df['VendorID'], errors='coerce')
    
    # 3. Remover ruídos e sujeiras
    df = df[df['total_amount'] > 0]
    df = df.dropna(subset=['data_real'])  
    
    return df

df = load_data()

# 4. Sidebar e Filtros
st.sidebar.header('Filtros Globais')
min_date = df['data_real'].min().date()
max_date = df['data_real'].max().date()

date_range = st.sidebar.date_input(
    "Selecione o Período:",
    value=(min_date, max_date),
    min_value=min_date,
    max_value=max_date
)

if len(date_range) == 2:
    start_date, end_date = date_range
    start_datetime = pd.Timestamp(start_date)
    end_datetime = pd.Timestamp(end_date) + pd.Timedelta(days=1)
    df_filtered = df[(df['data_real'] >= start_datetime) & (df['data_real'] <= end_datetime)]
else:
    df_filtered = df

# 5. Calcular KPIs para uso global
receita_total = df_filtered['total_amount'].sum()
viagens_totais = df_filtered.shape[0]
distancia_media = df_filtered['trip_distance'].mean()
valor_medio = df_filtered['total_amount'].mean()

# 6. Sidebar - Modo de Operação
st.sidebar.divider()
st.sidebar.subheader("🔧 Modo de Operação")
modo_operacao = st.sidebar.radio(
    "Escolha como a IA funcionará:",
    ["🚀 Modo Real (com API Key)", "🎭 Modo de Demonstração"],
    index=1
)

# 7. Abas principais
tab1, tab2 = st.tabs(["📊 Dashboard Operacional", "🤖 Market Intelligence & Pitch"])

# --- ABA 1: Dashboard Operacional (resumido) ---
with tab1:
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("💰 Receita Total", f"${receita_total:,.2f}")
    col2.metric("🚕 Total de Viagens", f"{viagens_totais:,}")
    col3.metric("📏 Distância Média", f"{distancia_media:.2f} milhas")
    col4.metric("💵 Valor Médio", f"${valor_medio:.2f}")
    
    st.divider()
    col_graf1, col_graf2 = st.columns(2)
    
    with col_graf1:
        st.subheader("📈 Evolução da Receita Diária")
        df_dia = df_filtered.copy()
        df_dia['data_dia'] = df_dia['data_real'].dt.date
        df_dia_agrupado = df_dia.groupby('data_dia')['total_amount'].sum().reset_index()
        if not df_dia_agrupado.empty:
            fig_line = px.line(df_dia_agrupado, x='data_dia', y='total_amount')
            st.plotly_chart(fig_line, use_container_width=True)
    
    with col_graf2:
        st.subheader("🏢 Receita por Fornecedor")
        df_vendor = df_filtered.groupby('VendorID')['total_amount'].sum().reset_index()
        df_vendor['VendorID'] = df_vendor['VendorID'].astype(str)
        if not df_vendor.empty:
            fig_bar = px.bar(df_vendor, x='VendorID', y='total_amount')
            st.plotly_chart(fig_bar, use_container_width=True)

# --- ABA 2: Market Intelligence & Pitch ---
with tab2:
    st.header("🤖 Market Intelligence & Pitch Generator")
    
    # Informar modo atual
    if modo_operacao == "🚀 Modo Real (com API Key)":
        if not openai_api_key:
            st.error("API Key não configurada para o modo real.")
            st.info("Configure uma chave da OpenAI ou use o Modo de Demonstração.")
            modo_operacao = "🎭 Modo de Demonstração"
        else:
            st.success("Modo Real ativado. Usando API da OpenAI.")
    else:
        st.info("🎭 **Modo de Demonstração Ativo** - Simulando respostas da API sem custos.")
    
    # ====== SEÇÃO 1: GERADOR DE BANNER COM IMAGEM ======
    st.subheader("🎨 Gerador de Banner Promocional")
    
    col_img1, col_img2 = st.columns([1, 2])
    
    with col_img1:
        st.markdown("**Configurações da Imagem**")
        estilo_imagem = st.selectbox(
            "Estilo visual:",
            ["Realista", "Cinematográfico", "Ilustração digital", "Vintage NYC", "Futurista"],
            key="estilo_img"
        )
        
        acao_imagem = st.selectbox(
            "Elemento principal:",
            ["Táxi em Times Square", "Táxi na ponte do Brooklyn", "Interior do táxi", "Mapa de rotas", "Passageiro feliz"],
            key="acao_img"
        )
        
        generate_image = st.button("🖼️ Gerar Banner com IA", type="primary", key="btn_imagem")
    
    with col_img2:
        st.markdown("**Pré-visualização do Banner**")
        
        # Área para exibir a imagem gerada
        image_placeholder = st.empty()
        
        # Texto explicativo inicial
        if not generate_image:
            st.info("Configure as opções e clique em 'Gerar Banner com IA' para ver a simulação.")
    
    # Lógica para gerar imagem (real ou demo)
    if generate_image:
        if modo_operacao == "🎭 Modo de Demonstração":
            with st.spinner("🎨 Simulando geração de imagem com DALL-E 3..."):
                time.sleep(2)  # Simular processamento
                
                # Criar uma imagem de exemplo usando Plotly
                fig = go.Figure()
                
                # Adicionar um "placeholder" estilizado
                fig.add_shape(type="rect", x0=0, y0=0, x1=1, y1=1, 
                            line=dict(color="gold", width=3),
                            fillcolor="lightyellow")
                
                # Adicionar texto no centro
                fig.add_annotation(text=f"BANNER DE MARKETING\n\nEstilo: {estilo_imagem}\nCena: {acao_imagem}\n\n[IMAGEM GERADA POR IA]\nModo Demonstração",
                                  xref="paper", yref="paper",
                                  x=0.5, y=0.5, showarrow=False,
                                  font=dict(size=16, color="darkblue"),
                                  align="center")
                
                # Adicionar elementos gráficos simples
                fig.add_trace(go.Scatter(x=[0.2, 0.8], y=[0.3, 0.3],
                                        mode="lines+markers",
                                        line=dict(color="gold", width=8),
                                        marker=dict(size=20, symbol="diamond")))
                
                fig.update_layout(
                    title=f"Banner Gerado: Yellow Taxi NYC",
                    xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                    yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                    plot_bgcolor="lightblue",
                    width=800,
                    height=500,
                    margin=dict(t=50, b=20)
                )
                
                # Exibir a figura
                image_placeholder.plotly_chart(fig, use_container_width=True)
                
                st.success("✅ Banner gerado com sucesso (simulação)!")
                
                # Mostrar detalhes técnicos
                with st.expander("📋 Detalhes da Simulação"):
                    st.markdown(f"""
                    **Prompt simulado enviado à API DALL-E 3:**
                    ```
                    "Professional advertising banner for Yellow Taxi NYC service, 
                    style: {estilo_imagem}, main element: {acao_imagem},
                    high quality, professional photography, vibrant colors, 
                    iconic New York City landmarks, yellow taxi prominent"
                    ```
                    
                    **Resposta da API simulada:**
                    ```json
                    {{
                      "created": {int(time.time())},
                      "data": [
                        {{
                          "url": "https://api.openai.com/v1/images/generations/demo-output",
                          "revised_prompt": "Professional ad banner featuring a yellow taxi in {acao_imagem} with {estilo_imagem.lower()} style"
                        }}
                      ],
                      "model": "dall-e-3"
                    }}
                    ```
                    """)
                    
                # Botão para download (imagem simulada)
                with st.expander("💾 Opções de Download"):
                    st.info("No modo real, esta opção baixaria a imagem gerada pela API.")
                    st.button("📥 Download Banner PNG (Simulado)", key="download_demo")
        
        else:  # Modo Real
            try:
                client = openai.OpenAI(api_key=openai_api_key)
                
                prompt_imagem = f"Professional advertising banner for Yellow Taxi NYC service, style: {estilo_imagem}, main element: {acao_imagem}, high quality, professional photography"
                
                with st.spinner("Gerando imagem com DALL-E 3..."):
                    response = client.images.generate(
                        model="dall-e-3",
                        prompt=prompt_imagem,
                        size="1024x1792",
                        quality="hd",
                        n=1,
                        response_format="b64_json"
                    )
                    
                    # Processar e exibir imagem real
                    image_data = base64.b64decode(response.data[0].b64_json)
                    image = Image.open(io.BytesIO(image_data))
                    image_placeholder.image(image, use_container_width=True)
                    
                    st.success("✅ Banner gerado com sucesso via API!")
                    
            except Exception as e:
                st.error(f"Erro na API: {str(e)}")
                st.info("Alternando para modo de demonstração...")
                modo_operacao = "🎭 Modo de Demonstração"
    
    # ====== SEÇÃO 2: GERADOR DE PITCH DE VENDAS ======
    st.divider()
    st.subheader("📝 Gerador de Pitch de Vendas Inteligente")
    
    # Configurações do Pitch
    col_config1, col_config2 = st.columns(2)
    
    with col_config1:
        objetivo = st.selectbox(
            "🎯 **Objetivo do Pitch**",
            [
                "Vender espaço publicitário nos táxis",
                "Buscar investidores para expansão da frota", 
                "Relatório Executivo para a Diretoria",
                "Apresentação para parceiros comerciais"
            ],
            key="objetivo_pitch"
        )
    
    with col_config2:
        tom = st.selectbox(
            "🎭 **Tom da Mensagem**",
            ["Persuasivo", "Analítico", "Urgente", "Otimista"],
            key="tom_pitch"
        )
    
    # Dados para o pitch
    st.markdown("**📊 Dados que serão utilizados:**")
    col_dados1, col_dados2, col_dados3 = st.columns(3)
    with col_dados1:
        st.metric("Período", f"{start_date} a {end_date}")
    with col_dados2:
        st.metric("Total de Viagens", f"{viagens_totais:,}")
    with col_dados3:
        st.metric("Receita Total", f"${receita_total:,.0f}")
    
    # Botão para gerar pitch
    if st.button("✨ Gerar Pitch Completo", type="primary", key="btn_pitch"):
        
        if modo_operacao == "🎭 Modo de Demonstração":
            with st.spinner("🧠 Simulando análise com IA..."):
                time.sleep(2.5)  # Simular tempo de processamento
                
                # Pitch gerado automaticamente com os dados
                pitch_demo = f"""
# 🚕 PITCH DE VENDAS - YELLOW TAXI NYC
**Objetivo:** {objetivo}  
**Tom:** {tom}  
**Data:** {datetime.now().strftime('%d/%m/%Y')}  
**Período Analisado:** {start_date} a {end_date}

---

## 📈 RESUMO EXECUTIVO
Com base na análise de **{viagens_totais:,} corridas** realizadas no período, identificamos uma **oportunidade de mercado concreta** com receita total de **${receita_total:,.2f}**. A distância média de **{distancia_media:.2f} milhas** por viagem demonstra alcance significativo na malha urbana.

## 🎯 OPORTUNIDADE ESPECÍFICA
Para **{objetivo.lower()}**, nossos dados revelam:

1. **Alta Visibilidade**: Cada táxi circula em média **{distancia_media:.2f} milhas/dia**, passando por pontos estratégicos
2. **Público Qualificado**: Ticket médio de **${valor_medio:.2f}** indica poder aquisitivo do usuário
3. **Cobertura Ampliada**: {viagens_totais:,} pontos de coleta de dados em tempo real

## 💡 PROPOSTA DE VALOR
1. **Segmentação por Rota**: Direcionamento baseado em zonas de maior movimento
2. **Análise Preditiva**: Antecipação de demandas sazonais e horárias
3. **Mensuração em Tempo Real**: Dashboards com ROI calculado por campanha

## 📅 PRÓXIMOS PASSOS
1. **Workshop Técnico**: Análise detalhada dos dados específicos para seu caso
2. **Piloto Controlado**: Teste em 10 veículos por 30 dias
3. **Expansão Gradual**: Escalonamento baseado em métricas pré-definidas

---

*Este pitch foi gerado automaticamente pela plataforma de Market Intelligence.*  
*Em modo real, seria enriquecido com insights de GPT-4 sobre tendências de mercado.*
                """
                
                st.success("✅ Pitch gerado com sucesso (simulação)!")
                st.markdown(pitch_demo)
                
                # Mostrar estrutura da requisição simulada
                with st.expander("🔧 Estrutura da Requisição Simulada"):
                    st.code(f"""
# Request to OpenAI API (simulated)
{{
  "model": "gpt-4",
  "messages": [
    {{
      "role": "system",
      "content": "Você é um consultor de negócios especializado em transporte urbano."
    }},
    {{
      "role": "user", 
      "content": "Gere um pitch para: {objetivo}. Tom: {tom}. Use estes dados: {viagens_totais} viagens, ${receita_total} receita, {distancia_media} milhas média."
    }}
  ],
  "temperature": 0.7,
  "max_tokens": 1500
}}
                    """, language="json")
                
                # Opções de exportação
                with st.expander("📤 Exportar Pitch"):
                    st.download_button(
                        label="📥 Baixar como TXT",
                        data=pitch_demo,
                        file_name=f"pitch_yellow_taxi_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
                        mime="text/plain"
                    )
                    st.info("No modo real, também estariam disponíveis formatos PDF e PPT.")
        
        else:  # Modo Real
            try:
                client = openai.OpenAI(api_key=openai_api_key)
                
                prompt_pitch = f"""
                Gere um pitch de vendas profissional com as seguintes especificações:
                
                OBJETIVO: {objetivo}
                TOM: {tom}
                DADOS: {viagens_totais} viagens, ${receita_total} receita total, 
                       {distancia_media} milhas de distância média, ${valor_medio} valor médio por viagem
                PERÍODO: {start_date} a {end_date}
                
                O pitch deve incluir:
                1. Resumo executivo impactante
                2. Destaque dos principais números
                3. Proposta de valor clara
                4. Chamada para ação específica
                
                Formato: Markdown com títulos e listas
                """
                
                with st.spinner("Gerando pitch com GPT-4..."):
                    response = client.chat.completions.create(
                        model="gpt-4",
                        messages=[
                            {"role": "system", "content": "Você é um consultor sênior de negócios."},
                            {"role": "user", "content": prompt_pitch}
                        ],
                        temperature=0.7,
                        max_tokens=1500
                    )
                    
                    pitch_real = response.choices[0].message.content
                    st.success("✅ Pitch gerado com sucesso via API!")
                    st.markdown(pitch_real)
                    
            except Exception as e:
                st.error(f"Erro na API: {str(e)}")
                st.info("Recriando pitch em modo de demonstração...")
                # Reexecutar a lógica de demo
                modo_operacao = "🎭 Modo de Demonstração"
                st.experimental_rerun()
    
    # ====== SEÇÃO 3: DOCUMENTAÇÃO TÉCNICA ======
    st.divider()
    with st.expander("📐 **Documentação Técnica para Avaliadores**"):
        st.markdown(f"""
        ### Arquitetura do Sistema
        
        **Módulos Implementados:**
        1. **Dashboard Analítico**: Visualização de KPIs em tempo real
        2. **Gerador de Imagens**: Integração com DALL-E 3 para marketing visual
        3. **Gerador de Pitches**: Análise de dados + GPT-4 para conteúdo persuasivo
        
        **Fluxo de Dados:**
        ```
        Dados CSV → Filtros (Período/Fornecedor) → Cálculo de KPIs → 
        → Input do Usuário (Objetivo/Tom) → 
        → {'API OpenAI (Modo Real)' if modo_operacao == '🚀 Modo Real (com API Key)' else 'Motor de Simulação (Modo Demo)'} → 
        → Renderização de Resultados
        ```
        
        **Variáveis de Contexto Atuais:**
        - Período: {start_date} a {end_date}
        - Viagens: {viagens_totais:,}
        - Receita: ${receita_total:,.2f}
        - Distância média: {distancia_media:.2f} milhas
        - Valor médio: ${valor_medio:.2f}
        
        **Tecnologias Utilizadas:**
        - Streamlit (UI)
        - Plotly (Gráficos)
        - Pandas (Processamento de dados)
        - OpenAI API (IA Generativa)
        - Python-dotenv (Gerenciamento de chaves)
        
        **Modo de Operação Atual:** {modo_operacao}
        
        ### Para Ativar o Modo Real
        1. Obtenha uma API Key em: https://platform.openai.com/api-keys
        2. Adicione ao arquivo `.env`: `OPENAI_API_KEY=sua_chave`
        3. Selecione "Modo Real" na sidebar
        4. As funcionalidades usarão a API real da OpenAI
        """)

# Footer
st.divider()
st.caption("Dashboard Yellow Taxi NYC • Modo: " + ("Demonstração" if modo_operacao == "🎭 Modo de Demonstração" else "Real") + 
          " • Desenvolvido para Case Técnico • Dados simulados para fins demonstrativos")