# Whizzap Pro – Role-Based WhatsApp Message Automation System

Whizzap Pro is a production-ready WhatsApp message automation system built using Python and Streamlit. Designed for administrative teams, educational institutions, and organizational workflows, Whizzap Pro converts natural language instructions into professional WhatsApp messages, automatically identifies the correct recipient based on role, and opens WhatsApp with the message pre-filled for quick dispatch.

This version is designed with interview readiness, explainability, and scalability in mind.


## Features

* **Natural Language Instruction Handling**: Accepts simple English instructions such as  
  “Inform correspondent to organize career guidance program”.
* **Role Detection from User Input**: Identifies recipient roles directly from the instruction text.
* **FAISS-Based Contact Matching**: Uses FAISS vector search to match detected roles with the most relevant contact from the dataset.
* **Professional Message Generation (Rule-Based NLP)**: Generates clean, formal, and interview-safe WhatsApp messages using deterministic rules (no LLMs).
* **Streamlit User Interface**: Interactive web interface for composing instructions, previewing messages, and triggering WhatsApp.
* **WhatsApp Deep-Link Integration**: Opens WhatsApp Web with the message pre-filled and ready to send.
* **Dataset-Driven Architecture**: Contacts are loaded from a CSV file, making the system easy to extend and maintain.
* **Action Logging**: Stores message activity logs for traceability and debugging.


## Project Structure



## How It Works

1. User enters a natural language instruction in the UI.
2. The system extracts the role from the instruction.
3. FAISS matches the role with the most relevant contact.
4. A professional message is generated using rule-based NLP.
5. WhatsApp opens with the message pre-filled and ready to send.


## Getting Started

### Installation

```bash
pip install -r requirements.txt

python build_faiss_index.py

streamlit run app.py
```


