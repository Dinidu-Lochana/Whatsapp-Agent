# agent_gemini.py
import os
from dotenv import load_dotenv
import nest_asyncio
from langchain_google_genai import ChatGoogleGenerativeAI
from crewai import Agent, Task, Crew

nest_asyncio.apply()
load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash",
                             verbose=True, 
                             temperature=0.5, # Randomness
                             google_api_key = os.getenv("GOOGLE_API_KEY"))

# Speech Fine Tuner
speech_finetune_agent = Agent(
    role=""

)

# Message Agent
message_agent = Agent(
    role="Message Composer",
    goal="Generate a concise WhatsApp message based on user input",
    backstory="You are skilled at creating friendly and informative WhatsApp messages.",
    llm=llm
)

def get_message_from_input(user_input):
    task = Task(
    description=f"Generate a WhatsApp message from: '{user_input}'",
    agent=message_agent,
    expected_output="A single, concise WhatsApp message suitable to send to someone."
)
    crew = Crew(
        agents=[message_agent],
        tasks=[task],
        verbose=True
    )
    return crew.kickoff()
