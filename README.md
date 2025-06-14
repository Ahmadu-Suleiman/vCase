# vCase

---

## Overview

**vCase** is a proof-of-concept demonstration of a vCon-powered communication hub within the CASE platform.
It transforms static case reports into structured, ongoing conversation threads that integrate multiple channels
(voice transcripts, SMS, email, direct messages). This prototype uses seeded data to illustrate how vCase unifies
all interactions for each case, preserving context, enabling transparent follow-up, and highlighting the benefits
for both community members and support organizations.

Try it out here: [vCase](https://vcase-be-heard.streamlit.app/)

---

## Key Features

* **Case Listing (Home Page)**

    * Displays all seeded cases from a community member’s perspective.
    * Each case shows an ID, title, and concise summary.

* **Case Detail View**

    * Presents the case title and its summary.
    * Lists all conversation threads associated with the case.
    * Allows navigation to any thread.

* **Thread View**

    * Shows a chronological sequence of messages, each labeled by:

        * **Author** (Member or Organization)
        * **Channel** (SMS, Email, etc.)
        * **Timestamp**
        * **Message Text** (simulating voice transcript or text content)
    * Provides a form to append new messages to the thread, simulating ongoing dialogue.

* **Multiple Threads per Case**

    * Each case can have multiple threads (e.g., “Case Verification”, “Follow-Up Actions”, “Outreach Coordination”,
      “Welfare Check”).
    * New threads can be added dynamically, illustrating how separate issues remain organized.

* **Seed Data**

    * Example cases with rich, multi-message threads covering various channels.
    * Pre-populated summaries and messages reflect realistic scenarios (e.g., land dispute verification, health clinic
      outreach).

* **Navigation Flow**

    * **Home Page**: List of cases; select to view details.
    * **Case Page**: Summary and thread selection; back navigation to home.
    * **Thread Page**: Full conversation history; form to add messages; back navigation to case or home.

---

## Intended Demonstration

This prototype is designed for a hackathon setting to showcase:

* **vCon-Centric Communication**: All interactions (voice transcripts, SMS, emails) appear in a unified thread.
* **Context Preservation**: Summaries and labeled messages ensure that anyone reviewing the case sees the full history
  at a glance.
* **Multi-Channel Integration**: By mixing channels in one view, it highlights how vCase centralizes communications.
* **Ease of Follow-Up**: Appending messages to existing threads illustrates effortless back-and-forth.
* **Accessibility Focus**: Simulated “voice transcripts” signal how low-literacy or low-connectivity users can interact
  via voice or SMS in a real implementation.

---

## Prerequisites

* **Python 3.8+** installed on the local machine.
---

## Installation & Setup

1. **Clone or Copy the Prototype Directory**

   Place all prototype files (including `app.py` or equivalent) in a local directory.

2. **Create and Activate a Virtual Environment (Optional but Recommended)**

   ```bash
   python3 -m venv vcase-env
   source vcase-env/bin/activate
   ```

3. **Install Dependencies**

   If a requirements file is provided (e.g., `requirements.txt`), install:

   ```bash
   pip install -r requirements.txt
   ```

4. **Seed Data**

   The code includes seeded cases and threads. No external database or backend is required. All data resides in
   in-memory or local structures within the prototype.

---

## Running the Prototype

1. **Launch the App**

   For a Streamlit-based demo:

   ```bash
   streamlit run app.py
   ```

2. **Navigate the Interface**

    * **Home Page**: Lists seeded cases. Click “View Case #…” to proceed.
    * **Case Page**: Displays case summary and available threads. Select a thread.
    * **Thread Page**: Review existing messages and add new ones via the provided form.
    * Use “Back to Case” or “Home” controls to navigate as needed.

3. **Simulating Interaction**

    * In the thread view, selecting “Author” and “Channel” then entering text simulates adding a new message:

        * **Author**: “Member” or “Organization”
        * **Channel**: “vCon” (for voice transcript), “SMS”, or “Email”
        * **Message Text**: Represents the transcript or text content
    * Upon submission, the message appears immediately in the conversation timeline with current timestamp.

---

## Customizing Seed Data

* **Cases**: Modify or add entries in the seed data array/list at the top of the prototype code.
* **Threads**: For each case, add or adjust thread objects with:

    * `title`: String title of the thread (e.g., “Verification”).
    * `messages`: List of message objects, each with `timestamp`, `author`, `channel`, `text`.
* **Summary**: Update case summaries to reflect the desired narrative for demonstration.

---

## Demo Script Suggestions

1. **Introduction**: Briefly explain the purpose of vCase within the CASE platform.
2. **Home View**: Show how cases are listed for a community member.
3. **Case Overview**: Highlight the summary and its role in context preservation.
4. **Thread Review**: Navigate through “Case Verification” thread; point out mixed-channel messages.
5. **Append Message**: Demonstrate adding a follow-up message (e.g., organization asks a question, member replies).
6. **New Thread Creation**: Show how a new thread (e.g., “Follow-Up Actions”) is started and populated.
7. **Emphasize Benefits**: Summarize how this prototype reflects vCon-powered improvements:

    * Unified view of voice/SMS/email
    * Effortless follow-up
    * Clear context through summaries and labeled messages
    * Accessibility for low-literacy or low-connectivity scenarios (simulated via voice transcript placeholders)

---

## Limitations

* **No Persistent Backend**: Data resets on restart or refresh; this is a front-end demonstration only.
* **Text Simulation of Voice**: Actual audio recording/playback is not implemented; messages are treated as transcripts.
* **No Authentication**: Both community member and organization roles are simulated without login.
* **Static Seed Data**: Interaction beyond the seeded cases depends on in-memory structures; not stored permanently.
* **No Real SMS/Email Integration**: Channels are labels only, without actual messaging services.

These limitations are intentional to keep the prototype simple and demonstrable in a short timeframe. The focus is on
illustrating vCon-based thread structure and the benefits it brings.

---

## Next Steps (Beyond Prototype)

* **Persistent Storage**: Integrate a backend or database for real data persistence.
* **Audio Capture & Playback**: Enable recording and playback of voice messages.
* **Multichannel Integration**: Connect real SMS, email, and voice-call services.
* **Summarization & AI Assist**: Add automated summaries and chat assistance per thread.
* **User Authentication & Roles**: Implement user accounts for community members and organization staff.
* **Security & Privacy**: Ensure encryption, access controls, and data protection for sensitive case information.
* **Localization**: Support multiple languages and voice prompts for low-literacy contexts.
* **Offline / Sync**: Design offline-first capabilities for intermittent connectivity.

---

## Acknowledgments

This prototype was developed to demonstrate the value of vCase as the vCon-powered communication hub for the CASE
platform, emphasizing accessibility, context preservation, and efficient case management for underserved communities. It
serves as a foundation for further development and real-world deployment.

---