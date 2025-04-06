import streamlit as st
from agent_logic import isproject_valid, agents_workflow, agent_response 
from chains import pm1_chain


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

        if "report" not in st.session_state:
            report_init= {
                "main_content": "",
                "tech_validation": "",
                "managerial_validation": "",
                "agent_contributions": {
                    "socrates": "",
                    "researcher": "",
                    "pm1": ""
                }
            }
            st.session_state["report"] = report_init
        
        if "evaluate_project" not in st.session_state:
            evaluate_project = False
            st.session_state["evaluate_project"] = evaluate_project 

        if "project_context" not in st.session_state:
            project_context = add_project()
            st.session_state["project_context"] = project_context
        else:
            project_context = get_project()

        if "disabled" not in st.session_state:
            st.session_state.disabled = False   

        idea_title = st.text_input("What is your project idea?",
            placeholder="Get a sense of the expected deliverables or product capabilities.",
            key="idea_title", 
            value = project_context["idea_title"],
            disabled= st.session_state.disabled,
        )
        objective = st.text_input("What is the primary goal of this project?",
            placeholder="Understand the main business objective or problem you want to solve.",
            key="objective", 
            value = project_context["objective"],
            disabled=st.session_state.disabled,
        )
        scope = st.text_input("What is the scope of this project?",
            placeholder="Get a sense of the expected deliverables or product capabilities.",
            key="scope", 
            value = project_context["scope"],
            disabled=st.session_state.disabled,
        )
        benefits = st.text_input("Who is the target audience, and what specific needs or pain points do they have?",
            placeholder="Clarify who will benefit from the solution and what their key challenges are.",
            key="benefits", 
            value = project_context["benefits"],
            disabled=st.session_state.disabled,
        )
        features = st.text_input("What are the key features or functionalities you envision?",
            placeholder="Get a sense of the expected deliverables or product capabilities.",
            key="features", 
            value = project_context["features"],
            disabled=st.session_state.disabled,
        )
        timeline = st.text_input("What is your desired timeline for this project?",
            placeholder="Establish critical milestones and deadlines to align expectations.",
            key="timeline", 
            value = project_context["timeline"],
            disabled=st.session_state.disabled,
        )
        budget = st.text_input("What budget constraints do we need to be aware of?",
            placeholder="Determine financial limits to shape the scope and priorities.",
            key="budget", 
            value = project_context["budget"],
            disabled=st.session_state.disabled,
        )
        metrics = st.text_input("How do you define success for this project?",
            placeholder="Identify the metrics or KPIs that will measure the project’s impact.",
            key="metrics", 
            value = project_context["metrics"],
            disabled=st.session_state.disabled,
        )
        risks = st.text_input("What are the known risks or potential challenges?",
            placeholder="Gather insights on any hurdles the customer anticipates.",
            key="risks", 
            value = project_context["risks"],
            disabled=st.session_state.disabled,
        )
        integrations = st.text_input("What are the existing systems or integrations that the solution must work with?",
            placeholder="Identify technical dependencies or legacy system requirements.",
            key="integrations", 
            value = project_context["integrations"],
            disabled=st.session_state.disabled,
        )
        stakeholders = st.text_input("Who are the main stakeholders, and what are their roles or expectations?",
            placeholder="Understand the key decision-makers and their interests.",
            key="stakeholders", 
            value = project_context["stakeholders"],
            disabled=st.session_state.disabled,
        )
        flexibility = st.text_input("How flexible is the project scope? Determine whether adjustments can be made if needed during development.",
            placeholder="Determine whether adjustments can be made if needed during development.",
            key="flexibility",  
            value = project_context["flexibility"],
            disabled=st.session_state.disabled,
        )
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
                    st.session_state.disabled = True
                    my_bar = st.progress(0, text="Operation in progress (PM1). Please wait.")
                    pm1_response = agent_response(_agent_chain=pm1_chain, project_context=project_context)
                    my_bar.progress(100, text="Operation completed (PM1).")
                    validate_project = isproject_valid(pm1_response)
                    if validate_project:
                        if "pm1_respond" not in st.session_state:
                            st.session_state["pm1_respond"] = pm1_response
                        report = agents_workflow(pm1_response)
                        st.session_state["report"] = report
                        st.success("Project context processed successfully!")
                    st.rerun()  
                    
            else:
                st.warning("Please fill in all the fields.")


def forms():
    project_fragment() 

forms()