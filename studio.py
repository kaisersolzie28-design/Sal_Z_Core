import streamlit as st
import google.generativeai as genai
import os

# 1. Page Configuration
st.set_page_config(page_title="Sal Z Master OS", page_icon="🤖")
st.title("🤖 Sal Z Master OS")

# 2. API Setup
genai.configure(api_key=api_key)
# Try using the model name without 'models/' prefix or just the ID
model = genai.GenerativeModel('gemini-1.5-flash')1.5-flash-latest')

# 3. Initialize Chat History
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Sal Z online. How can I assist with the film production or tour logistics today?"}
    ]

# 4. Display Chat History
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 5. The Chat Engine
if prompt := st.chat_input("Enter command..."):
    # Add user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate AI Response
    with st.chat_message("assistant"):
        response = model.generate_content(prompt)
        st.markdown(response.text)
        st.session_state.messages.append({"role": "assistant", "content": response.text})