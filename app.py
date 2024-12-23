import streamlit as st
from helper import generate_chat_completion

st.title("AI Stand-Up Comedian 😂") 

with st.form("user_form", clear_on_submit=True):
    user_input = st.text_input("Type something")
    submit_button = st.form_submit_button(label="Send")

if submit_button:
    with st.spinner("Wait for it..."):
        completion = generate_chat_completion(user_input)
        st.write(completion)