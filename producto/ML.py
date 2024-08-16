import streamlit as st
import pandas as pd
import matplotlib as plt
from datetime import date
from prophet import Prophet
from prophet.plot import plot_plotly
from plotly import graph_objs as go
import matplotlib.dates as mdates


# creditos: https://www.youtube.com/watch?v=0E_31WqVzCY
st.title("Forecasting :material/timeline:")

# Cargar y guardar en cache y mostrar la data

import streamlit as st

st.markdown("""
### ¡Bienvenido a la Sección de Predicciones Avanzadas!

En esta página, se puede explorar las proyecciones futuras de las principales métricas relacionadas con el mercado de taxis en Nueva York. Utilizando técnicas de machine learning, hemos creado modelos que predicen:

- **Tarifa Promedio (tarifa_prom)**: Estimación de la tarifa media que los pasajeros pagarán.
- **Tarifa Total (tarifa_total)**: Estimación de la tarifa total del día.      
- **Distancia Promedio (distancia_prom)**: Predicción de la distancia media recorrida por viaje.
- **Distancia Total (distancia_total)**: Proyección de la distancia total por día que cubrirán todos los viajes.
- **Viajes Totales (viajes_totales)**: Pronóstico del número total de viajes realizados por día.

Estas predicciones ayudarán a anticipar tendencias tanto para taxis verdes como amarillos y tomar decisiones informadas.
""")


@st.cache_data
def cargar(csv):
    df = pd.read_csv(csv)
    return df

df = cargar("data/auxiliar_diario.csv")

st.subheader('Tabla de datos')
st.write(df.head())

# listas para selecionar las predicciones
tipos1 = ("green", "yellow")
selec1 = st.selectbox("Selecciones la predicción que desea calcular", tipos1)

tipos2 = ("tarifa_prom", "tarifa_total", "distancia_prom", "distancia_total", "viajes_totales")
selec2 = st.selectbox("Selecciones la predicción que desea calcular", tipos2)


# creado de la tabla para prophet
def data_lista(df, tipo_taxi, columna):
    df_filtrado = df[df['taxi'] == tipo_taxi]
    df_prophet = df_filtrado[['mes', 'dia', columna]].copy()
    df_prophet['dias'] = df_prophet['mes'].astype(str) + '-' + df_prophet['dia'].astype(str) + '-2019'
    df_prophet.rename(columns={'dias': 'ds', columna: 'y'}, inplace=True)
    df_prophet['ds'] = pd.to_datetime(df_prophet['ds'], format='%m-%d-%Y')

    return df_prophet
    

df_prophet = data_lista(df, selec1, selec2)

#grafica de la data original
def graficar_original(df_prophet, selec2):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df_prophet["ds"], y=df_prophet["y"], marker=dict(symbol='circle', color='royalblue')))
    fig.layout.update(title_text= "Datos históricos",yaxis_title=(f"{selec2} de {selec1} taxis") , xaxis_rangeslider_visible=True)
    st.plotly_chart(fig)

graficar_original(df_prophet, selec2)

periodos = st.slider("Seleccione la cantidad de periodos:", 1, 60 )

def predecir_columna(df_prophet, periodos, selec1, selec2):
    model = Prophet(changepoint_prior_scale=0.05, seasonality_prior_scale=10.0, seasonality_mode='additive')
    model.add_seasonality(name='weekly', period=7, fourier_order=2)
    model.fit(df_prophet)
    future = model.make_future_dataframe(periods=periodos)
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

st.subheader("Tendencia anual y semanal")

plt.style.use('dark_background')
fig1 = model.plot_components(forecast)
            
for ax in fig1.axes:
    for line in ax.get_lines():
        line.set_color('white')
st.write(fig1)