# Este modelo es muy rapido pero solo repite lo que dice el archivo de texto, no es muy util para responder preguntas

import streamlit as st
from langchain_ollama.llms import OllamaLLM
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
import time
import re

path = 'assets/FAQ2.txt' # Ruta al archivo de texto con preguntas y respuestas

# Configuro el modelo Ollama
llm = OllamaLLM(model='llama3.1:latest')

# Defino una función para dividir el archivo de texto en chunks más pequeños
def dividir_archivo_en_chunks(path, chunk_size=500):
    # Leo el archivo completo
    with open(path, 'r', encoding='utf-8') as file:
        texto = file.read()
    # Divido el texto en partes más pequeñas de tamaño chunk_size
    return [texto[i:i+chunk_size] for i in range(0, len(texto), chunk_size)]

# Defino una función para encontrar el chunk relevante y extraer la respuesta
def encontrar_chunk_relevante(chunks, pregunta):
    # Convierto los chunks y la pregunta en vectores TF-IDF
    vectorizer = TfidfVectorizer().fit_transform(chunks + [pregunta])
    vectors = vectorizer.toarray()
    # Calculo la similitud entre la pregunta y los chunks
    similarity_scores = cosine_similarity(vectors[-1].reshape(1, -1), vectors[:-1])
    # Encuentro el chunk más relevante basado en la similitud
    chunk_relevante = chunks[similarity_scores.argmax()]
    
    # Utilizo una expresión regular para buscar la pregunta y extraer la respuesta correspondiente
    patron = re.compile(r'pregunta:\s*(.*?)\s*respuesta:\s*(.*)', re.IGNORECASE)
    matches = patron.findall(chunk_relevante)
    # Comparo la pregunta del usuario con las preguntas en el chunk y retorno la respuesta correspondiente
    for match in matches:
        if pregunta.lower() in match[0].lower():
            return match[1]
    # Si no encuentro una respuesta, retorno un mensaje indicando que no se encontró respuesta
    return "Lo siento, no tengo respuesta para esa pregunta. Por favor contactese con el equipo para saber mas."

# Configuro la interfaz de Streamlit
st.title("Asistente virtual 🐱‍💻")

# Inicializo la variable para almacenar los mensajes si no existe
if "messages" not in st.session_state:
    st.session_state.messages = []

# Inicializo la variable para mostrar el mensaje de bienvenida si es la primera vez
if "first_message" not in st.session_state:
    st.session_state.first_message = True

# Divido el archivo de texto en chunks para facilitar la búsqueda de respuestas
chunks = dividir_archivo_en_chunks(path)

# Muestro los mensajes anteriores en el chat
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Si es la primera vez que se ejecuta, muestro un mensaje de bienvenida
if st.session_state.first_message:
    with st.chat_message("assistant"):
        st.markdown("Hola, ¿cómo puedo ayudarle hoy?")
    st.session_state.messages.append({"role":"assistant", "content": "Hola!, ¿cómo puedo ayudarle hoy?"})
    st.session_state.first_message = False

# Capturo la entrada del usuario y genero la respuesta
if prompt := st.chat_input("Tu consulta"):
    with st.chat_message("user"):
       st.markdown(prompt)
    st.session_state.messages.append({"role":"user", "content":prompt})

    # Encuentro el chunk relevante y obtengo la respuesta correspondiente
    start_time = time.time()
    respuesta_obtenida = encontrar_chunk_relevante(chunks, prompt)
    end_time = time.time()

    elapsed_time = end_time - start_time
    print(f"Tiempo de respuesta: {elapsed_time} segundos")

    # Muestro la respuesta gradualmente, letra por letra
    with st.chat_message("assistant"):
        response_placeholder = st.empty()
        partial_response = ""
        for i, char in enumerate(respuesta_obtenida):
            partial_response += char
            if i % 10 == 0:  # Actualizo cada 10 caracteres
                response_placeholder.markdown(partial_response)
                time.sleep(0.05)
        response_placeholder.markdown(partial_response)
    
    # Almaceno la respuesta completa en el historial de mensajes
    st.session_state.messages.append({"role":"assistant", "content":respuesta_obtenida})
