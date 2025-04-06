import streamlit as st 
from workflow import process_user_input 
 
@st.cache_resource
def agent_chatbot(response):
    message = [{"role": "assistant", "content": "Evaluating project..."}]
    message.append({"role": "assistant", "content": response})
    for msg in message:
        st.chat_message(msg["role"]).write(msg["content"])
    message

@st.cache_resource
def agent_response(_agent_chain,project_context):
    response = _agent_chain.invoke(project_context)
    return response

def isproject_valid(response):
    if len(response) < 200:
        if "I don't know" in response:
            st.warning("This project is not related to programming or software development. Please refresh the page and try again.")
            st.cache_data.clear()
            return False
        else:
            return True
    else:
        return True 

@st.cache_resource
def agents_workflow(pm1_evaluation:str):
    report = process_user_input(user_input = pm1_evaluation)
    st.session_state["report"] = report
    return report