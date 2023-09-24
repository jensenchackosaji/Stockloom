import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image

st.set_page_config(page_title="StockLoom", layout="wide")
logo = Image.open("./pictures/my-logo.png")

with st.sidebar:
    selected= option_menu(menu_title="Watch List",options=["Realiance","Tata Consulting Servises","HDFC Bank","Tata Chemicals"],default_index=0)

if selected == "Realiance":
    st.title(f"You have select ")


