# WhatsApp & Email Sender

Python scripts to send WhatsApp messages (via Twilio) and emails (via SMTP).

## 📁 Project Structure

```
whatsapp_sender/
├── app/
│   ├── main.py           # WhatsApp message sender
│   └── mail_service.py   # Email sender
├── .env.example          # Environment variables template
├── .gitignore
├── requirements.txt
└── README.md
```

## Prerequisites

- Python 3.8+
- A Twilio account with WhatsApp sandbox enabled (for WhatsApp)
- A Gmail account with App Password enabled (for email)

## Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/AmineMK1337/wapp_message.git
   cd wapp_message
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**
   - Windows:
     ```bash
     venv\Scripts\activate
     ```
   - Linux/Mac:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Create a `.env` file** from the example template:
   ```bash
   cp .env.example .env
   ```
   
   Then edit `.env` with your credentials:
   ```env
   # Twilio (WhatsApp)
   TWILIO_ACCOUNT_SID=your_account_sid
   TWILIO_AUTH_TOKEN=your_auth_token
   TWILIO_WHATSAPP_NUMBER=whatsapp:+14155238886

   # Email
   EMAIL_ADDRESS=your_email@gmail.com
   EMAIL_PASSWORD=your_app_password
   SMTP_SERVER=smtp.gmail.com
   SMTP_PORT=587
   ```

6. **Join the Twilio WhatsApp Sandbox**
   - Go to [Twilio Console > Messaging > WhatsApp](https://console.twilio.com/us1/develop/sms/try-it-out/whatsapp-learn)
   - Send the join code from your WhatsApp to the sandbox number (+1 415 523 8886)

## Usage

### Send WhatsApp Message

1. Edit `app/main.py` and set the `receiver` variable to the recipient's phone number (with country code):
   ```python
   receiver = "+1234567890"
   ```

2. Run the script:
   ```bash
   cd app
   python main.py
   ```

### Send Email

1. Edit `app/mail_service.py` and set the recipient, subject, and body:
   ```python
   recipient = "destination@example.com"
   subject = "Test Email"
   body = "Hello! This is a test email."
   ```

2. Run the script:
   ```bash
   cd app
   python mail_service.py
   ```

### Gmail App Password Setup

If using Gmail, you need an App Password (not your regular password):
1. Go to [Google Account > Security](https://myaccount.google.com/security)
2. Enable 2-Step Verification
3. Go to App Passwords and generate one for "Mail"
4. Use that password in your `.env` file

## Notes

- The sender number must be the Twilio WhatsApp sandbox number (for testing) or an approved WhatsApp Business number.
- Recipients must join the sandbox before receiving messages.
- Phone numbers must include the country code (e.g., +216 for Tunisia).

## Other Email Providers

| Provider | SMTP Server | Port |
|----------|-------------|------|
| Gmail | smtp.gmail.com | 587 |
| Outlook | smtp-mail.outlook.com | 587 |
| Yahoo | smtp.mail.yahoo.com | 587 |

## 🔒 Security

- **Never commit your `.env` file** - it's already in `.gitignore`
- Use `.env.example` as a template for others
- For Gmail, always use App Passwords instead of your account password
- Rotate your API keys and passwords regularly

## 📄 License

MIT License
