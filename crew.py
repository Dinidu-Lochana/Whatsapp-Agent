from crewai import Crew, Process
from task import create_whatsapp_message
from agent import speech_finetune_agent, message_agent

def get_message_from_input(user_input):
    task = create_whatsapp_message(user_input) # Create the tasl according to user speech
    crew = Crew(
        agents=[
            speech_finetune_agent,   # Fine tuning the text of user speech
            message_agent],          # Generate the whatsapp message
        tasks=task,
        process=Process.sequential,  
        verbose=True    # Enable logging for debugging
    )
    return crew.kickoff()
