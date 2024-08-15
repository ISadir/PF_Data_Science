import streamlit as st
import pandas as pd
import matplotlib as plt
from datetime import date
from prophet import Prophet
from prophet.plot import plot_plotly
from plotly import graph_objs as go

# creditos: https://www.youtube.com/watch?v=0E_31WqVzCY

# start = "2019-01-01"
# today = date.today().strftime("%Y-%m-%d")

st.title("Forecast")

st.subheader("En esta sección se presentan las graficas orientadas al análisis BI")

@st.cache_data
def cargar(csv):
    df = pd.read_csv(csv)
    return df

df = cargar("original data/auxiliar.csv")

st.subheader('Tabla de datos')
st.write(df.head())

tipos1 = ("green", "yellow")
selec1 = st.selectbox("Selecciones la predicción que desea calcular", tipos1)

tipos2 = ("tarifa_prom", "distancia_prom", "distancia_total", "viajes_totales")
selec2 = st.selectbox("Selecciones la predicción que desea calcular", tipos2)

def data_lista(df, tipo_taxi, columna):
    df_filtrado = df[df['taxi'] == tipo_taxi]
    df_prophet = df_filtrado[['mes', columna]].copy()
    df_prophet.rename(columns={'mes': 'ds', columna: 'y'}, inplace=True)
    df_prophet['ds'] = df_prophet['ds'].astype(str) + '-2019'
    df_prophet['ds'] = pd.to_datetime(df_prophet['ds'], format='%m-%Y')

    return df_prophet

df_prophet = data_lista(df, selec1, selec2)

def graficar_original(df_prophet, selec2):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df_prophet["ds"], y=df_prophet["y"], marker=dict(symbol='circle', color='royalblue')))
    fig.layout.update(title_text= "Datos históricos",yaxis_title=(f"{selec2} de {selec1} taxis") , xaxis_rangeslider_visible=True)
    st.plotly_chart(fig)

graficar_original(df_prophet, selec2)

periodos = st.slider("Seleccione la cantidad de periodos:", 1, 5 )

def predecir_columna(df_prophet, periodos, selec1, selec2):
    model = Prophet(changepoint_prior_scale=0.1, seasonality_prior_scale=20.0, seasonality_mode='additive')
    model.add_seasonality(name='weekly', period=7, fourier_order=5)

    model.fit(df_prophet)
    future = model.make_future_dataframe(periods=periodos, freq='M')
    forecast = model.predict(future)

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df_prophet["ds"], y=df_prophet["y"], name='Datos Históricos', marker=dict(symbol='circle', color='royalblue')))
    fig.add_trace(go.Scatter(x=forecast['ds'], y=forecast['yhat'], name='Predicción', marker=dict(symbol='diamond', color='white')))
    fig.add_trace(go.Scatter(x=forecast['ds'].tolist() + forecast['ds'][::-1].tolist(), y=forecast['yhat_upper'].tolist() + forecast['yhat_lower'][::-1].tolist(), fill='toself', fillcolor='rgba(255, 255, 255, 0.2)', line=dict(color='rgba(255, 255, 255, 0)'), name='Intervalo de predicción'))
    fig.layout.update(xaxis_title='Fecha', yaxis_title=selec2 ,title_text= (f"Predicción para {selec2} de {selec1} taxis"), xaxis_rangeslider_visible=True)
    st.plotly_chart(fig)
    
#     respuesta = f'La predicción para taxis {tipo_taxi} para el siguiente mes de su valor {columna} es {round(forecast["yhat"].iloc[-1], 3)}'
    return model, forecast

model, forecast = predecir_columna(df_prophet, periodos, selec1, selec2)

st.text(forecast.head())

# fig1 = model.plot_components(forecast)
# st.write(fig1)