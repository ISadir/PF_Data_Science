import streamlit as st
from langchain_ollama.llms import OllamaLLM
import time
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_community.vectorstores import FAISS
from langchain_google_vertexai import VertexAIEmbeddings
import vertexai
from langchain_google_vertexai import VertexAI
from forms.contacto import contactar
from google.oauth2 import service_account

st.title("🚕 ¡Bienvenido!")

st.markdown(
    """
    <p style="text-align: justify;">
    Esta aplicación es una Plataforma de Análisis Avanzado para adentrarse y entender el mercado de taxis en la ciudad de Nueva York. 
    Explora insights poderosos a través de nuestros análisis de datos, combinando la precisión del machine learning con la versatilidad 
    del business intelligence. Ya sea que busques predicciones futuras o una comprensión profunda de tus datos, estás en el lugar correcto. 
    </p>
    """, 
    unsafe_allow_html=True
)

@st.dialog('¿Tiene alguna duda?')
def mostrar_contacto():
    contactar()


col1, col2 = st.columns(2, gap='small', vertical_alignment='center')

with col1:
    st.image('assets/logo.png', width= 300)

with col2:
    st.header('Contacte con nosotros', anchor=False)
    st.write('Por cualquier pregunta de uso o sobre los datos, no dude en contactar con nosotros. \n\n Pero primero, no olvide consultar a nuestro asistente virtual :material/smart_toy:')
    if st.button(':material/contact_mail: Contactenos'):
        mostrar_contacto()

PROJECT_ID = st.secrets['PROJECT_ID']
CREDENTIALS_ST = st.secrets['vertex']

CREDENTIALS = service_account.Credentials.from_service_account_info(CREDENTIALS_ST)

vertexai.init(project= PROJECT_ID, location="us-central1", credentials = CREDENTIALS)

#embeddings = VertexAIEmbeddings(model_name="textembedding-gecko-multilingual@001")
embeddings = VertexAIEmbeddings(
    model_name="textembedding-gecko-multilingual@001",
    batch_size=4  # Ajusta según tus necesidades
)

path = 'assets/FAQ.txt'  # ruta al archivo de texto con preguntas y respuestas

# configuro el modelo ollama

llm = VertexAI(model_name= "text-bison") #Contesta hay que configurar el prompt para que responda preguntas basicas


def carga_chunks_db(path):
    # leo el archivo completo
    with open(path, 'r', encoding='utf-8') as file:
        texto = file.read()
    # divido el texto en partes más pequeñas de tamaño chunk_size con un overlap en caso de ser necesario
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    split_text = text_splitter.split_text(texto)
    # creo la base de datos faiss
    db = FAISS.from_texts(split_text, embeddings)
    return db

def get_response(path, query, k=5):
    db = carga_chunks_db(path)

    # realizo la búsqueda de documentos similares
    docs = db.similarity_search(query, k=k)
    # obtengo el contenido de los documentos
    docs_page_content = " ".join([d.page_content for d in docs])
    # creo el prompt para el modelo
    prompt = PromptTemplate(
        input_variables=["question", "docs"],
        template="""
        You are a helpful assistant that that can answer questions about a company project 
        based on the documents of this project. Also you're talking to the user of the project so don't forget to be polite and 
        don't talk about the documents where you're getting the information.
            
        Answer the following question: {question}
        By searching the following document: {docs}
            
        Only use the factual information from the document to answer the question.
            
        If you feel like you don't have enough information to answer the question, say "lo siento no tengo informacion sobre eso.
        para saber mas por favor pongase en contacto con el equipo de urban data.". Although, because you're an assistant, you should try to answer the common questions
        like 'hello', 'how are you', etc.
            
        Your answers shouldn't be too verbose, should be detailed, fast and always in spanish.
        """,
    )
    # creo la cadena de procesamiento
    chain = LLMChain(llm=llm, prompt=prompt)
    # obtengo la respuesta del modelo
    response = chain.run(question=query, docs=docs_page_content)
    # elimino el salto de línea final
    response = response.replace("\n", "")
    return response

# configurar la interfaz de streamlit

st.title("Asistente virtual :material/smart_toy:")


# inicializar el historial de mensajes si no existe
if "messages" not in st.session_state:
    st.session_state.messages = []

# mostrar el mensaje de bienvenida si es la primera vez
if "first_message" not in st.session_state:
    st.session_state.first_message = True
    st.session_state.messages.append({"role": "assistant", "content": "Hola, ¿cómo puedo ayudarte hoy?"})

# mostrar mensajes anteriores en el chat
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# capturar la entrada del usuario y generar la respuesta
if prompt := st.chat_input("Tu Consulta"):
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # obtener la respuesta completa
    start_time = time.time()
    respuesta_obtenida = get_response(path, prompt)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Tiempo de respuesta: {elapsed_time} segundos")

    # mostrar la respuesta gradualmente, letra por letra
    with st.chat_message("assistant") as response_message:
        response_placeholder = st.empty()
        partial_response = ""
        for i, char in enumerate(respuesta_obtenida):
            partial_response += char
            if i % 10 == 0:  # actualiza cada 10 caracteres
                response_placeholder.markdown(partial_response)
                time.sleep(0.05)  # añade un pequeño retraso para simular la velocidad de escritura
        response_placeholder.markdown(partial_response)  # muestra el mensaje completo al final

    # actualizar el historial de mensajes
    st.session_state.messages.append({"role": "assistant", "content": respuesta_obtenida})
