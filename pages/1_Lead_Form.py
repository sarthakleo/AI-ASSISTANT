# pages/1_Lead_Form.py — NEW FILE
import streamlit as st
from database import save_lead
from email_utils import send_lead_notification

st.set_page_config(page_title='Get a Free Consultation', page_icon=':memo:')
st.title(' Get a Free Consultation')
st.caption('Tell us about your project — we will get back within 24 hours')
st.divider()

with st.form('business_lead_form', clear_on_submit=True):
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input('Full Name *', placeholder='Your name')
        email = st.text_input('Email Address *', placeholder='you@company.com')
        phone = st.text_input('Phone Number', placeholder='+91 XXXXXXXXXX')
    with col2:
        company = st.text_input('Company / Startup Name', placeholder='Your company')
        service = st.selectbox('Service Interested In *', [
            'AI Chatbot Development',
            'Business Process Automation',
            'LLM Integration',
            'Data Analytics Dashboard',
            'Custom AI Solution',
            'Not Sure — Need Consultation',
        ])
        budget = st.selectbox('Approximate Budget', [
            'Under 25,000',
            ' 25,000 – 50,000',
            ' 50,000 – 1,00,000',
            'Above 1,00,000',
            'To be discussed',
        ])
    message = st.text_area('Describe Your Requirement', height=100,
        placeholder='What problem do you want to solve with AI/automation?')
    submitted = st.form_submit_button(
        ' Request Free Consultation', use_container_width=True, type='primary')

if submitted:
    if not name.strip() or not email.strip():
        st.error('Name and Email are required.')
    else:
        save_lead(name, email, phone, company, service, budget, message)
        send_lead_notification(name, email, phone, company, service, budget, message)
        st.success(f'Thank you {name}! We will contact you within 24 hours.')