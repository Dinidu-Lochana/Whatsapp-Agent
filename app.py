# app.py
import streamlit as st
from crew import get_message_from_input
from whatsapp_sender import send_whatsapp_message
from speech_to_text import transcribe_voice
import os
from dotenv import load_dotenv

load_dotenv()

# Load environment variables
instance_id = os.getenv("INSTANCE_ID")
token = os.getenv("TOKEN")

st.set_page_config(page_title="🎙️ WhatsApp Voice Messenger", layout="centered")

st.title("🎙️ WhatsApp Voice Message Generator")
st.markdown("Speak your intent and generate a WhatsApp message using AI.")

# Step 1: Capture voice
if st.button("🎤 Start Voice Input"):
    with st.spinner("Listening... Speak now!"):
        user_input = transcribe_voice()

    if user_input.strip() == "":
        st.error("Could not understand the voice input.")
    else:
        st.success(f"✅ Transcribed: `{user_input}`")

        # Step 2: Generate WhatsApp message
        with st.spinner("🧠 Generating WhatsApp message..."):
            composed_message = get_message_from_input(user_input)

        st.markdown("### ✉️ Composed WhatsApp Message:")
        st.info(composed_message)

        # Step 3: Send message
        phone_number = st.text_input("📱 Enter phone number (with country code)", placeholder="+94712345678")

        if st.button("📤 Send WhatsApp Message"):
            if not phone_number.startswith("+"):
                st.error("❌ Please enter a valid phone number with country code (e.g., +94...)")
            else:
                with st.spinner("Sending message..."):
                    result = send_whatsapp_message(phone_number, composed_message, instance_id, token)

                st.success("✅ Message Sent!")
                st.json(result)
