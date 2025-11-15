import streamlit as st
from openai import OpenAI
import os

# Configurar API Key
os.environ["OPENAI_API_KEY"] = "sk-svcacct-mnm5nN3MBpUcU_R0iZtxkTu5qFkYV_XNOSuuveU2YbnxczYPRL_PbpISa3JopT3BlbkFJ4QsqPBfiyrIUf5Gv5qj_1_uURCTlHM2HY9FpvXIc-ao4dGN0Tmz1wO0gozjAA"

# Inicializar cliente OpenAI
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Configurar página
st.set_page_config(
    page_title="ChatGPTGRUPO1",
    page_icon="🤖",
    layout="wide"
)

# CSS para estilo ChatGPT
st.markdown("""
<style>
    .main {
        background-color: #343541;
    }
    .stChatMessage {
        padding: 20px 0;
    }
    .stChatMessage:first-child {
        border-top: 1px solid #4a4b52;
    }
    .stChatMessage {
        border-bottom: 1px solid #4a4b52;
    }
    [data-testid="stChatMessage"] {
        padding: 24px 0;
    }
    [data-testid="stChatMessage"]:nth-child(odd) {
        background-color: #343541;
    }
    [data-testid="stChatMessage"]:nth-child(even) {
        background-color: #444654;
    }
    .stTextInput textarea {
        background-color: #40414f !important;
        color: white !important;
        border: 1px solid #565869 !important;
        border-radius: 12px !important;
    }
    .stTextInput textarea:focus {
        border-color: #19c37d !important;
        box-shadow: none !important;
    }
</style>
""", unsafe_allow_html=True)

# Inicializar historial del chat
if "messages" not in st.session_state:
    st.session_state.messages = []

# Header estilo ChatGPT
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.markdown("<h1 style='text-align: center; color: white; margin-bottom: 30px;'>ChatGrupo01GPT</h1>", unsafe_allow_html=True)

# Mostrar mensajes del historial
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input del usuario
if prompt := st.chat_input("Envía un mensaje..."):
    # Agregar mensaje del usuario
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generar respuesta con OpenAI (nueva API)
    with st.chat_message("assistant"):
        with st.spinner("Pensando..."):
            try:
                response = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "Eres un asistente útil y amigable. Responde en español."}
                    ] + [{"role": m["role"], "content": m["content"]} for m in st.session_state.messages],
                    max_tokens=500,
                    temperature=0.7
                )
                respuesta = response.choices[0].message.content
                st.markdown(respuesta)
                st.session_state.messages.append({"role": "assistant", "content": respuesta})
            except Exception as e:
                error_msg = f"Error: {str(e)}"
                st.error(error_msg)
                st.session_state.messages.append({"role": "assistant", "content": error_msg})

# Botón para limpiar el chat
col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    if st.button("🧹 Limpiar Chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()