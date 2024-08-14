import streamlit as st
from langchain_ollama.llms import OllamaLLM
import time

path = 'assets/FAQ.txt'  # Ruta al archivo de texto con preguntas y respuestas

# Configuro el modelo Ollama
llm = OllamaLLM(model='llama3.1:latest')

# Función para cargar y procesar el archivo de texto con caché
@st.cache_data
def cargar_archivo(path):
    with open(path, 'r', encoding='utf-8') as file:
        texto = file.read()
    return texto

# Función para obtener una respuesta generada por el LLM basada en el contexto
def obtener_respuesta_llm(pregunta_usuario, contexto):
    prompt = f"Contexto:\n{contexto}\n\nPregunta del usuario: {pregunta_usuario}\nPor favor, responde de manera clara y concisa:"
    respuesta = llm(prompt)
    return respuesta.strip()

# Cargar el archivo y obtener el contenido
contexto = cargar_archivo(path)

# Configurar la interfaz de Streamlit
st.title("Asistente virtual 🐱‍💻")

# Inicializar el historial de mensajes si no existe
if "messages" not in st.session_state:
    st.session_state.messages = []

# Mostrar el mensaje de bienvenida si es la primera vez
if "first_message" not in st.session_state:
    st.session_state.first_message = True
    st.session_state.messages.append({"role": "assistant", "content": "Hola, ¿cómo puedo ayudarte hoy?"})

# Mostrar mensajes anteriores en el chat
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Capturar la entrada del usuario y generar la respuesta
if prompt := st.chat_input("Tu consulta"):
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Obtener la respuesta completa
    start_time = time.time()
    respuesta_obtenida = obtener_respuesta_llm(prompt, contexto)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Tiempo de respuesta: {elapsed_time} segundos")

    # Mostrar la respuesta gradualmente, letra por letra
    with st.chat_message("assistant") as response_message:
        response_placeholder = st.empty()
        partial_response = ""
        for i, char in enumerate(respuesta_obtenida):
            partial_response += char
            if i % 10 == 0:  # Actualiza cada 10 caracteres
                response_placeholder.markdown(partial_response)
                time.sleep(0.05)  # Reduce el tiempo de espera para una visualización más rápida
        response_placeholder.markdown(partial_response)  # Asegúrate de mostrar el mensaje completo al final

    # Actualizar el historial de mensajes
    st.session_state.messages.append({"role": "assistant", "content": respuesta_obtenida})
