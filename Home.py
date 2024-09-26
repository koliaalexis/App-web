import streamlit as st

# Title
st.title("Mon formulaire")

# Texte
st.write ("Ceci est un formulaire de contact")

# Champ de saisi 
user_input = st.text_input ("Tapez votre texte : ")

st.write(user_input)

# Image 
st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQWaPkuu9hTOXlu4U2yrDFAhiuzBIbo3B2B3g&s")

# Sidebare
st.sidebar.title("Alexis Thomas")

# Vidéo dans la sidebar
st.sidebar.video("https://www.youtube.com/watch?v=0iU3yCYue_U")

# Select bar 
student_grad = st.selectbox("Selectionnez votre niveau d'étude", ["Bac", "Bac+2", "Bac+3"])

#Selecct slider
age = st.select_slider("Quel est votre age", range(0,99))

# Condition en python 
if age > 18:
  st.write("Vous êtes majeur")
else:
    st.write("Vous êtes mineur")



