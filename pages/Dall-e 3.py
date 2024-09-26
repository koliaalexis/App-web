import streamlit as st

st.title("Dall-e 3")

#Champ de saisie
test_input = st.text_input("Open IA")
st.write(test_input)

#La clé OpenAI
search_input = st.sidebar.text_input("La clé OpenAI")
st.write(search_input)

#Intéraction avec OpenAI
from openai import OpenAI
clients = OpenAI(api_key=search_input)

prompt = "A cute baby sea otter"

image = clients.images.generate(
    model="dall-e-2",
    prompt=test_input,
    size="512x512",
    quality="standard",
    n=1,
)
image_url = image.data[0].url
