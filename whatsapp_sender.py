import requests

def send_whatsapp_message(phone_number, message, instance_id, token):
    url = f"https://api.ultramsg.com/{instance_id}/messages/chat"
    payload = {
        "token": token,
        "to": phone_number,
        "body": message
    }
    response = requests.post(url, data=payload)
    return response.json()
