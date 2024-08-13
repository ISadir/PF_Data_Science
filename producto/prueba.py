from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM
path = 'assets/FAQ2.txt'
with open(path, 'r') as file:
    file_content = file.read()

template = """Question: {question}

Answer: {content}."""

prompt = ChatPromptTemplate.from_template(template)

model = OllamaLLM(model="llama3.1:latest")

chain = prompt | model

print(chain.invoke({"question": "Cual es el objetivo general del proyecto?", "content": file_content}))


# Cargar y dividir el archivo de texto
'''def load_and_split_text(file_path):
    loader = TextLoader(file_path)
    documents = loader.load()
    
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    chunks = text_splitter.split_documents(documents)
    return chunks

text_data = load_and_split_text(path)

# Configurar el sistema de recuperación
retriever = RetrievalQA.from_documents(
    documents=text_data,
    llm=llm
)

def get_best_response(prompt):
    response = retriever(prompt)
    return response['result']'''