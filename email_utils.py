# email_utils.py — NEW FILE
import smtplib, os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

def send_lead_notification(name, email, phone, company, service, budget, message=''):
    """
    Automation Workflow: Lead Form submitted → Email notification sent.
    This is the mandatory automation workflow for the assessment.
    """
    try:
        sender = os.getenv('EMAIL_SENDER')
        password = os.getenv('EMAIL_PASSWORD')
        receiver = os.getenv('EMAIL_RECEIVER')
        body = f'''
 NEW BUSINESS LEAD — Codex Business Assistant
 {'='*50}
Name: {name}
Email: {email}
Phone: {phone or 'Not provided'}
Company: {company or 'Not provided'}
Service: {service}
Budget: {budget}
Message: {message or 'None'}
Time: {datetime.now().strftime('%d %b %Y, %I:%M %p IST')}
→ Login to Admin Dashboard to view all leads.
'''
        msg = MIMEMultipart()
        msg['Subject'] = f'[Codex] New Lead: {name} — {service}'
        msg['From'] = sender
        msg['To'] = receiver
        msg.attach(MIMEText(body, 'plain'))
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(sender, password)
            server.send_message(msg)
        return True, 'Notification sent'
    except Exception as e:
        print(f'[Email Error] {e}')
        return False, str(e)