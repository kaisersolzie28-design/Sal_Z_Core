import streamlit as st
import google.generativeai as genai
import os

# --- 1. CONFIGURATION ---
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
model = genai.GenerativeModel('gemini-1.5-flash')

st.set_page_config(page_title="Sal Z Master OS", layout="wide")
st.title('🤖 Sal Z | Master Operating System')

# --- 2. SKILL MODULES (CLOUD COMPATIBLE) ---
def execute_spange_search(query):
    # Search locally within the deployed folder
    data_path = "Project_Data" 
    if not os.path.exists(data_path):
        return "Archival data folder not found."
    
    results = []
    for filename in os.listdir(data_path):
        with open(os.path.join(data_path, filename), 'r') as f:
            content = f.read()
            if query.lower() in content.lower():
                results.append(f"Found in {filename}: {content[:200]}...")
    
    return "\n".join(results) if results else "No records found."

# --- 3. CORE INTERFACE ---
if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# --- 4. EXECUTION LOOP ---
if prompt := st.chat_input("Master Command:"):
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # AI Logic
    if "spange" in prompt.lower() or "ledger" in prompt.lower():
        response = execute_spange_search(prompt)
    else:
        response = model.generate_content(prompt).text

    with st.chat_message("assistant"):
        st.markdown(response)
    
    st.session_state.messages.append({"role": "assistant", "content": response})
