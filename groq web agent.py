import os
from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.duckduckgo import DuckDuckGoTools

# Display the model options to the user
print("Select a model:")
print("1. llama-3.3-70b-versatile")
print("2. deepseek-r1-distill-llama-70b")

# Get the user's choice for the model
model_choice = input("Enter the number of the model you want to use (1 or 2): ")

# Set the Groq API key via environment variable (replace with your actual API key)
os.environ["GROQ_API_KEY"] = "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"  # Replace with your actual API key

# Select the model based on the user's input
if model_choice == '1':
    model_id = 'llama-3.3-70b-versatile'
elif model_choice == '2':
    model_id = 'deepseek-r1-distill-llama-70b'
else:
    print("Invalid selection, defaulting to llama-3.3-70b-versatile.")
    model_id = 'llama-3.3-70b-versatile'  # Default model if input is invalid

# Get the user input for the prompt
prompt = input('Enter a prompt: ')

# Initialize the agent with the selected model and DuckDuckGoTools
agent = Agent(
    model=Groq(id=model_id),  # Set the model based on the user's choice
    description="You are an enthusiastic news reporter with a flair for storytelling!",
    tools=[DuckDuckGoTools()],  # Add DuckDuckGo tool to search the web
    show_tool_calls=True,       # Shows tool calls in the response, set to False to hide
    markdown=True               # Format responses in markdown
)

# Prompt the agent to fetch a response based on the selected model
agent.print_response(prompt, stream=True)
