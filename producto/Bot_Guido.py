import streamlit as st
from langchain_ollama import OllamaLLM
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
#agentes: que divida archivo en base de dato de texto usar metodo de similaridad por coseno (Todo en langchain)
#Y crear un documento con todos los datos a necesitar. Pipelines
#Retrieval Augmented Generation (RAG)

def jaccard_similarity(query, document):
    query = query.lower().split(" ")
    document = document.lower().split(" ")
    intersection = set(query).intersection(set(document))
    union = set(query).union(set(document))
    return len(intersection) / len(union)

def calcular_similaridad_jac(prompt, faq_data):
    # Divide el FAQ en preguntas y respuestas
    faqs = faq_data.split("\n\n")  # Asumiendo que las preguntas y respuestas están separadas por dos saltos de línea

    # Inicializa la mejor similitud
    best_similarity = 0

    # Recorre cada FAQ y calcula la similitud con el prompt
    for faq in faqs:
        if ':' in faq:  # Verifica que el texto contiene una pregunta y respuesta
            pregunta, respuesta = faq.split(':', 1)
            pregunta = pregunta.strip()
            respuesta = respuesta.strip()
            
            # Calcula la similitud Jaccard para la pregunta
            similarity = jaccard_similarity(prompt, pregunta)
            if similarity > best_similarity:
                best_similarity = similarity
                best_response = respuesta

    return best_response if best_similarity > 0.2 else None  # Ajusta el umbral según sea necesario

def respuesta_jac(llm, prompt):
    # Leer el archivo FAQ.txt
    with open("assets/FAQ2.txt", "r", encoding="utf-8") as file:
        faq_data = file.read()

    # Calcular la similitud entre el prompt y el contenido del FAQ
    best_response = calcular_similaridad_jac(prompt, faq_data)

    if best_response:
        # Si se encuentra una respuesta adecuada en el FAQ
        return best_response
    else:
        # Obtener la respuesta utilizando el conocimiento general del LLM
        response = llm.generate(prompts=[f"Pregunta: {prompt}\n\nRespuesta:"])
        return response.generations[0][0].text

def calcular_similaridad_cos(prompt, faq_data):
    # Combina el prompt y el contenido del FAQ para calcular la similaridad
    textos = [prompt, faq_data]
    
    # Transforma los textos en vectores TF-IDF
    vectorizer = TfidfVectorizer().fit_transform(textos)
    
    # Calcula la similaridad coseno
    similarity_matrix = cosine_similarity(vectorizer[0:1], vectorizer)
    
    # Retorna la similaridad entre el prompt y el contenido del FAQ
    return similarity_matrix[0][1]

def respuesta_cos(llm, prompt):
    # Leer el archivo FAQ.txt
    with open("assets/FAQ2.txt", "r", encoding="utf-8") as file: #Archivo txt
        faq_data = file.read()
    
    # Calcular la similitud entre el prompt y el contenido del FAQ
    similarity_score = calcular_similaridad_cos(prompt)

    # Calcular la similitud entre el prompt y el contenido del archivo FAQ.txt
    similarity_score = calcular_similaridad_cos(prompt, faq_data) #Para archivo txt

    # Si la similitud es mayor a un umbral determinado, seleccionar la respuesta correspondiente
    if similarity_score > 0.8:
        # Obtener la respuesta utilizando el modelo LLM y el contenido del archivo FAQ.txt
        #response = llm.generate(prompts=[f"Basado en la siguiente información: {faq_data}\n\nPregunta: {prompt}\n\nRespuesta:"])
        response = llm.generate(prompts=[f"Este es un extracto de un archivo FAQ que contiene información relevante para tu pregunta:\n\n{faq_data}\n\nPregunta: {prompt}\n\nPor favor, proporciona una respuesta basada en la información anterior."])
    else:
        # Obtener la respuesta utilizando el conocimiento general del LLM
        response = llm.generate(prompts=[f"Pregunta: {prompt}\n\nRespuesta:"])

    return response.generations[0][0].text

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


    response = respuesta_jac(llm, prompt) #Cambiar si desea usar la similaridad por coseno o jaccard

    with st.chat_message("assistant"):
       st.markdown(response) #respuesta del bot
    st.session_state.messages.append({"role":"assistant", "content":response}) #agregar al historial

