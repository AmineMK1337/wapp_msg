import os
from dotenv import load_dotenv
from twilio.rest import Client

# Load environment variables
load_dotenv()

# Get credentials from .env
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
twilio_number = os.getenv("TWILIO_WHATSAPP_NUMBER")

# Create Twilio client
client = Client(account_sid, auth_token)

def send_whatsapp_message(to_number, message_text):
    message = client.messages.create(
        from_=twilio_number,
        body=message_text,
        to=f"whatsapp:{to_number}"
    )
    return message.sid

if __name__ == "__main__":
    receiver = "+21650767482"  # put the real number
    text = "waaaaaaaaaywa"

    sid = send_whatsapp_message(receiver, text)
    print("Message sent successfully!")
    print("Message SID:", sid)
