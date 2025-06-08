import streamlit as st
from datetime import datetime

# --- Seed Data ---
def seed_cases():
    return [
        {
            'id': 1,
            'title': 'Water Access Complaint',
            'summary': 'Community reports broken well pump; follow-ups needed.',
            'threads': [
                {
                    'title': 'Initial Report',
                    'messages': [
                        {'timestamp': '2025-06-01 08:15', 'author': 'Member', 'channel': 'vCon', 'text': 'The well pump at the east end is not working.'},
                        {'timestamp': '2025-06-01 09:00', 'author': 'Organization', 'channel': 'Email', 'text': 'Acknowledged. We will inspect tomorrow.'},
                        {'timestamp': '2025-06-02 10:30', 'author': 'Member', 'channel': 'SMS', 'text': 'Any update on the inspection?'},
                        {'timestamp': '2025-06-02 11:00', 'author': 'Organization', 'channel': 'vCon', 'text': 'Inspection done; parts ordered.'},
                    ]
                },
                {
                    'title': 'Follow-Up Actions',
                    'messages': [
                        {'timestamp': '2025-06-03 14:20', 'author': 'Organization', 'channel': 'SMS', 'text': 'Pump installed. Please confirm.'},
                        {'timestamp': '2025-06-03 15:00', 'author': 'Member', 'channel': 'vCon', 'text': 'Confirmed—water flow resumed.'},
                    ]
                }
            ]
        },
        {
            'id': 2,
            'title': 'Road Repair Request',
            'summary': 'Potholes on Main St. causing accidents.',
            'threads': [
                {
                    'title': 'Safety Alert',
                    'messages': [
                        {'timestamp': '2025-06-02 07:45', 'author': 'Member', 'channel': 'SMS', 'text': 'Several accidents last night near Pond Road.'},
                        {'timestamp': '2025-06-02 08:10', 'author': 'Organization', 'channel': 'Email', 'text': 'We have dispatched a crew.'},
                        {'timestamp': '2025-06-02 16:00', 'author': 'Organization', 'channel': 'vCon', 'text': 'Crew completed temporary patch.'},
                        {'timestamp': '2025-06-03 09:30', 'author': 'Member', 'channel': 'SMS', 'text': 'Patch seems stable.'},
                    ]
                },
                {
                    'title': 'Permanent Fix Plan',
                    'messages': [
                        {'timestamp': '2025-06-04 10:00', 'author': 'Organization', 'channel': 'Email', 'text': 'Contractor scheduled for June 10.'},
                        {'timestamp': '2025-06-05 12:00', 'author': 'Member', 'channel': 'vCon', 'text': 'Please share cost details.'},
                    ]
                }
            ]
        }
    ]

if 'initialized' not in st.session_state:
    st.session_state.initialized = True
    st.session_state.cases = seed_cases()
    st.session_state.page = 'home'
    st.session_state.case_id = None
    st.session_state.thread_index = None

# --- Helper Functions ---
def format_message(msg):
    return f"**{msg['author']}** ({msg['channel']}) @ {msg['timestamp']}  \n> {msg['text']}"

# --- Page Rendering ---
def render_home():
    st.title('vCase: Voice-Centered Case Communication')
    st.markdown("""
    **vCase** is a vCon-powered platform that turns one-off reports into rich, ongoing conversations. 
    It brings together voice transcripts, SMS, and email into one centralized thread for each case, 
    making follow-up effortless and transparent.

    Each case holds:
    - A **chronological summary** for easy context
    - Multiple **threads** based on topics (e.g. Verification, Follow-Up)
    - Unified **messages** labeled by channel (vCon, SMS, Email)

    Explore your active cases below:
    """)
    for case in st.session_state.cases:
        if st.button(f"View Case #{case['id']}: {case['title']}", key=f"case{case['id']}"):
            st.session_state.page = 'case'
            st.session_state.case_id = case['id']
            st.rerun()

def render_case():
    case = next(c for c in st.session_state.cases if c['id'] == st.session_state.case_id)
    st.header(f"Case #{case['id']}: {case['title']}")
    st.subheader('Summary')
    st.info(case['summary'])
    st.subheader('Threads')
    for index, thread in enumerate(case['threads']):
        if st.button(thread['title'], key=f"thread{case['id']}_{index}"):
            st.session_state.page = 'thread'
            st.session_state.thread_index = index
            st.rerun()
    if st.button('Back to Home'):
        st.session_state.page = 'home'
        st.rerun()

def render_thread():
    case = next(c for c in st.session_state.cases if c['id'] == st.session_state.case_id)
    thread = case['threads'][st.session_state.thread_index]

    st.header(f"Case #{case['id']}: {case['title']} – Thread: {thread['title']}")
    st.subheader('Summary')
    st.info(case['summary'])

    st.subheader('Messages')
    for msg in thread['messages']:
        st.markdown(format_message(msg))
        st.markdown('---')

    st.subheader('Add to Thread')
    with st.form(key='msg_form'):
        author = st.selectbox('Author', ['Member', 'Organization'])
        channel = st.selectbox('Channel', ['vCon', 'SMS', 'Email'])
        text = st.text_area('Message')
        if st.form_submit_button('Send Message') and text.strip():
            new_msg = {
                'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M'),
                'author': author,
                'channel': channel,
                'text': text
            }
            thread['messages'].append(new_msg)
            st.success('Message added!')
            st.rerun()

    if st.button('Back to Case'):
        st.session_state.page = 'case'
        st.rerun()
    if st.button('Home'):
        st.session_state.page = 'home'
        st.rerun()

# --- Render Appropriate Page ---
if st.session_state.page == 'home':
    render_home()
elif st.session_state.page == 'case':
    render_case()
elif st.session_state.page == 'thread':
    render_thread()
