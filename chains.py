from langchain_core.runnables import RunnablePassthrough, RunnableLambda
from langchain_core.output_parsers import StrOutputParser
from typing import Dict, Any
from context.pms import pm1_prompt, pm2_prompt
from context.tech_lead import tech_lead_prompt
from context.eng_m import engineering_manager_prompt
from context.socrates import socrates_prompt
from context.researcher import researcher_prompt
from models import llama_socrates, llama_researcher, claude_model

# Function to combine outputs for PM1
def combine_for_pm1(inputs: Dict[str, Any]) -> Dict[str, Any]:
    return {
        "idea_title"  : inputs["idea_title"], 
        "objective" : inputs["objective"], 
        "scope" : inputs["scope"], 
        "benefits" : inputs["benefits"], 
        "features" : inputs["features"], 
        "timeline" : inputs["timeline"], 
        "budget" : inputs["budget"], 
        "metrics" : inputs["metrics"], 
        "risks" : inputs["risks"], 
        "integrations" : inputs["integrations"], 
        "stakeholders" : inputs["stakeholders"], 
        "flexibility" : inputs["flexibility"]
    }

pm1_chain = (
    RunnableLambda(combine_for_pm1)
    | pm1_prompt
    | claude_model
    | StrOutputParser()
)

socrates_chain = (
    {"key_topics": RunnablePassthrough()}
    | socrates_prompt
    | llama_socrates
    | StrOutputParser()
)

researcher_chain = (
    {"key_topics": RunnablePassthrough()}
    | researcher_prompt
    | llama_researcher
    | StrOutputParser()
)

# Function to combine outputs for Tech Lead and Engineering Manager
def combine_for_leads(inputs: Dict[str, Any]) -> Dict[str, Any]:
    return {
        "Socrates_respond": inputs["Socrates_respond"],
        "Research_respond": inputs["Research_respond"],
        "PM1_respond": inputs["PM1_respond"]
    }

tech_lead_chain = (
    RunnableLambda(combine_for_leads)
    | tech_lead_prompt
    | claude_model
    | StrOutputParser()
)

engineering_manager_chain = (
    RunnableLambda(combine_for_leads)
    | engineering_manager_prompt
    | claude_model
    | StrOutputParser()
)

# Function to combine outputs for PM2
def combine_for_pm2(inputs: Dict[str, Any]) -> Dict[str, Any]:
    return {
        "tech_eval": inputs["tech_eval"],
        "managerial_eval": inputs["managerial_eval"],
        "PM1_respond": inputs["PM1_respond"]
    }

pm2_chain = (
    RunnableLambda(combine_for_pm2)
    | pm2_prompt
    | claude_model
    | StrOutputParser()
)