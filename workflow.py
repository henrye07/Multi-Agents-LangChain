
from chains import socrates_chain, researcher_chain, tech_lead_chain, engineering_manager_chain, pm2_chain

# Main orchestration function
def process_user_input(user_input: str, iterations: int = 1):
    # Initial parallel processing with Socrates and Researcher
    socrates_output = socrates_chain.invoke(user_input)
    researcher_output = researcher_chain.invoke(user_input)

    # Initial lead guidance
    tech_input = {
        "Socrates_respond": socrates_output,
        "Research_respond": researcher_output,
        "PM1_respond": user_input
    }
    tech_output = tech_lead_chain.invoke(tech_input)
    managerial_input = {
        "Socrates_respond": socrates_output,
        "Research_respond": researcher_output,
        "PM1_respond": user_input
    }
    managerial_output = engineering_manager_chain.invoke(managerial_input)
    # PM2 processes both outputs
    pm2_input = {
        "tech_eval": tech_output,
        "managerial_eval": managerial_output,
        "PM1_respond": user_input
    }
    pm2_output = pm2_chain.invoke(pm2_input)

    # Compile final output
    final_output = {
        "main_content": pm2_output,
        "tech_validation": tech_output,
        "managerial_validation": managerial_output,
        "agent_contributions": {
            "socrates": socrates_output,
            "researcher": researcher_output,
            "pm1": user_input,
        }
    }

    return final_output