import streamlit as st
from core.contacts_manager import ContactsManager
import subprocess


def contacts_page():
    st.title("Contacts Management")

    manager = ContactsManager()
    df = manager.load()

    # ---------------- View ----------------
    st.subheader("All Contacts")
    st.dataframe(df, use_container_width=True)

    st.divider()

    # ---------------- Add ----------------
    st.subheader("Add Contact")

    name = st.text_input("Name")
    role = st.text_input("Role (e.g., hr, administrator)")
    phone = st.text_input("Phone")

    if st.button("Add Contact"):
        if name and role and phone:
            manager.add_contact(name, role, phone)
            st.success("Contact added successfully. Please rebuild FAISS index.")
            st.rerun()
        else:
            st.error("All fields are required.")

    st.divider()

    # ---------------- Update ----------------
    st.subheader("Update Contact")

    index = st.number_input(
        "Row Index to Update",
        min_value=0,
        max_value=len(df) - 1 if len(df) > 0 else 0,
        step=1
    )

    new_name = st.text_input("New Name")
    new_role = st.text_input("New Role")
    new_phone = st.text_input("New Phone")

    if st.button("Update Contact"):
        manager.update_contact(index, new_name, new_role, new_phone)
        st.success("Contact updated. Please rebuild FAISS index.")
        st.rerun()

    st.divider()

    # ---------------- Delete ----------------
    st.subheader("Delete Contact")

    delete_index = st.number_input(
        "Row Index to Delete",
        min_value=0,
        max_value=len(df) - 1 if len(df) > 0 else 0,
        step=1
    )

    if st.button("Delete Contact"):
        manager.delete_contact(delete_index)
        st.success("Contact deleted. Please rebuild FAISS index.")
        st.rerun()

    st.divider()

    # ---------------- FAISS Rebuild ----------------
    st.subheader("Search Index")

    if st.button("Rebuild FAISS Index"):
        subprocess.run(["python", "build_faiss_index.py"])
        st.success("FAISS index rebuilt successfully.")
