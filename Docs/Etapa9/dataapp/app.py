# Importando as bibliotecas
import streamlit as st
import pandas as pd 
import plotly.express as px
from datetime import datetime
import os


# 1. Configuração da página
st.set_page_config(page_title="Dashboard Yellow Taxi", layout="wide")

st.title("Dashboard Sobre Análise Exploratória dos Dados (EDA) - Yellow Taxi NYC")
st.markdown("""
            Este Data app explora os dados sobre viagens de Taxi da linha amarela de New York, 
            com objetivo de buscar identificar oportunidades de transformação dos dados brutos em insights. 
            """)

# 2. Carregamento e limpeza dos dados
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

# 3. Carregar os dados
try:
    df = load_data()
    st.success("Dados carregados com sucesso!")
except Exception as e:
    st.error(f'Erro ao carrgar os dados: {e}')
    st.stop()
    
# 4. Filtros (sidebar)
st.sidebar.header('Filtros')
# Obter datas mínima e máxima do dataset
min_date = df['data_real'].min().date()
max_date = df['data_real'].max().date()

# Ajuste nos parâmetros Data com parâmetros corretos
date_range = st.sidebar.date_input(
    "Selecione o Período:",
    value=(min_date, max_date),
    min_value=min_date,
    max_value=max_date
)

# Aplicar filtro de datas
if len(date_range) == 2:
    start_date, end_date = date_range
    start_datetime = pd.Timestamp(start_date)
    end_datetime = pd.Timestamp(end_date) + pd.Timedelta(days=1)  # Incluir todo o dia final
    df_filtered = df[(df['data_real'] >= start_datetime) & (df['data_real'] <= end_datetime)]
else:
    df_filtered = df

st.sidebar.info(f"Período selecionado: {len(date_range)} dias")

# 5. KPI (Mesmos da camada Gold)
col1, col2, col3 = st.columns(3)

receita_total = df_filtered['total_amount'].sum()
viagens_totais = df_filtered.shape[0]
distancia_media = df_filtered['trip_distance'].mean()

# Coluna métrica
col1.metric("Receita total", f"${receita_total:,.2f}")
col2.metric("Total de Viagens", f"{viagens_totais:,}")
col3.metric("Distância Média", f"{distancia_media:.2f} milhas")

# 6. Visualizações
st.divider()

col_graf1, col_graf2 = st.columns(2)

with col_graf1:
    st.subheader("Evolução Receita por Dia")
    
    # Agrupamento dos dados por dia
    df_dia = df_filtered.copy()
    df_dia['data_dia'] = df_dia['data_real'].dt.date
    df_dia_agrupado = df_dia.groupby('data_dia')['total_amount'].sum().reset_index()
    
    if not df_dia_agrupado.empty:
        fig_line = px.line(df_dia_agrupado, x='data_dia', y='total_amount', 
                          title='Receita Diária', labels={'data_dia': 'Data', 'total_amount': 'Receita ($)'})
        st.plotly_chart(fig_line, use_container_width=True)
    else:
        st.info("Nenhum dado disponível para o período selecionado")

    
with col_graf2:
    st.subheader("Distribuição de Valor por Fornecedor")
    
    if 'VendorID' in df_filtered.columns:
        # Agrupar por VendorID
        df_vendor = df_filtered.groupby('VendorID')['total_amount'].sum().reset_index()
        
        if not df_vendor.empty:
            fig_bar = px.bar(df_vendor, x='VendorID', y='total_amount', 
                            title='Receita por Fornecedor', 
                            labels={'VendorID': 'Fornecedor', 'total_amount': 'Receita Total ($)'})
            st.plotly_chart(fig_bar, use_container_width=True)
        else:
            st.info("Nenhum dado de fornecedor disponível")
    else:
        st.warning("Coluna 'VendorID' não encontrada no dataset")
    
st.subheader("Distribuição das Distâncias das Viagens")
fig_hist = px.histogram(df_filtered, x='trip_distance', nbins=50,
                       title='Distribuição de Distâncias',
                       labels={'trip_distance': 'Distância (milhas)', 'count': 'Número de Viagens'})
fig_hist.update_layout(bargap=0.1)
st.plotly_chart(fig_hist, use_container_width=True)

# 8. Amostra dos dados (Tabela)
st.subheader("Visualização das Amostras Brutas")
st.dataframe(df_filtered.head(50))

# 9. Estatísticas resumidas
with st.expander("Ver Estatísticas Detalhadas"):
    st.write("**Estatísticas Descritivas:**")
    st.dataframe(df_filtered.describe())
    
    st.write("**Informações do Dataset:**")
    buffer = pd.io.common.StringIO()
    df_filtered.info(buf=buffer)
    st.text(buffer.getvalue())