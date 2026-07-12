import streamlit as st


def is_logged_in():
    return st.session_state.get("logged_in", False)


def is_admin():
    return st.session_state.get("role") == "admin"


def logout():

    st.session_state.logged_in = False
    st.session_state.user_id = None
    st.session_state.email = None
    st.session_state.role = None
    st.session_state.current_page = "login"

    st.rerun()