#agentes: que divida archivo en base de dato de texto usar metodo de similaridad por coseno (Todo en langchain)
#Y crear un documento con todos los datos a necesitar. Pipelines
#Retrieval Augmented Generation (RAG)
path = 'assets/FAQ2.txt'
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM

# Configurar Ollama
llm = OllamaLLM(model='llama3.1:latest')

# Función para obtener la respuesta del modelo
def respuesta(llm, pregunta):
    with open(path,'r') as file:
        contexto = file.read() # leer el archivo de texto
    template = """{contexto} 

    Pregunta: {pregunta}
    Respuesta:""" # plantilla para el prompt

    prompt = ChatPromptTemplate.from_template(template) # crear el prompt

    chain = prompt | llm # concatenar el prompt con el modelo

    return chain.invoke({"contexto": contexto, "pregunta": pregunta}) # invocar el modelo

#Streamlit

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


    response = respuesta(llm, prompt) # obtener respuesta

    with st.chat_message("assistant"):
       st.markdown(response) #respuesta del bot
    st.session_state.messages.append({"role":"assistant", "content":response}) #agregar al historial