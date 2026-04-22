import streamlit as st
from app.chat_service import out_put

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

user_input = st.chat_input("Enter your question")

if user_input:
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("user"):
        st.markdown(user_input)

    llm_output = out_put(user_input=user_input)

    with st.chat_message("ai"):
        st.markdown(llm_output)

    st.session_state.messages.append({
        "role": "ai",
        "content": llm_output
    })