import streamlit as st

from core.role_extractor import RoleExtractor
from core.faiss_engine import FaissEngine
from core.message_builder import MessageBuilder
from core.logger import ActionLogger
from core.whatsapp_link import build_whatsapp_link


@st.cache_resource
def load_components():
    # Initialize FAISS engine
    faiss_engine = FaissEngine(
        contacts_path="data/contacts.csv",
        index_path="data/faiss.index"
    )

    # Load contacts once
    faiss_engine.load_contacts()

    return (
        RoleExtractor(),                     # Role detection
        faiss_engine,                        # Semantic search
        MessageBuilder(default_signature="Whizzap"),  # Message formatting
        ActionLogger(log_file="data/message_logs.csv")
    )


def composer_page():
    st.title("Compose Message")

    role_extractor, faiss_engine, message_builder, logger = load_components()

    st.markdown("### Enter your instruction")

    prompt = st.text_area(
        "Instruction",
        placeholder="Send message to class teacher about attending class 12B",
        height=120
    )

    tone = st.selectbox("Message tone", ["neutral", "formal"])

    if st.button("Generate Message"):
        if not prompt.strip():
            st.error("Please enter a valid instruction.")
            return

        # -------- Step 1: Role Extraction --------
        role = role_extractor.extract_role(prompt)

        if role is None:
            st.error("Unable to detect role from instruction.")
            return

        # -------- Step 2: FAISS Matching --------
        matches = faiss_engine.search(role, top_k=1)

        if not matches:
            st.error("No matching contact found.")
            return

        best = matches[0]

        # -------- Step 3: Message Generation --------
        message = message_builder.build(
            prompt=prompt,
            recipient_name=best["name"],
            tone=tone
        )

        st.divider()

        # -------- Detected Recipient --------
        st.subheader("Detected Recipient")
        st.write(f"**Name:** {best['name']}")
        st.write(f"**Role:** {best['role']}")
        st.write(f"**Phone:** {best['phone']}")

        # -------- Message Preview --------
        st.subheader("Message Preview")
        st.text_area("Final Message", message, height=180)

        # -------- WhatsApp Button --------
        whatsapp_url = build_whatsapp_link(best["phone"], message)

        st.markdown(
            f"""
            <a href="{whatsapp_url}" target="_blank">
                <button style="
                    padding:12px 20px;
                    border-radius:10px;
                    border:none;
                    background:#25D366;
                    color:black;
                    font-weight:600;
                    font-size:15px;
                    cursor:pointer;
                ">
                    Open WhatsApp Chat
                </button>
            </a>
            """,
            unsafe_allow_html=True
        )

        st.caption("WhatsApp will open with the message pre-filled. Press Enter to send.")

        # -------- Logging --------
        logger.log({
            "prompt": prompt,
            "role": role,
            "name": best["name"],
            "phone": best["phone"],
            "status": "DRY_RUN",
            "details": "WhatsApp chat opened with pre-filled message"
        })
