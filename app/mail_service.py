import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get credentials from .env
email_address = os.getenv("EMAIL_ADDRESS")
email_password = os.getenv("EMAIL_PASSWORD")
smtp_server = os.getenv("SMTP_SERVER", "smtp.gmail.com")
smtp_port = int(os.getenv("SMTP_PORT", 587))


def send_email(to_email, subject, body, html=False):
    """
    Send an email to the specified recipient.
    """
    msg = MIMEMultipart()
    msg["From"] = email_address
    msg["To"] = to_email
    msg["Subject"] = subject

    content_type = "html" if html else "plain"
    msg.attach(MIMEText(body, content_type))

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(email_address, email_password)
            server.sendmail(email_address, to_email, msg.as_string())
        return True
    except Exception as e:
        print(f"Error sending email: {e}")
        return False


if __name__ == "__main__":
    recipient = "baya.chatti.ahmed@gmail.com"
    subject = "SOSVE EMERGENCY!"

    # 🔹 Variable for remaining time
    remaining_time = "2 heures"  # Change dynamically if needed

    body = f"""Bonjour,

Pourriez-vous, s’il vous plaît, vérifier vos signalements et compléter les fichiers ainsi que le rapport DPE ?
Il vous reste {remaining_time} pour finaliser cette tâche.

Merci pour votre collaboration.

Cordialement,
L'équipe SOSVE"""

    if send_email(recipient, subject, body):
        print("Email sent successfully!")
    else:
        print("Failed to send email.")
