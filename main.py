import os
import streamlit as st
from langchain.llms import OpenAI
from dotenv import dotenv_values
env_vars = dotenv_values(".env")
api_key = env_vars.get("openai_key")# Set your OpenAI API key
os.environ["OPENAI_API_KEY"] =openai_key

# Initialize the language model
llm = OpenAI(temperature=0.8)

# Streamlit framework
st.image('color.png', width=200)
st.title('Chatbot')

# Initialize conversation history
conversation_history = []

# Function to display chat bubble
def chat_bubble(sender, message):
    if sender == "You":
        st.text_area("", value=message, height=50, key=message, disabled=True)
    else:
        st.text_area("", value=message, height=500, key=message, disabled=True)

# Function to display entire conversation history
def display_conversation_history():
    if conversation_history:
        st.markdown("## Conversation History")
        for sender, message in conversation_history:
            chat_bubble(sender, message)

# Main chatbox interface
input_text = st.text_area("Type a message...", height=100)
if st.button("Send"):
    if input_text:
        # Add user message to conversation history
        conversation_history.append(("You", input_text))
        # Generate response from language model
        response = llm(input_text)
        # Add bot response to conversation history
        conversation_history.append(("Bot", response))
        # Display entire conversation history
        display_conversation_history()



