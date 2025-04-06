from dotenv import load_dotenv
from langchain_community.llms import Together
from langchain_anthropic import ChatAnthropic
from langchain_groq import ChatGroq

# Load environment variables
load_dotenv()

# Initialize models
llama_socrates = Together(
    model="meta-llama/Meta-Llama-3-70B-Instruct-Turbo",
    temperature=0.3,
    max_tokens=500,
    verbose=True
)

llama_researcher = Together(
    model="meta-llama/Meta-Llama-3-70B-Instruct-Turbo",
    temperature=0.3,
    max_tokens=500,
    verbose=True
)

claude_model = ChatAnthropic(
    model="claude-3-5-sonnet-20240620",
    temperature=0.3,
    max_tokens=1000,
    verbose=True
)

gpt4o_mini = ChatGroq(
    model="gpt-4o-mini",
    temperature=0.3,
    max_tokens=1000,
    verbose=True
)