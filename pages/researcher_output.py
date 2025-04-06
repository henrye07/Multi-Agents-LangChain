import streamlit as st 
from chains import socrates_chain 
from agent_logic import agent_chatbot
# with st.sidebar:
#     llama_api_key = st.text_input("LLAMA API Key", key="chatbot_api_key", type="password")
#     "[Get an Llama API key](https://platform.openai.com/account/api-keys)"
#     "[View the source code](https://github.com/streamlit/llm-examples/blob/main/Chatbot.py)"
#     "[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/streamlit/llm-examples?quickstart=1)"

st.title("💬 Researcher Chatbot")
st.caption("🚀 A Streamlit chatbot powered by Llama")


report = st.session_state["report"].get('agent_contributions', {}).get('researcher', '')
agent_chatbot(report)