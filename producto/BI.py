import streamlit as st

st.title("Dashboards BI")
st.text("En esta sección se presentan las graficas orientadas al análisis BI")
st.header("Dashboard relativo al mercado de taxis en NY")


# Incluir el iframe con el dashboard de Power BI
st.components.v1.iframe(
    src="https://app.powerbi.com/view?r=eyJrIjoiNzI0MjkzNGQtMDgyMS00OTliLWEyYTYtMzM3YmJmNTQ2NzMxIiwidCI6IjcxOWU4ZTRkLWZkZDMtNDQxZC05NDcyLTM0MDAxNGJiMTM1NyIsImMiOjR9",  # Reemplaza con tu URL de inserción
    width=800,  # Ancho del iframe
    height=500,  # Alto del iframe
    scrolling=True  # Habilitar el scrolling si el contenido es grande
)

st.subheader("Concluciones")

st.text("...")

st.header("Dashboard relativo a CO2, estaciones de carga eléctrica y eficiencia de los autos")


# Incluir el iframe con el dashboard de Power BI
st.components.v1.iframe(
    src="https://app.powerbi.com/view?r=eyJrIjoiOTUzYTNhN2QtYmI2NC00ZmNjLThjMTktMmUwNGE2OGU4NWY5IiwidCI6IjcxOWU4ZTRkLWZkZDMtNDQxZC05NDcyLTM0MDAxNGJiMTM1NyIsImMiOjR9",
    width=800,  # Ancho del iframe
    height=500,  # Alto del iframe
    scrolling=True  # Habilitar el scrolling si el contenido es grande
)

st.subheader("Concluciones")

st.text("...")