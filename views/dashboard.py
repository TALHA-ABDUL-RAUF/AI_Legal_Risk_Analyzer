import streamlit as st

from auth.session import is_logged_in, logout
from sqlalchemy import func

from database.database import SessionLocal
from database.crud import total_documents, total_analysis
from components.navigation import show_navigation

def show():

    if not is_logged_in():
        st.warning("Please login first.")
        st.session_state.current_page = "login"
        st.rerun()

    st.title("🏠 Dashboard")
    show_navigation()
    st.success("Login Successful")

    st.write(f"User ID: {st.session_state.user_id}")
    st.write(f"Email: {st.session_state.email}")
    st.write(f"Role: {st.session_state.role}")

    db = SessionLocal()

    docs = total_documents(
        db,
        st.session_state.user_id
    )

    analysis = total_analysis(
        db,
        st.session_state.user_id
    )

    c1, c2 = st.columns(2)

    with c1:
        st.metric("Documents", docs)

    with c2:
        st.metric("Analyses", analysis)

    db.close()

    # ---------------- Admin ----------------

    if st.session_state.role == "admin":

        if st.button("Admin Panel"):

            st.session_state.current_page = "admin"
            st.rerun()

    # ---------------- Upload / Search ----------------

    col1, col2 = st.columns(2)

    with col1:

        if st.button("📄 Upload Contract", use_container_width=True):

            st.session_state.current_page = "upload"
            st.rerun()

    with col2:

        if st.button("🔎 Semantic Search", use_container_width=True):

            st.session_state.current_page = "search"
            st.rerun()

    # ---------------- Pipeline Overview ----------------

    # ---------------- Pipeline Overview ----------------

    st.divider()
    st.subheader("⚙️ How It Works")

    pipeline_steps = [
        ("📤", "Upload"),
        ("✅", "Validation"),
        ("📄", "Text Extraction"),
        ("🧩", "Chunking"),
        ("🧠", "Embeddings"),
        ("🗂️", "ChromaDB"),
        ("🔎", "Semantic Search"),
        ("🦙", "Llama3"),
        ("⚖️", "Legal Risk Analysis"),
    ]

    steps_html = ""
    for i, (icon, label) in enumerate(pipeline_steps):
        steps_html += f'<div class="pipeline-step"><span class="icon">{icon}</span>{label}</div>'
        if i < len(pipeline_steps) - 1:
            steps_html += '<div class="pipeline-arrow">➜</div>'

    pipeline_html = (
        '<style>'
        '.pipeline-wrap{display:flex;flex-wrap:wrap;align-items:center;gap:6px;padding:16px 4px;}'
        '.pipeline-step{background:linear-gradient(135deg,#1f2937,#111827);border:1px solid #374151;'
        'border-radius:10px;padding:10px 14px;color:#f9fafb;font-size:13px;font-weight:600;'
        'text-align:center;min-width:100px;box-shadow:0 2px 6px rgba(0,0,0,0.25);}'
        '.pipeline-step .icon{font-size:20px;display:block;margin-bottom:4px;}'
        '.pipeline-arrow{color:#9ca3af;font-size:18px;font-weight:bold;}'
        '</style>'
        f'<div class="pipeline-wrap">{steps_html}</div>'
    )

    st.markdown(pipeline_html, unsafe_allow_html=True)
  

    # ---------------- History / Logout ----------------

    col1, col2 = st.columns(2)

    with col1:

        if st.button("📜 History", use_container_width=True):

            st.session_state.current_page = "history"
            st.rerun()

    with col2:

        if st.button("🚪 Logout", use_container_width=True):

            logout()

            st.session_state.logged_in = False
            st.session_state.user_id = None
            st.session_state.email = None
            st.session_state.role = None
            st.session_state.current_page = "login"

            st.rerun()