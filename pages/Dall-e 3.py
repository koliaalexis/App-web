import streamlit as st

st.title("Dall-e 3")

st.write ("Veuillez entré une description de l'image que vous souhaitez generer")

dalle_input = st.text_input ("Tapez votre texte : ")
st.write(dalle_input)
