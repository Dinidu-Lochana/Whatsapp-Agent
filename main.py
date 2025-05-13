# main.py
from agent import get_message_from_input
from whatsapp_sender import send_whatsapp_message
import os
from dotenv import load_dotenv

load_dotenv()

instance_id = os.getenv("INSTANCE_ID")
token = os.getenv("TOKEN")


if __name__ == "__main__":
    user_input = input("Enter your message intent: ")
    composed_message = get_message_from_input(user_input)
    
    phone = input("Enter WhatsApp number (with country code): ")
    
    
    
    result = send_whatsapp_message(phone, composed_message, instance_id, token)
    print("Message Sent Result:", result)
