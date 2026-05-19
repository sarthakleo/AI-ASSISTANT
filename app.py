# app.py — FULL REWRITE
import streamlit as st
from bot import stream_chat, new_conversation
from config import (
    APP_TITLE, APP_ICON, APP_CAPTION,
    WELCOME_MESSAGE, QUICK_QUESTIONS,
)
from database import init_db

# Initialize SQLite database on every app start
init_db()

# Page config
st.set_page_config(
    page_title='Business Assistant | Codex',
    page_icon=':robot_face:',
    layout='centered'
)

# Session state init
if 'messages' not in st.session_state:
    st.session_state.messages = new_conversation()
if 'chat_started' not in st.session_state:
    st.session_state.chat_started = False

# Sidebar
with st.sidebar:
    st.title(' Business Assistant')
    st.caption('Codex Solutions · AI & Automation')
    st.divider()
    st.subheader('Quick Questions')
    for question in QUICK_QUESTIONS:
        if st.button(question, use_container_width=True):
            st.session_state['quick_input'] = question
    st.divider()
    st.info(' Use the sidebar pages to register interest or view the admin panel.')
    if st.button(' Clear Conversation', use_container_width=True):
        st.session_state.messages = new_conversation()
        st.session_state.chat_started = False
        st.rerun()

# Main chat area
st.title(' AI Business Assistant')
st.caption('Powered by · Codex Solutions')
st.divider()

# Show welcome if no messages yet
if not st.session_state.chat_started:
    with st.chat_message('assistant'):
        st.markdown(WELCOME_MESSAGE)

# Show existing chat history
for message in st.session_state.messages:
    with st.chat_message(message['role']):
        st.markdown(message['content'])

# Handle quick question button
if 'quick_input' in st.session_state:
    user_input = st.session_state.pop('quick_input')
else:
    user_input = None

# Chat input
if prompt := (st.chat_input('Ask about our services, pricing, automation...') or user_input):
    st.session_state.chat_started = True
    st.session_state.messages.append({'role': 'user', 'content': prompt})
    with st.chat_message('user'):
        st.markdown(prompt)
    with st.chat_message('assistant'):
        response = st.write_stream(
            stream_chat(st.session_state.messages, prompt)
        )
        st.session_state.messages.append({'role': 'assistant', 'content': response})