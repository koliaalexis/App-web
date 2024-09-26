import streamlit as st

# Title
st.title("Mon formulaire")

# Texte
st.write ("Ceci est un formulaire de contact")

# Champ de saisi 
user_input = st.text_input ("Tapez votre texte : ")

st.write(user_input)

# Image 
st.image("https://images.app.goo.gl/s8F241UyNzTfDBNh6")

# Sidebare
st.sidebar.title("Alexis Thomas")
