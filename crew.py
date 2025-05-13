# crew.py
from crewai import Crew
from task import create_whatsapp_task
from agent import message_agent

def get_message_from_input(user_input):
    task = create_whatsapp_task(user_input)
    crew = Crew(
        agents=[message_agent],
        tasks=[task],
        verbose=True
    )
    return crew.kickoff()
