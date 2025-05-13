from crewai import Task
from agent import message_agent

def create_whatsapp_task(user_input):
    return Task(
        description=f"Generate a WhatsApp message from: '{user_input}'",
        agent=message_agent,
        expected_output="A single, concise WhatsApp message suitable to send to someone."
    )
