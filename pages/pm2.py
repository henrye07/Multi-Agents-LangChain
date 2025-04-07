import streamlit as st 
from chains import pm2_chain
from agent_logic import agent_chatbot

st.title("💬 Product Manager (PM2) Chatbot")
st.caption("🚀 A Streamlit chatbot powered by Anthropic")

report = st.session_state["report"].get('main_content', {})
agent_chatbot(report)