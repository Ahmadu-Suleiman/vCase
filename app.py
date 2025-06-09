import io
import speech_recognition as sr
import streamlit as st

from datetime import datetime
from seed_cases import seed_cases

# --- Initialize Session State ---
if 'initialized' not in st.session_state:
    st.session_state.initialized = True
    st.session_state.cases = seed_cases()
    st.session_state.page = 'home'
    st.session_state.case_id = None
    st.session_state.thread_index = None


# --- Helper Functions ---
def format_message(msg):
    return f"**{msg['author']}** ({msg['channel']}) @ {msg['timestamp']}  \n> {msg['text']}"


def transcribe_audio_bytes(audio_file):
    try:
        audio_bytes = audio_file.read()
        audio_io = io.BytesIO(audio_bytes)

        recognizer = sr.Recognizer()
        with sr.AudioFile(audio_io) as source:
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            audio_data = recognizer.record(source)
            print(audio_data)
            transcript = recognizer.recognize_google(audio_data)
            return transcript
    except sr.UnknownValueError:
        st.error("Could not understand the audio.")
    except sr.RequestError as e:
        st.error(f"Speech recognition service error: {e}")
    return None


# --- Audio Recorder and Transcription ---
def record_and_transcribe_audio():
    try:
        st.subheader("🎙️ Record Audio for Transcription")
        audio_file = st.audio_input("Click to record audio message:")
        if audio_file is not None:
            st.audio(audio_file)
            transcript = transcribe_audio_bytes(audio_file)
            if transcript:
                st.success("Transcription successful:")
                st.info(transcript)
                with st.form("add_audio_msg_form"):
                    author = st.selectbox("Author (for audio)", ["Member", "Organization"], key="a_author")
                    channel = st.selectbox("Channel", ['Text', 'SMS', 'Email', 'Transcript'], key="a_channel")
                    if st.form_submit_button("Add Transcribed Message"):
                        return {
                            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M'),
                            'author': author,
                            'channel': channel,
                            'text': transcript
                        }

    except sr.UnknownValueError:
        st.error("Google Speech Recognition could not understand the audio. Please try again.")
    except sr.RequestError as e:
        st.error(f"Could not request results from Google Speech Recognition service; {e}")

    return None


# --- Page Rendering ---
def render_home():
    st.image("case logo.svg", width=100)
    st.title('vCase')
    st.subheader('vCon-Powered Communication Hub for the CASE Platform', divider='orange')
    st.markdown("""
    **vCase** is a vCon-powered platform that turns one-off reports into rich, ongoing conversations. 
    It brings together voice transcripts, SMS, and email into one centralized thread for each case, 
    making follow-up effortless and transparent.

    Each case holds:
    - A **chronological summary** for easy context
    - Multiple **threads** based on topics (e.g. Verification, Follow-Up)
    - Unified **messages** labeled by channel (SMS, Email, Transcripts)

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
        channel = st.selectbox('Channel', ['Text', 'SMS', 'Email', 'Transcript'])
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

    transcribed_msg = record_and_transcribe_audio()
    if transcribed_msg:
        thread['messages'].append(transcribed_msg)
        st.success("Transcribed message added!")
        st.rerun()

    if st.button('Back to Case'):
        st.session_state.page = 'case'
        st.rerun()
    if st.button('Home'):
        st.session_state.page = 'home'
        st.rerun()


# --- Page Setup ---
st.set_page_config(
    page_title="vCase",
    page_icon="case logo.png",
    menu_items={
        'Get Help': 'mailto:casebeheard@gmail.com',
        'Report a bug': 'mailto:casebeheard@gmail.com',
        'About': 'https://linktr.ee/case.be.heard'
    }
)

# --- Page Routing ---
if st.session_state.page == 'home':
    render_home()
elif st.session_state.page == 'case':
    render_case()
elif st.session_state.page == 'thread':
    render_thread()
