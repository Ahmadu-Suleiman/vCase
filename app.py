import streamlit as st
from datetime import datetime


# --- Seed Data ---
def seed_cases():
    return [
        {
            'id': 1,
            'title': 'Broken Borehole in Zamfara Village',
            'summary': 'Residents of a rural village in Zamfara report that their only borehole is not dispensing water. Community leaders and organizations have exchanged updates on repair plans.',
            'threads': [
                {
                    'title': 'Initial Complaint',
                    'messages': [
                        {'timestamp': '2025-06-01 08:15', 'author': 'Member', 'channel': 'vCon',
                         'text': 'The borehole in Gidan-Dari village has stopped working completely.'},
                        {'timestamp': '2025-06-01 09:00', 'author': 'Organization', 'channel': 'Email',
                         'text': 'Thanks for reporting. Our team will assess the site.'},
                        {'timestamp': '2025-06-02 10:30', 'author': 'Member', 'channel': 'SMS',
                         'text': 'People are fetching from unsafe streams now.'},
                        {'timestamp': '2025-06-02 11:00', 'author': 'Organization', 'channel': 'vCon',
                         'text': 'Assessment completed. We will provide new pump parts soon.'},
                    ]
                },
                {
                    'title': 'Repairs and Confirmation',
                    'messages': [
                        {'timestamp': '2025-06-03 14:20', 'author': 'Organization', 'channel': 'SMS',
                         'text': 'Pump parts delivered. Installation ongoing.'},
                        {'timestamp': '2025-06-03 15:00', 'author': 'Member', 'channel': 'vCon',
                         'text': 'Installation complete. Water is flowing again. Thank you!'},
                    ]
                }
            ]
        },
        {
            'id': 2,
            'title': 'Collapsed Bridge in Bayelsa',
            'summary': 'A key bridge connecting two communities in Bayelsa collapsed after heavy rainfall. Case follows the safety alert and action plans.',
            'threads': [
                {
                    'title': 'Safety Alert and First Response',
                    'messages': [
                        {'timestamp': '2025-06-02 07:45', 'author': 'Member', 'channel': 'SMS',
                         'text': 'The wooden bridge to Okolobiri has collapsed. People are stranded.'},
                        {'timestamp': '2025-06-02 08:10', 'author': 'Organization', 'channel': 'Email',
                         'text': 'We are sending engineers to assess.'},
                        {'timestamp': '2025-06-02 16:00', 'author': 'Organization', 'channel': 'vCon',
                         'text': 'Temporary crossing set up. Permanent fix under budget review.'},
                        {'timestamp': '2025-06-03 09:30', 'author': 'Member', 'channel': 'SMS',
                         'text': 'Thanks. People are using the detour path for now.'},
                    ]
                },
                {
                    'title': 'Funding and Contractor Engagement',
                    'messages': [
                        {'timestamp': '2025-06-04 10:00', 'author': 'Organization', 'channel': 'Email',
                         'text': 'State government allocated emergency funds.'},
                        {'timestamp': '2025-06-05 12:00', 'author': 'Member', 'channel': 'vCon',
                         'text': 'Please ensure contractor begins soon. Rainfall expected again.'},
                    ]
                }
            ]
        },
        {
            'id': 3,
            'title': 'Unpaid Teachers in Local School',
            'summary': 'Teachers at a public school in Osun State have not been paid for three months. PTA and community leaders intervene.',
            'threads': [
                {
                    'title': 'Teacher Complaints',
                    'messages': [
                        {'timestamp': '2025-06-01 07:10', 'author': 'Member', 'channel': 'vCon',
                         'text': 'We have not received our salaries since March. We cannot continue teaching without pay.'},
                        {'timestamp': '2025-06-01 08:30', 'author': 'Organization', 'channel': 'Email',
                         'text': 'The issue is under review by the local government.'},
                        {'timestamp': '2025-06-02 09:00', 'author': 'Member', 'channel': 'SMS',
                         'text': 'Students are missing classes. We need action urgently.'},
                        {'timestamp': '2025-06-02 10:00', 'author': 'Organization', 'channel': 'vCon',
                         'text': 'We’ve escalated it to the education commissioner.'},
                    ]
                },
                {
                    'title': 'PTA Mediation',
                    'messages': [
                        {'timestamp': '2025-06-03 12:30', 'author': 'Organization', 'channel': 'SMS',
                         'text': 'PTA has offered emergency stipends.'},
                        {'timestamp': '2025-06-03 14:00', 'author': 'Member', 'channel': 'vCon',
                         'text': 'Thank you. Teaching will resume while we await salary resolution.'},
                    ]
                }
            ]
        },
        {
            'id': 4,
            'title': 'Electricity Transformer Theft in Kaduna',
            'summary': 'Residents report the theft of a community transformer. The issue is logged, and discussions around security and replacement begin.',
            'threads': [
                {
                    'title': 'Incident Reporting',
                    'messages': [
                        {'timestamp': '2025-06-01 06:00', 'author': 'Member', 'channel': 'vCon',
                         'text': 'Our transformer at Angwan Rimi was stolen last night.'},
                        {'timestamp': '2025-06-01 08:00', 'author': 'Organization', 'channel': 'Email',
                         'text': 'We are working with police and NEPA to investigate.'},
                        {'timestamp': '2025-06-01 11:45', 'author': 'Member', 'channel': 'SMS',
                         'text': 'We have no light and no business activity today.'},
                        {'timestamp': '2025-06-01 13:00', 'author': 'Organization', 'channel': 'vCon',
                         'text': 'Security patrols will increase. Replacement being discussed.'},
                    ]
                },
                {
                    'title': 'Replacement Planning',
                    'messages': [
                        {'timestamp': '2025-06-02 10:00', 'author': 'Organization', 'channel': 'Email',
                         'text': 'New transformer will arrive in 5 working days.'},
                        {'timestamp': '2025-06-02 12:30', 'author': 'Member', 'channel': 'vCon',
                         'text': 'Thank you. We will inform residents and prepare security volunteers.'},
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
    st.logo(
        image="case logo.png",
        size="large",
        link="https://linktr.ee/case.be.heard"
    )
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


st.set_page_config(
    page_title="vCase",
    page_icon="case logo.png",
    layout="wide",
    menu_items={
        'Get Help': 'mailto:casebeheard@gmail.com',
        'Report a bug': "mailto:casebeheard@gmail.com",
        'About': "https://linktr.ee/case.be.heard"
    }
)

# --- Render Appropriate Page ---
if st.session_state.page == 'home':
    render_home()
elif st.session_state.page == 'case':
    render_case()
elif st.session_state.page == 'thread':
    render_thread()
