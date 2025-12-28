import streamlit as st
import pathlib

from ui.composer import composer_page
from ui.logs import logs_page
from ui.contacts import contacts_page

# ---------------- Load CSS ----------------
style_path = pathlib.Path("assets/style.css")
if style_path.exists():
    st.markdown(
        f"<style>{style_path.read_text()}</style>",
        unsafe_allow_html=True
    )

anim_path = pathlib.Path("assets/animations.css")
if anim_path.exists():
    st.markdown(
        f"<style>{anim_path.read_text()}</style>",
        unsafe_allow_html=True
    )

# ---------------- Page Config ----------------
st.set_page_config(
    page_title="Whizzap",
    layout="wide"
)

# ---------------- Sidebar ----------------
st.sidebar.title("Whizzap")

page = st.sidebar.radio(
    "Navigation",
    ["Compose Message", "Contacts", "Logs"]
)

if page == "Compose Message":
    composer_page()
elif page == "Contacts":
    contacts_page()
elif page == "Logs":
    logs_page()

