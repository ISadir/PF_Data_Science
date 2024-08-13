import streamlit as st
from langchain_ollama import OllamaLLM
#agentes: que divida archivo en base de dato de texto usar metodo de similaridad por coseno (Todo en langchain)
#Y crear un documento con todos los datos a necesitar. Pipelines
#Retrieval Augmented Generation (RAG)

st.title("Asistente virtual 🐱‍💻")

llm = OllamaLLM(model='llama3.1:latest')

if "messages" not in st.session_state:
    st.session_state.messages = [] # almacena el historial del chat

if "first_message" not in st.session_state:
    st.session_state.first_message = True # flag para dar la bienvenida

for message in st.session_state.messages:
    with st.chat_message(message["role"]): # muestra los mensajes If name is "user" or "human", the message will have a default user icon. If name is "ai" or "assistant", the message will have a default bot icon.
        st.markdown(message["content"])

if st.session_state.first_message: # mensaje de bienvenida
    with st.chat_message("assistant"):
        st.markdown("Hola, ¿cómo puedo ayudarle hoy?")

    st.session_state.messages.append({"role":"assistant", "content": "Hola!, ¿cómo puedo ayudarle hoy?"}) #agregar al historial
    st.session_state.first_message = False

if prompt := st.chat_input("Tu consulta"):
    with st.chat_message("user"):
       st.markdown(prompt) # consulta del usuario
    st.session_state.messages.append({"role":"user", "content":prompt}) #agregar al historial


    response = llm.invoke(prompt)

    with st.chat_message("assistant"):
       st.markdown(response) #respuesta del bot
    st.session_state.messages.append({"role":"assistant", "content":prompt}) #agregar al historial
