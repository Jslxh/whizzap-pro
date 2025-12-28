import streamlit as st
import pandas as pd
import os


def logs_page():
    st.title("Message Logs")
    st.subheader("Execution History")

    log_file = "data/message_logs.csv"

    if not os.path.exists(log_file):
        st.info("No logs available yet.")
        return

    df = pd.read_csv(log_file)

    if df.empty:
        st.info("No log entries found.")
        return

    # Backward compatibility for old logs
    if "timestamp" not in df.columns:
        st.warning("Log file is missing timestamps. Showing unsorted logs.")
        st.dataframe(df)
        return

    df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")
    df = df.sort_values(by="timestamp", ascending=False)

    st.dataframe(df, use_container_width=True)
