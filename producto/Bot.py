import streamlit as st

st.title("Asistente virtual 🐱‍💻")

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

# if prompt := st.chat_input("Tu consulta"):
#     with st.chat_message("user"):
#         st.markdown(prompt) # consulta del usuario
#     st.session_state.messages.append({"role":"user", "content":prompt}) #agregar al historial


#     # inst = llama(prompt)
#     # resp = llama()

#     with st.chat_message("assistant"):
#         st.markdown(resp) #respuesta del bot
#     st.session_state.messages.append({"role":"assistant", "content":prompt}) #agregar al historial
