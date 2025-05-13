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
    print("🧠 Waiting for voice input...")
    user_input = transcribe_voice()

    if not user_input.strip():
        print("❌ Could not understand speech. Try again.")
        exit()

    composed_message = get_message_from_input(user_input)

    print("\n📤 Composed WhatsApp Message:")
    print(composed_message)

    phone = input("\n📱 Enter WhatsApp number (with country code, e.g., +94712345678): ")
    
    if not phone.startswith("+"):
        print("❌ Invalid phone number format. Must include country code starting with '+'.")
    else:
        result = send_whatsapp_message(phone, composed_message, instance_id, token)
        print("\n✅ Message Sent Result:")
        print(result)
