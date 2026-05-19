from groq import Groq
from config import GROQ_API_KEY, MODEL, MAX_TOKENS, TEMPERATURE
from prompts import (
    SYSTEM_PROMPT, SALES_PROMPT, TECHNICAL_SUPPORT_PROMPT,
    LEAD_PROMPT, FAQ_PROMPT
)

client = Groq(api_key=GROQ_API_KEY)

PROMPT_MAP = {
    'general': SYSTEM_PROMPT,
    'sales': SALES_PROMPT,
    'technical': TECHNICAL_SUPPORT_PROMPT,
    'lead': LEAD_PROMPT,
    'faq': FAQ_PROMPT,
}

def detect_prompt_type(user_message: str) -> str:
    """Detect which prompt to use based on user message keywords."""
    msg = user_message.lower()
    
    # Sales / Pricing keywords
    sales_keywords = [
        'price', 'cost', 'fee', 'how much', 'pricing', 'quote',
        'package', 'plan', 'buy', 'purchase', 'hire', 'budget',
        'affordable', 'cheap', 'expensive', 'rate', 'charge'
    ]
    
    # Technical support keywords
    tech_keywords = [
        'error', 'bug', 'not working', 'broken', 'integrate', 'api',
        'how to', 'technical', 'setup', 'configure', 'deploy',
        'webhook', 'database', 'install', 'implement'
    ]
    
    # Lead / contact / interested keywords
    lead_keywords = [
        'interested', 'contact', 'reach', 'call me', 'discuss',
        'demo', 'meeting', 'consult', 'get started', 'sign up',
        'register', 'inquiry', 'proposal', 'project'
    ]
    
    # FAQ keywords
    faq_keywords = [
        'how long', 'timeline', 'nda', 'support', 'after delivery',
        'startup', 'refund', 'guarantee', 'revision', 'contract'
    ]
    
    if any(k in msg for k in sales_keywords):
        return 'sales'
    elif any(k in msg for k in tech_keywords):
        return 'technical'
    elif any(k in msg for k in lead_keywords):
        return 'lead'
    elif any(k in msg for k in faq_keywords):
        return 'faq'
    else:
        return 'general'

def chat(history, user_message):
    history.append({"role": "user", "content": user_message})
    prompt_type = detect_prompt_type(user_message)
    system_prompt = PROMPT_MAP.get(prompt_type, SYSTEM_PROMPT)
    messages = [{"role": "system", "content": system_prompt}] + history
    response = client.chat.completions.create(
        model=MODEL,
        messages=messages,
        max_tokens=MAX_TOKENS,
        temperature=TEMPERATURE
    )
    reply = response.choices[0].message.content
    history.append({"role": "assistant", "content": reply})
    return reply

def stream_chat(history, user_message):
    history.append({"role": "user", "content": user_message})
    prompt_type = detect_prompt_type(user_message)
    system_prompt = PROMPT_MAP.get(prompt_type, SYSTEM_PROMPT)
    messages = [{"role": "system", "content": system_prompt}] + history
    stream = client.chat.completions.create(
        model=MODEL,
        messages=messages,
        max_tokens=MAX_TOKENS,
        temperature=TEMPERATURE,
        stream=True
    )
    for chunk in stream:
        if chunk.choices[0].delta.content:
            yield chunk.choices[0].delta.content

def new_conversation():
    return []

