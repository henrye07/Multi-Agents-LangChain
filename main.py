import streamlit as st 


pages = {
    "Setting Parameters": [
        st.Page("pages/setting_params.py", title="Setting Parameters"),
    ],
    "Workflow 1": [
        st.Page("pages/pm1.py", title="Product Manager (PM1)"),
        st.Page("pages/socrates_output.py", title="Socrates Output"),
        st.Page("pages/researcher_output.py", title="Researcher Output"),
        st.Page("pages/tech_lead_output.py", title="Tech Lead Output"),
        st.Page("pages/eng_manager_output.py", title="Engineering Manager Output"),
        st.Page("pages/pm2.py", title="Product Manager - Final Decision"),
        st.Page("pages/pm_chatbot.py", title="Product Manager Chatbot"),
    ]
}


if __name__ == "__main__":
    st.set_page_config(page_title="Personal Tech Team", page_icon=":robot_face:")
    
    pg = st.navigation(pages)
    pg.run()
    
