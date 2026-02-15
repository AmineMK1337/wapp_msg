# WhatsApp Sender

A Python script to send WhatsApp messages using the Twilio API.

## Prerequisites

- Python 3.8+
- A Twilio account with WhatsApp sandbox enabled

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

5. **Create a `.env` file** in the root directory with your Twilio credentials:
   ```env
   TWILIO_ACCOUNT_SID=your_account_sid
   TWILIO_AUTH_TOKEN=your_auth_token
   TWILIO_WHATSAPP_NUMBER=whatsapp:+14155238886
   ```

6. **Join the Twilio WhatsApp Sandbox**
   - Go to [Twilio Console > Messaging > WhatsApp](https://console.twilio.com/us1/develop/sms/try-it-out/whatsapp-learn)
   - Send the join code from your WhatsApp to the sandbox number (+1 415 523 8886)

## Usage

1. Edit `app/main.py` and set the `receiver` variable to the recipient's phone number (with country code):
   ```python
   receiver = "+1234567890"
   ```

2. Run the script:
   ```bash
   cd app
   python main.py
   ```

## Notes

- The sender number must be the Twilio WhatsApp sandbox number (for testing) or an approved WhatsApp Business number.
- Recipients must join the sandbox before receiving messages.
- Phone numbers must include the country code (e.g., +216 for Tunisia).
