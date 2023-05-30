import streamlit as st


def design():
    icon = 'https://i.ibb.co/Dkv728b/Encryption-PNG-File.png'

    st.set_page_config(page_title="101",
                       page_icon=icon)
    page_bg_img = f"""
    <style>
    [data-testid="stAppViewContainer"] > .main {{
    background-image: url("https://i.ibb.co/C2zXThM/4062621.png");
    background-size: 130%;
    }}
    </style>
    """
    st.markdown(page_bg_img, unsafe_allow_html=True)
