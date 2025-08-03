
import streamlit as st
import urllib.parse

st.set_page_config(page_title="Enviar mensaje a WhatsApp", layout="centered")

st.title("💬 Enviar mensaje a WhatsApp")

# Formulario
nombre = st.text_input("Tu nombre")
mensaje = st.text_area("Escribe tu mensaje")

# Número fijo (oculto)
numero = "+56967010107"

if st.button("📲 Enviar a WhatsApp"):
    if nombre and mensaje:
        mensaje_final = f"Hola, soy {nombre}. {mensaje}"
        mensaje_codificado = urllib.parse.quote(mensaje_final)
        link = f"https://wa.me/{numero.replace('+', '')}?text={mensaje_codificado}"
        st.success("Redireccionando a WhatsApp...")
        st.markdown(f"[👉 Haz clic aquí para continuar a WhatsApp]({link})", unsafe_allow_html=True)
    else:
        st.warning("Completa todos los campos antes de enviar.")
