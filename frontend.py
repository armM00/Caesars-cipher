import streamlit as st
import backend, design

design.design()

st.title("Caesar's cipher")
st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/b/b5/CipherDisk2000.jpg/330px-CipherDisk2000.jpg")

text = st.text_input(label="Enter Text", placeholder="Tango Down")
steps = (st.text_input(label="Enter number of Steps", placeholder="3"))


if text != "" and steps != "":
    try:
        steps = int(steps)
        result = backend.counter(text, steps)
        st.write(result)
    except ValueError:
        st.error("Enter valid credentials")
