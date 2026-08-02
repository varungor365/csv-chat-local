import streamlit as st
import pandas as pd
from pandasai import SmartDataframe
from pandasai.llm import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="CSV Chat Local", page_icon="📊", layout="wide")

st.title("📊 Chat with your CSV (Local Edition)")
st.markdown("Upload a CSV file and ask questions about your data using natural language.")

# Sidebar for API Key
with st.sidebar:
    st.header("Settings")
    api_key = st.text_input("OpenAI API Key", type="password", value=os.getenv("OPENAI_API_KEY", ""))
    if api_key:
        os.environ["OPENAI_API_KEY"] = api_key
    else:
        st.warning("Please enter your OpenAI API key to continue.")

uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file and api_key:
    # Load data
    df = pd.read_csv(uploaded_file)
    
    st.subheader("Data Preview")
    st.dataframe(df.head())
    
    # Initialize PandasAI
    llm = OpenAI(api_token=api_key)
    sdf = SmartDataframe(df, config={"llm": llm})
    
    # Chat interface
    st.subheader("Chat")
    
    if "messages" not in st.session_state:
        st.session_state.messages = []
        
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
            
    if prompt := st.chat_input("Ask a question about your data (e.g. 'What is the average sales by region?')"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
            
        with st.chat_message("assistant"):
            with st.spinner("Analyzing data..."):
                try:
                    response = sdf.chat(prompt)
                    st.markdown(str(response))
                    st.session_state.messages.append({"role": "assistant", "content": str(response)})
                except Exception as e:
                    st.error(f"Error: {str(e)}")
elif uploaded_file and not api_key:
    st.info("Upload complete. Please enter your API key in the sidebar to chat.")
