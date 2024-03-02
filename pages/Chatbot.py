import streamlit as st
import pandas as pd
import subprocess
import platform
import random
import time

#=============================================================================
# HELPER FUNCTIONS
#=============================================================================
def getResponseFromModel(question):
    response = random.choice(
        [
            "Hello there! How can I assist you today?",
            "Hi, human! Is there anything I can help you with?",
            "Do you need help?",
        ]
    )
    for word in response.split():
        yield word + " "
        time.sleep(0.1)

#=============================================================================
# Chatbot Section
#=============================================================================

st.subheader("Chatbot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("How can I help you?"):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    response = f"Piazza AI: {prompt}"
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        response = st.write_stream(getResponseFromModel("Asdf"))
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})