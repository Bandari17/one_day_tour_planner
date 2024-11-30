import streamlit as st
import requests

st.title("One-Day Tour Planning Assistant")

# User login
username = st.text_input("Enter your username:")
if st.button("Login"):
    st.session_state['username'] = username
    st.success(f"Welcome, {username}!")

# Chat interface
user_input = st.text_input("You: ")
if st.button("Send"):
    # Send user input to backend API
    response = requests.post("http://localhost:8000/preferences/", json={"username": username, "input": user_input})
    st.text_area("Assistant:", value=response.json()["response"], height=200)
