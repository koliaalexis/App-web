import stramlit as st

st.title("ChatGPT - Rédacteur Web")

user_input = st.text_input("Choisissez une thématique")

openai_key = st.sidebar.text_input("Tapez une clé OpenAI")

