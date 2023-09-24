import pickle
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain
import streamlit as st
import os
from transu import translate_to_malayalam

os.environ["OPENAI_API_KEY"] = "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"


def chatBotUI(vectorstore):
    llm = ChatOpenAI(temperature=0.0, max_tokens=1000, model_name="gpt-3.5-turbo")
    messages = []
    qa = ConversationalRetrievalChain.from_llm(llm, vectorstore.as_retriever())
    prompty = f"""
               Analyze the whole document and give me an idea of the company,how it is performing,who should invest and make sure you dont use any technical terms.your answer
               should be like you are talking to a common man. Do not print based on the information provided answer it by saying according to 
               stockloom's analysis. Note : Do not say what all data are provided in the documents, instead use the data values to give a reported answer
            """
    summary = qa({"question": prompty, "chat_history": [(message["role"], message["content"]) for message in
                                                      messages]})
    col1, col2 = st.columns([0.5,0.5])
    with col1:
        st.write(summary["answer"])
    with col2:
        st.write(translate_to_malayalam(summary["answer"]))



    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])


    if prompt := st.chat_input("Ask your questions"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        result = qa({"question": prompt, "chat_history": [(message["role"], message["content"]) for message in
                                                              st.session_state.messages]})


        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            message_placeholder2 = st.empty()
            full_response = result["answer"]
            message_placeholder.markdown(full_response + "|")
        message_placeholder.markdown(full_response)
        message_placeholder2.markdown(translate_to_malayalam(full_response))
        print(full_response)
        st.session_state.messages.append({"role": "assistant", "content": full_response})

