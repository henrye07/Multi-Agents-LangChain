from langchain.prompts import PromptTemplate
""" Questions to User

1. **What is the primary goal of this project?**
    *Understand the main business objective or problem you want to solve.*
    
2. **Who is the target audience, and what specific needs or pain points do they have?**
    *Clarify who will benefit from the solution and what their key challenges are.*
    
3. **What are the key features or functionalities you envision?**
    *Get a sense of the expected deliverables or product capabilities.*
    
4. **What is your desired timeline for this project?**
    *Establish critical milestones and deadlines to align expectations.*
    
5. **What budget constraints do we need to be aware of?**
    *Determine financial limits to shape the scope and priorities.*
    
6. **How do you define success for this project?**
    *Identify the metrics or KPIs that will measure the project’s impact.*
    
7. **What are the known risks or potential challenges?**
    *Gather insights on any hurdles the customer anticipates.*
    
8. **Are there any existing systems or integrations that the solution must work with?**
    *Identify technical dependencies or legacy system requirements.*
    
9. **Who are the main stakeholders, and what are their roles or expectations?**
    *Understand the key decision-makers and their interests.*
    
10. **How flexible is the project scope?**
    *Determine whether adjustments can be made if needed during development.*

"""

pm1_system_template : str = """
You are a Product Manager (PM1), the Project Information Aggregator skilled in overseeing software development projects. Your responsibility is to process the constant project context provided by the user and extract the core information into a structured, actionable format for further analysis by specialized agents (Socrates and Researcher).If you receive any inquiries or responses that are not related to these domains (Programming), simply reply: I don't know.

Your tasks include:
- Receiving the project context (including idea title, objective, scope, etc.).
- Extracting and highlighting key topics and themes.
- Organizing the information into a comprehensive brief that includes both reflective insights and preliminary market details.

Generate a structured summary based on the project context below.
"""

pm1_user_template : str = """
Project Context:
- Idea Title: {idea_title}
- Objective: {objective}
- Scope: {scope}
- Benefits: {benefits}
- Features: {features}
- Timeline: {timeline}
- Budget: {budget}
- Metrics: {metrics}
- Risks: {risks}
- Integrations: {integrations}
- Stakeholders: {stakeholders}
- Flexibility: {flexibility}

Extract the key topics and themes from this context and present a clear, organized brief for further evaluation.
"""

pm1_template : str = pm1_system_template + "\n" + pm1_user_template

pm1_prompt : PromptTemplate = PromptTemplate(
    input_variables=["idea_title", "objective", "scope", "benefits", "features", "timeline", "budget", "metrics", "risks", "integrations", "stakeholders", "flexibility"], 
    template=pm1_template
)

# Define pm2 system-level instruction
pm2_system_template : str = """
You are PM2, the Final Project Decision Maker, renowned for critical inquiry and skilled in overseeing software development projects.
You integrate technical and managerial evaluations to synthesizing all insights, recommendations, and analyses into a comprehensive final the final PDM (Project Decision Making) report for the design team, project manager and developers..
You have received the Tech Lead final response, Engineering Manager response and PM1 project context which includes **expert recommendations and guidance** for the project.

You will:
- Read the outputs from the Tech Lead, Engineering Manager and PM1.
- Balance insights and synthesize a project summary, technical evaluation, and execution plan.
- Engage in live conversation with the user to address feedback.
- If needed, iterate with the Engineering Manager (and Tech Lead) to refine the plan.

Your final report must be clear, actionable, and holistic.
"""

# Define human message (user interaction prompt)
pm2_human_template : str = """
- Technical Evaluation (from Tech Lead): {tech_eval}
- Managerial Overview (from Engineering Manager): {managerial_eval}
- Project Context (from PM1): {project_context}

Based on these, respond with:
1. Project Summary
2. Final Technical Evaluation
3. Operational Plan (timeline, budget, risks)
4. Clarification or next steps (if feedback is present)
"""

# Define prompt template
pm2_prompt : PromptTemplate = PromptTemplate(
    input_variables=["tech_eval", "managerial_eval", "project_context"],
    template=pm2_human_template
)