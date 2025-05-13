# task.py
from crewai import Task
from agent import speech_finetune_agent, message_agent

def create_whatsapp_message(user_input):
    
    correct_input_task = Task(
        description=f"Clean and refine this speech-to-text input: '{user_input}'",
        agent=speech_finetune_agent,
        expected_output="A clean and well-structured version of the original input."
    )

    message_task = Task(
        description="Generate a WhatsApp message from the corrected input.",
        agent=message_agent,
        expected_output="A single, concise WhatsApp message suitable to send to someone.",
        depends_on=[correct_input_task]
    )

    return [correct_input_task, message_task]
