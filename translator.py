import streamlit as st
from googletrans import Translator, LANGUAGES

# Initialize the translator
translator = Translator()

# App Title
st.title("🌐 Universal Language Translator")
st.markdown("Enter text below and select a language to translate.")

# Create UI Elements
# Text input area
text_input = st.text_area("Input:", placeholder="Type something...", height=150)

# Language selection dropdown
# We map the language names to their codes
lang_options = {name.capitalize(): code for code, name in LANGUAGES.items()}
target_lang_name = st.selectbox("Translate to:", options=list(lang_options.keys()), index=list(lang_options.keys()).index("Spanish"))
target_lang_code = lang_options[target_lang_name]

# Translate button
if st.button("Translate", type="primary"):
    if text_input.strip() == "":
        st.warning("Please enter some text to translate.")
    else:
        try:
            # Perform translation
            res = translator.translate(text_input, dest=target_lang_code)
            
            # Display Results
            st.divider()
            st.subheader("Result:")
            st.write(f"**Original ({res.src}):** {res.origin}")
            st.success(f"**Translated:** {res.text}")
        except Exception as e:
            st.error(f"An error occurred: {e}")
