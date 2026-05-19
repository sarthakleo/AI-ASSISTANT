# pages/2_Admin_Dashboard.py — NEW FILE
import streamlit as st
import pandas as pd
from database import get_all_leads

st.set_page_config(
    page_title='Admin Dashboard', page_icon=':bar_chart:', layout='wide')
st.title(' Admin Dashboard')
st.caption('Business Lead Intelligence — Codex Solutions')
st.divider()

leads = get_all_leads()
if not leads:
    st.info('No leads yet. Share the consultation form link to start capturing leads.')
    st.stop()

df = pd.DataFrame(leads)

# KPI Row
c1, c2, c3, c4, c5 = st.columns(5)
c1.metric('Total Leads', len(df))
c2.metric('Unique Companies', df['company'].nunique())
today = pd.Timestamp.now().strftime('%Y-%m-%d')
c3.metric('Today', len(df[df['timestamp'].str.startswith(today)]))
hot = df[df['budget'].str.contains('1,00,000|50,000', na=False)]
c4.metric('High Budget Leads', len(hot))
c5.metric('Avg per Day',
    round(len(df) / max(df['timestamp'].str[:10].nunique(), 1), 1))

st.divider()

# Leads Table
col1, col2 = st.columns([3, 1])
with col1: st.subheader('All Leads')
with col2:
    search = st.text_input('Search', placeholder='name / email / company')

show_df = df.copy()
if search:
    mask = (
        show_df['name'].str.contains(search, case=False, na=False) |
        show_df['email'].str.contains(search, case=False, na=False) |
        show_df['company'].str.contains(search, case=False, na=False)
    )
    show_df = show_df[mask]

st.dataframe(
    show_df[['id', 'name', 'email', 'company', 'service', 'budget', 'timestamp']],
    use_container_width=True, hide_index=True
)

# Charts Row
st.divider()
ch1, ch2 = st.columns(2)
with ch1:
    st.subheader('Leads by Service')
    st.bar_chart(df['service'].value_counts())
with ch2:
    st.subheader('Leads by Budget Range')
    st.bar_chart(df['budget'].value_counts())

# Export
st.divider()
csv = df.to_csv(index=False)
st.download_button(
    ' Download All Leads (CSV)',
    csv, 'business_leads.csv', 'text/csv',
    use_container_width=True
)