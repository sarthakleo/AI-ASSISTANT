import os
from dotenv import load_dotenv
load_dotenv()
GROQ_API_KEY = os.getenv('GROQ_API_KEY')
MODEL = 'llama-3.3-70b-versatile'
MAX_TOKENS = 1024
TEMPERATURE = 0.7
APP_TITLE = ' Business Assistant'
APP_ICON = 'robot_face'
APP_CAPTION = 'AI-Powered Business Automation Assistant | Codex'
WELCOME_MESSAGE = 'Welcome! I am your AI Business Assistant. '
'I can help with: services, pricing, automation, support, and sales.'
SERVICES = {
'AI Chatbot Development': {'price': ' 49,999–1,49,999', 'weeks': '2–6'},
'Business Process Automation': {'price': ' 29,999–99,999', 'weeks': '1–4'},
'LLM Integration': {'price': ' 39,999–1,19,999', 'weeks': '2–5'},
'Data Analytics Dashboard': {'price': ' 24,999–79,999', 'weeks': '1–3'},
}
BUSINESS_INFO = {
'company_name': 'Codex Solutions',
'tagline': 'Automate. Innovate. Accelerate.',
'website': 'codex.com',
'email': 'hello@codex.com',
'phone': '1800-COD-ENIX',
'support_hours': 'Mon–Sat, 9 AM – 7 PM IST',
}
QUICK_QUESTIONS = [
'What services do you offer?',
'How much does a chatbot cost?',
'Can you automate my business workflows?',
'What is your typical project timeline?',
'Do you offer post-deployment support?',
'How do I get started?',
]
# Email + DB (NEW additions)
EMAIL_SENDER = os.getenv('EMAIL_SENDER')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')
EMAIL_RECEIVER = os.getenv('EMAIL_RECEIVER')
DB_PATH = 'leads.db'