import streamlit as st

st.title("Dashboards BI")
st.text("En esta sección se presentan las graficas orientadas al análisis BI")
st.header("Dashboard relativo al mercado de taxis en NY")


# Incluir el iframe con el dashboard de Power BI
st.components.v1.iframe(
    src="https://app.powerbi.com/view?r=eyJrIjoiMjYwMDJlNGMtZTJkMy00MTVlLWI3ZDUtMDY0ZjNkYmI2YzQyIiwidCI6IjcxOWU4ZTRkLWZkZDMtNDQxZC05NDcyLTM0MDAxNGJiMTM1NyIsImMiOjR9&filterPaneEnabled=false",  # Reemplaza con tu URL de inserción
    width=800,  # Ancho del iframe
    height=600,  # Alto del iframe
    scrolling=True  # Habilitar el scrolling si el contenido es grande
)

st.subheader("Concluciones")

st.text("...")

st.header("Dashboard relativo a CO2, estaciones de carga eléctrica y eficiencia de los autos")


# Incluir el iframe con el dashboard de Power BI
st.components.v1.iframe(
    src="https://app.powerbi.com/groups/me/reports/a526bff2-981c-4e64-b3a3-484ae40898e1/4fac95764ee9b89ab887",
    width=800,  # Ancho del iframe
    height=600,  # Alto del iframe
    scrolling=True  # Habilitar el scrolling si el contenido es grande
)

st.subheader("Concluciones")

st.text("...")