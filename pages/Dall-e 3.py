import streamlit as st

st.title("Dall-e 3")

#st.write ("Veuillez entré une description de l'image que vous souhaitez generer")

text_input = st.text_input("Application Web - Open IA")
st.write(text_input)

sidebar_in = st.sidebar.text_input("Veuillez entré la clé Open IA")

#Intéraction avec OpenAI
from openai import OpenAI
client = OpenAI(api_key=sidebar_in)

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
