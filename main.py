# main.py
from crew import get_message_from_input
from whatsapp_sender import send_whatsapp_message
from speech_to_text import transcribe_voice
import os
from dotenv import load_dotenv

load_dotenv()

instance_id = os.getenv("INSTANCE_ID")
token = os.getenv("TOKEN")

if __name__ == "__main__":
    print("Say the message")
    user_input = transcribe_voice()

    composed_message = get_message_from_input(user_input)

    print("\nWhatsApp Message : ")
    print(composed_message) 

    phone_number = input("\nEnter WhatsApp number : ")
    
    if not phone_number.startswith("+"):
        print("Invalid phone number.")
    else:
        result = send_whatsapp_message(phone_number, composed_message, instance_id, token)
        print("\nMessage Sent Result : ")
        print(result)
