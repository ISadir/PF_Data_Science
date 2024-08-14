import streamlit as st

# Páginas

pagina1 = st.Page(
    page = 'producto/Home.py',
    title = 'Home',
    icon = '🚕', 
    default= True,)

pagina2 = st.Page(
    page = 'producto/ML.py',
    title = 'Forescasting',
    icon = ':material/timeline:')

pagina3 = st.Page(
    page = 'producto/BI.py',
    title = 'Dashboards BI',
    icon = ':material/finance:')

pagina4 = st.Page(
    page = 'producto/Bot_Lento.py',
    title = 'Asistente virtual',
    icon = ':material/smart_toy:')

pagina5 = st.Page(
    page = 'producto/Bot_Rapido.py',
    title = 'Asistente virtual Rapido',
    icon = ':material/smart_toy:')

pg = st.navigation(pages=[pagina1, pagina2, pagina3, pagina4, pagina5])
pg.run()

st.logo('assets\logo3.png')
st.sidebar.text('Urban Data. 2024')