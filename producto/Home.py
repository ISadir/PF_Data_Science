import streamlit as st
from forms.contacto import contactar

st.title("🚕 Bienvenido")
st.text('Explicación de uso')

@st.dialog('¿Tiene alguna duda?')
def mostrar_contacto():
    contactar()


col1, col2 = st.columns(2, gap='small', vertical_alignment='center')

with col1:
    st.image('assets\logo.png', width= 300)

with col2:
    st.title('Contacte con nosotros', anchor=False)
    st.write('Por cualquier pregunta, no dude en contactar con nosotros, pero no olvide consultar a nuestro asistente virtual :material/smart_toy:')
    if st.button(':material/contact_mail: Contactenos'):
        mostrar_contacto()

