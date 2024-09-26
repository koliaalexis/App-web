import streamlit as st

st.title("Dall-e 3")

#Champ de saisie
text_input = st.text_input("Application Web - Open IA")
st.write(text_input)

#Champ de saisie dans la sidebar
sidebar_input = st.sidebar.text_input("Tapez la clé OpenAI ici :")
st.write(sidebar_input)

#Intéraction avec OpenAI
from openai import OpenAI
client = OpenAI(api_key=sidebar_input)

prompt = "A boat"

image = client.images.generate(
    model="dall-e-2",
    prompt=text_input,
    size="512x512",
    quality="standard",
    n=1,
)
image_url = image.data[0].url

#Affichage de l'image
st.image(image_url)
