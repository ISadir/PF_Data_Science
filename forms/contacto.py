import streamlit as st
import re
import requests

# creditos: https://www.youtube.com/watch?v=9n4Ch2Dgex0

WEBHOOKS_URL = st.secrets['WEBHOOKS_URL']

def validar_email(email):
    patron = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$"
    return re.fullmatch(patron, email) is not None

def contactar():
    with st.form('Su consulta'):
        email = st.text_input('Su email')
        mensaje = st.text_area('Su consulta')
        button = st.form_submit_button('Enviar')

        if button:
            if not WEBHOOKS_URL:
                st.error('Ocurrio un error inesperado, intente nuevamente')
                st.stop()

            if not email or not validar_email(email):
                st.error(':material/mark_email_read: Por favor ingrese una dirección de mail válida para que lo contactemos')
                st.stop()

            if not mensaje:
                st.error(':material/contract_edit: No olvide escribirnos su consulta')
                st.stop()

            datos ={'emal': email, 'mensaje' : mensaje}
            respuesta = requests.post(WEBHOOKS_URL, json= datos)

            if respuesta.status_code == 200:
                st.success('Consulta enviada correctamente. Contestaremos su pregunta en breve, revise su mail')

            else: 
                st.error('Ocurrio un error, intente nuevamente')
