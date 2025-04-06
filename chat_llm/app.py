from context.pms import pm3_memory, pm3_chat_prompt
from langchain.chains import LLMChain
from models import chat_llm


# Dummy functions to simulate real tools (these should be connected to real logic in your app)
def get_context():
    return "Project: AI-driven Freelancer Assistant | Objective: Help freelancers manage projects efficiently."

def call_mentor(change_request=None):
    return f"Mentor evaluated the request: '{change_request}' and responded with adjusted architecture and timeline."

def call_cache():
    return {
        "socrates_output": "Key philosophical questions: ...",
        "research_output": "Similar tools: Trello, Asana AI features..."
    }

def update_report(update_note):
    return f"Report updated with the following note: {update_note}"

def budget_estimator(change):
    return f"New budget estimated based on '{change}': $8,000 over 3 months."

# Define tools
tools = [
    Tool(
        name="GetContext",
        func=lambda _: get_context(),
        description="Use to get the original project context from the user."
    ),
    Tool(
        name="CallMentor",
        func=lambda query: call_mentor(query),
        description="Ask the Mentor (Tech Lead or Engineering Manager) for insights or technical re-evaluation."
    ),
    Tool(
        name="GetCache",
        func=lambda _: call_cache(),
        description="Retrieve saved insights from Socrates and Researcher."
    ),
    Tool(
        name="UpdateReport",
        func=lambda update: update_report(update),
        description="Update the final project report with new insights or decisions."
    ),
    Tool(
        name="EstimateBudget",
        func=lambda change: budget_estimator(change),
        description="Estimate the impact of a change on the project's budget and timeline."
    )
]

# Memory for conversation tracking
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

# === Chain Setup ===

pm3_chain = LLMChain(
    llm=chat_llm,
    prompt=pm3_chat_prompt,
    memory=pm3_memory,
    verbose=True  # Optional for debugging
)

# === Using the Chain ===

response = pm3_chain.run({
    "tech_eval": "The proposed microservice architecture is scalable and robust...",
    "managerial_eval": "Estimated timeline is 6 months with a $200k budget...",
    "user_message": "Can you reduce the timeline to 4 months without major tradeoffs?"
})