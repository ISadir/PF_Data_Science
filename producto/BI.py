import streamlit as st

st.title("Dashboards BI :material/finance:")

st.markdown("""
### ¡Bienvenido a la Sección de Business Intelligence!

En esta página, se puede explorar dashboards interactivos que proporcionarán un análisis detallado de varios aspectos críticos del mercado de taxis en Nueva York:

- **Viajes y Ganancias en 2019**: Un análisis de los viajes realizados y las ganancias generadas durante el año 2019.
- **Viajes y Zonas de la Ciudad**: Un mapa interactivo que detalla cómo se distribuyen los viajes a lo largo de las diferentes zonas de Nueva York.
- **Estaciones de Carga Eléctrica y Autos Eléctricos**: Visualiza la red de estaciones de carga eléctrica y la adopción de autos eléctricos en la ciudad.
- **Emisión de CO2 por Medios de Transporte**: Un informe sobre las emisiones de CO2 generadas por los diferentes medios de transporte en Nueva York.

Utiliza estos dashboards para obtener una visión clara y detallada del mercado.
""")

st.header("Mercado de taxis en New York City")

# Incluir el iframe con el dashboard de Power BI
st.components.v1.iframe(
    src="https://app.powerbi.com/view?r=eyJrIjoiNzI0MjkzNGQtMDgyMS00OTliLWEyYTYtMzM3YmJmNTQ2NzMxIiwidCI6IjcxOWU4ZTRkLWZkZDMtNDQxZC05NDcyLTM0MDAxNGJiMTM1NyIsImMiOjR9",  # Reemplaza con tu URL de inserción
    width=800,  # Ancho del iframe
    height=500,  # Alto del iframe
    scrolling=True  # Habilitar el scrolling si el contenido es grande
)

st.subheader("Algunas conclusiones a tener en cuenta")

st.markdown("""
Con una flota inicial de 5 autos, cada uno realizando un promedio de 20 viajes diarios, se pueden destacar varios puntos clave:

- **Gastos e Ingresos Mensuales**: Los gastos promedio mensuales se sitúan entre 25 y 28 mil dólares, mientras que los ingresos varían entre 58 y 62 mil dólares.
- **Retorno de Inversión (ROI)**: El ROI se mantiene en un rango del 10 al 12%, lo que sugiere que la inversión inicial podría recuperarse en aproximadamente 10 meses.
- **Tendencias Anuales**: Si las tendencias actuales se mantienen, los meses de marzo y octubre serían los más favorables para ingresar al mercado.
- **Distribución de Taxis Verdes**: El ratio de taxis verdes es altamente variable. Como era de esperarse, Manhattan tiene la menor presencia, seguido por Staten Island, Queens, y Brooklyn. La mayor concentración se encuentra en el Bronx.
""")


st.header("Autos eléctricos, estaciones de carga y CO2")


# Incluir el iframe con el dashboard de Power BI
st.components.v1.iframe(
    src="https://app.powerbi.com/view?r=eyJrIjoiOTUzYTNhN2QtYmI2NC00ZmNjLThjMTktMmUwNGE2OGU4NWY5IiwidCI6IjcxOWU4ZTRkLWZkZDMtNDQxZC05NDcyLTM0MDAxNGJiMTM1NyIsImMiOjR9",
    width=800,  # Ancho del iframe
    height=500,  # Alto del iframe
    scrolling=True  # Habilitar el scrolling si el contenido es grande
)

st.subheader("Algunas conclusiones a tener en cuenta")

st.markdown("""
Considerando los autos eléctricos disponibles en el mercado y la infraestructura de carga, podemos concluir lo siguiente:

- **Brooklyn** es la mejor opción para iniciar operaciones en zonas de taxis verdes, ya que concentra la mayor cantidad de estaciones de carga en Nueva York, con un 90% de ellas siendo públicas.
- **Precio Promedio de Autos Eléctricos**: Los modelos de autos eléctricos aptos para el transporte de personas y con buen rendimiento tienen un precio promedio de alrededor de 52 mil dólares.
- **Emisiones de CO2**: El volumen de emisiones de CO2 por medios de transporte es variable, aunque ha disminuido ligeramente en comparación con el año anterior. Si se opta por invertir en autos con motor de combustión, se recomiendan marcas como Honda y Volkswagen, que en promedio tienen un menor impacto ambiental y precios más accesibles.
""")

