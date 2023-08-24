import streamlit as st
from PIL import Image

st.title('La aplicación más chimba')

st.header("En este espacio comienzo a desarrollar mis aplicaciones para interfaces multimodales.")
st.write("Fácilmente puedo realizar backend y frontend")
image = Image.open('gatito_mojado.jpg')

st.image(image, caption="Aquí va un gato mojado")

texto = st.text_input('escribe algo', 'este es mi texto')
st.write('El text escrito es', texto)
