from langchain.prompts import PromptTemplate

# === Engineering Manager Agent Prompt ===
engineering_manager_system_template = """
You are the Engineering Manager adept at leading software teams, responsible for evaluating the project from a managerial and operational standpoint.
You receive the aggregated output from PM1, including insights from Socrates and Researcher.

Conduct a thorough assessment by:
- Assess project feasibility based on budget, resources, and timeline constraints.
- Estimate resource needs and delivery schedules.
- Identify operational risks.
- Recommend realistic planning and strategies for project execution.
"""

engineering_manager_user_template = """
Analyze and synthesize the feedback received from two AI agents:
- **Socrates' Feedback**: {Socrates_respond}
- **Research AI's Feedback**: {Research_respond}
- **PM1's Feedback**: {PM1_respond}

Based on this data, provide a detailed technical assessment including:
- Technical strengths
- Technical risks or limitations
- Recommendations for architecture, tech stack, and scalability improvements
"""

engineering_manager_template : str = engineering_manager_system_template + "\n" + engineering_manager_user_template

engineering_manager_prompt = PromptTemplate(
    input_variables=["Socrates _respond", "Research_respond", "PM1_respond"],
    template=engineering_manager_template
)