import pickle
import streamlit as st
import os
from chatp import chatBotUI
from PIL import Image

pdf_mapping = {
    'LUPIN': 'LUPIN.pdf',
    'MAHINDRA & MAHINDRA': 'M&M_Ltd.pdf',
    'BAJAJFINSERV': 'BAJAJFINSERV.pdf',
    'SBIN': 'SBIN.pdf',
    'INDUSTOWER': 'INDUSTOWER.pdf',
}

st.set_page_config(page_title="StockLoom",layout="wide")

logo= Image.open("./pictures/my-logo.png")
def main():
    st.header("Stock Data")
    with st.sidebar:
        st.image(logo)
        st.markdown('''
            ## About
            Choose the desired Stock, then perform a query.
            ''')

    custom_names = list(pdf_mapping.keys())
    selected_custom_name = st.sidebar.radio('Choose your Stock', [ *custom_names])
    selected_actual_name = pdf_mapping.get(selected_custom_name)

    if selected_actual_name:
        pdf_folder = "D:\MecHackStockLoom\Stockloom\statement_pdf"
        file_path = os.path.join(pdf_folder, selected_actual_name)

        pickle_folder = "Pickle"
        pickle_file_path = os.path.join(pickle_folder, f"{selected_custom_name}.pkl")

        with open(pickle_file_path, "rb") as f:
            vectorstore = pickle.load(f)


    chatBotUI(vectorstore)


main()