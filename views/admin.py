import streamlit as st
from components.navigation import show_navigation
from auth.session import (
    is_logged_in,
    is_admin,
)


def show():

    if not is_logged_in():

        st.warning("Please login.")

        st.session_state.current_page = "login"

        st.rerun()

    if not is_admin():

        st.error("Access Denied")

        return

    st.title("🛡️ Admin Panel")

    st.success("Administrator Access Granted")