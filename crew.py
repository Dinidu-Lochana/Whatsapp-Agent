from crewai import Crew, Process
from task import create_whatsapp_message
from agent import speech_finetune_agent, message_agent

def get_message_from_input(user_input):
    task = create_whatsapp_message(user_input)
    crew = Crew(
        agents=[speech_finetune_agent, message_agent],
        tasks=task,
        process=Process.sequential,  
        verbose=True
    )
    return crew.kickoff()
