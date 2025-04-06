import streamlit as st

st.title("Personal Tech Team")

def add_project():
    return{
        "idea_title": "",
        "objective": "",
        "scope": "",
        "benefits": "",
        "features": "",
        "timeline": "",
        "budget": "",
        "metrics": "",
        "risks": "",
        "integrations": "",
        "stakeholders": "",
        "flexibility": ""
    }

def get_project():
    return st.session_state["project_context"]

@st.fragment
def project_fragment():
    with st.form("my_form"):
        st.header("Project Context")
        if "project_context" not in st.session_state:
            project_context = add_project()
            st.session_state["project_context"] = project_context
        else:
            project_context = get_project()

        idea_title = st.text_input("What is your project idea?",placeholder="Get a sense of the expected deliverables or product capabilities.",key="idea_title", value = project_context["idea_title"])
        objective = st.text_input("What is the primary goal of this project?",placeholder="Understand the main business objective or problem you want to solve.",key="objective", value = project_context["objective"])
        scope = st.text_input("What is the scope of this project?",placeholder="Get a sense of the expected deliverables or product capabilities.",key="scope", value = project_context["scope"])
        benefits = st.text_input("Who is the target audience, and what specific needs or pain points do they have?",placeholder="Clarify who will benefit from the solution and what their key challenges are.",key="benefits", value = project_context["benefits"])
        features = st.text_input("What are the key features or functionalities you envision?",placeholder="Get a sense of the expected deliverables or product capabilities.",key="features", value = project_context["features"])
        timeline = st.text_input("What is your desired timeline for this project?",placeholder="Establish critical milestones and deadlines to align expectations.",key="timeline", value = project_context["timeline"])
        budget = st.text_input("What budget constraints do we need to be aware of?",placeholder="Determine financial limits to shape the scope and priorities.",key="budget", value = project_context["budget"])
        metrics = st.text_input("Identify the metrics or KPIs that will measure the project’s impact.",placeholder="Identify the metrics or KPIs that will measure the project’s impact.",key="metrics", value = project_context["metrics"])
        risks = st.text_input("Gather insights on any hurdles the customer anticipates.",placeholder="Gather insights on any hurdles the customer anticipates.",key="risks", value = project_context["risks"])
        integrations = st.text_input("Identify technical dependencies or legacy system requirements.",placeholder="Identify technical dependencies or legacy system requirements.",key="integrations", value = project_context["integrations"])
        stakeholders = st.text_input("Understand the key decision-makers and their interests.",placeholder="Understand the key decision-makers and their interests.",key="stakeholders", value = project_context["stakeholders"])
        flexibility = st.text_input("Determine whether adjustments can be made if needed during development.",placeholder="Determine whether adjustments can be made if needed during development.",key="flexibility", value = project_context["flexibility"])
        submit_button = st.form_submit_button("Submit")
        if submit_button:
            if all([idea_title, objective, scope, benefits, features, timeline, budget, metrics, risks, integrations, stakeholders, flexibility]):
                with st.spinner("Processing..."):
                    #save the data
                    project_context['idea_title'] = idea_title
                    project_context['objective'] = objective
                    project_context['scope'] = scope
                    project_context['benefits'] = benefits
                    project_context['features'] = features
                    project_context['timeline'] = timeline
                    project_context['budget'] = budget
                    project_context['metrics'] = metrics
                    project_context['risks'] = risks
                    project_context['integrations'] = integrations
                    project_context['stakeholders'] = stakeholders
                    project_context['flexibility'] = flexibility
                    st.success("Project context processed successfully!")
            else:
                st.warning("Please fill in all the fields.")


@st.fragment
def forms():
    project_fragment() 

forms()