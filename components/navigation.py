import streamlit as st


def show_navigation():

    st.sidebar.title("Navigation")

    if st.sidebar.button("🏠 Dashboard"):
        st.session_state.current_page = "dashboard"
        st.rerun()

    if st.sidebar.button("📄 Upload"):
        st.session_state.current_page = "upload"
        st.rerun()

    if st.sidebar.button("🔎 Search"):
        st.session_state.current_page = "search"
        st.rerun()

    if st.sidebar.button("📜 History"):
        st.session_state.current_page = "history"
        st.rerun()

    st.sidebar.divider()

    if st.sidebar.button("Logout"):

        from auth.session import logout

        logout()