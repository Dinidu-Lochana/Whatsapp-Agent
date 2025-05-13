# agent_gemini.py
import os
from dotenv import load_dotenv
import nest_asyncio
from langchain_google_genai import ChatGoogleGenerativeAI
from crewai import Agent

nest_asyncio.apply()
load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash",
                             verbose=True, 
                             temperature=0.5, # Randomness
                             google_api_key = os.getenv("GOOGLE_API_KEY"))

# Speech Fine Tuner
speech_finetune_agent = Agent(
    role="Speech Fine Tuner",
    goal="Refine the transcription into grammatically correct English",
    backstory="You are skilled at correcting transcribed speech into clear written form and also fill the missing parts of the transcribed speech.",
    llm=llm
)

# Message Agent
message_agent = Agent(
    role="Message Composer",
    goal="Generate a WhatsApp message based on user input",
    backstory="You are skilled at creating friendly WhatsApp messages.",
    llm=llm
)
