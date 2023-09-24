# import os
# import pickle
#
# pickle_folder = "Pickle"
# selected_custom_name = "stock"
# vectorstore = ['1','2','3','4']
# if not os.path.exists(pickle_folder):
#     os.mkdir(pickle_folder)
#
# pickle_file_path = os.path.join(pickle_folder, f"{selected_custom_name}.pkl")
#
# if not os.path.exists(pickle_file_path):
#     with open(pickle_file_path, "wb") as f:
#         pickle.dump(vectorstore, f)
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# # Load the Langchain chatbot
#         llm = ChatOpenAI(temperature=0, max_tokens=1000, model_name="gpt-3.5-turbo")
#         qa = ConversationalRetrievalChain.from_llm(llm, vectorstore.as_retriever())
#
#         # Initialize Streamlit chat UI
#         if "messages" not in st.session_state:
#             st.session_state.messages = []
#
#         for message in st.session_state.messages:
#             with st.chat_message(message["role"]):
#                 st.markdown(message["content"])
#
#         if prompt := st.chat_input("Ask your questions from PDF "f'{selected_custom_name}'"?"):
#             st.session_state.messages.append({"role": "user", "content": prompt})
#             with st.chat_message("user"):
#                 st.markdown(prompt)
#
#             result = qa({"question": prompt, "chat_history": [(message["role"], message["content"]) for message in st.session_state.messages]})
#             print(prompt)
#
#             with st.chat_message("assistant"):
#                 message_placeholder = st.empty()
#                 full_response = result["answer"]
#                 message_placeholder.markdown(full_response + "|")
#             message_placeholder.markdown(full_response)
#             print(full_response)
#             st.session_state.messages.append({"role": "assistant", "content": full_response})
#
#
#
