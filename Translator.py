from googletrans import Translator
import streamlit as st

translator = Translator()

# Set up streamlit app
st.title("Language Translator")
st.write("Enter the text to be translated below: ")


user_input = st.text_input("Text to be translated: ")


# source and target language 
src_lang = st.selectbox("Select source language: ", options = ["pl", "en", "es", "fr", "pt", "es", "de", "it", "uk"])
tgt_lang = st.selectbox("Select target language: ", options = ["en", "pl", "es", "fr", "pt", "es", "de", "it", "uk"])


# translate text
if user_input:
    translated_text = translator.translate(user_input, src = src_lang, dest = tgt_lang )
    st.write("Translated text: ")
    st.write(translated_text.text)

