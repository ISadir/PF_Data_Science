import streamlit as st
from langchain_ollama.llms import OllamaLLM
import time
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain import PromptTemplate
from langchain.chains import LLMChain
from langchain_community.vectorstores import FAISS
from langchain_google_vertexai import VertexAIEmbeddings
import vertexai


from forms.contacto import contactar

st.title("🚕 Bienvenido")
st.text('Explicación de uso')

@st.dialog('¿Tiene alguna duda?')
def mostrar_contacto():
    contactar()


col1, col2 = st.columns(2, gap='small', vertical_alignment='center')

with col1:
    st.image('assets/logo.png', width= 300)

with col2:
    st.title('Contacte con nosotros', anchor=False)
    st.write('Por cualquier pregunta, no dude en contactar con nosotros, pero no olvide consultar a nuestro asistente virtual :material/smart_toy:')
    if st.button(':material/contact_mail: Contactenos'):
        mostrar_contacto()


st.title("")

st.title("Asistente virtual :material/smart_toy:")

vertexai.init(project='GOOGLE_CLOUD_PROJECT', location="us-central1")

embeddings = VertexAIEmbeddings(model_name="textembedding-gecko-multilingual@001")

path = 'assets/FAQ.txt'  # Ruta al archivo de texto con preguntas y respuestas

# Configuro el modelo Ollama
llm = OllamaLLM(model='llama3.1:latest')

def carga_chunks_db(path):
    # Leo el archivo completo
    with open(path, 'r', encoding='utf-8') as file:
        texto = file.read()
    # Divido el texto en partes más pequeñas de tamaño chunk_size con un overlap en caso de ser necesario
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    split_text = text_splitter.split_text(texto)
    # Creo la base de datos FAISS
    db = FAISS.from_texts(split_text, embeddings)
    return db

def get_response(path, query, k=2):
    db = carga_chunks_db(path)
    # Realizo la búsqueda de documentos similares
    docs = db.similarity_search(query, k=k)
    # Obtengo el contenido de los documentos
    docs_page_content = " ".join([d.page_content for d in docs])
    # Creo el prompt para el modelo
    prompt = PromptTemplate(
        input_variables=["question", "docs"],
        template="""
        You are a helpful assistant that that can answer questions about a company project 
        based on the documents of this project. Also you're talking to the user of the project so don't forget to be polite and 
        don't talk about the documents where you're getting the information.
        
        Answer the following question: {question}
        By searching the following document: {docs}
        
        Only use the factual information from the document to answer the question.
        
        If you feel like you don't have enough information to answer the question, say "Lo siento no tengo informacion sobre eso.
        Para saber mas por favor pongase en contacto con el equipo de Urban Data.".
        
        Your answers shouldn't be too verbose, should be detailed, fast and always in spanish.
        """,
    )
    # Creo la cadena de procesamiento
    chain = LLMChain(llm=llm, prompt=prompt)
    # Obtengo la respuesta del modelo
    response = chain.run(question=query, docs=docs_page_content)
    # Elimino el salto de línea final
    response = response.replace("\n", "")
    return response

# Configurar la interfaz de Streamlit
st.title("Asistente virtual ':material/smart_toy:'")

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
    respuesta_obtenida = get_response(path, prompt)
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
                time.sleep(0.05)  # Añade un pequeño retraso para simular la velocidad de escritura
        response_placeholder.markdown(partial_response)  # Muestra el mensaje completo al final

    # Actualizar el historial de mensajes
    st.session_state.messages.append({"role": "assistant", "content": respuesta_obtenida})
