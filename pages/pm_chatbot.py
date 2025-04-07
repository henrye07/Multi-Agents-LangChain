import streamlit as st
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.output_parsers import StrOutputParser
from langchain.prompts import ChatPromptTemplate
from models import claude_model_chat

st.title("💬 Product Manager - Chatbot")
st.caption("🚀 A Streamlit chatbot powered by Anthropic")

# Define the Anthropic model (Claude)
llm = claude_model_chat

# Define system message to guide Claude's role
system_message = SystemMessage(content="""
You are PM3, the final decision-maker and project strategist AI agent.
Your role is to integrate all prior insights, user feedback, and team evaluations to make budget, scope, and planning decisions.
Communicate clearly and concisely, and ask follow-up questions if necessary.
You are not connected to tools, but base your reasoning on your internal knowledge and memory of previous discussions.
""")
report = st.session_state["report"].get('main_content', '')
template = ChatPromptTemplate([
    system_message,
    ("ai", report),
    ("human", "{input}")
])

# Generate response
pm_chain =  template | llm | StrOutputParser()

# === Using the Chain ===

if "chatmessages" not in st.session_state:
    st.session_state["chatmessages"] = [{"role": "assistant", "content": "What do you think about the approach in 'Product Manager - Final Decision'?"}]

for msg in st.session_state.chatmessages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    st.session_state.chatmessages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    response = pm_chain.invoke({"input": prompt})
    st.session_state.chatmessages.append({"role": "assistant", "content": response})
    st.chat_message("assistant").write(response)
