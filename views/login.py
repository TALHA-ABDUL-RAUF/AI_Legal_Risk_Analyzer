import streamlit as st

from database.database import SessionLocal
from auth.login import login_user
from components.navigation import show_navigation

def show():
    st.title("🔐 Login")

    email = st.text_input("Email")

    password = st.text_input(
        "Password",
        type="password",
    )

    col1, col2, col3 = st.columns([1, 1, 6])

    with col1:

        if st.button("Login"):

            db = SessionLocal()

            success, message, user = login_user(
                db=db,
                email=email,
                password=password,
            )

            db.close()

            if success:

                st.session_state.logged_in = True
                st.session_state.user_id = user.id
                st.session_state.email = user.email
                st.session_state.role = user.role

                st.session_state.current_page = "dashboard"

                st.rerun()

            else:
                st.error(message)

    with col2:

        if st.button("Register"):

            st.session_state.current_page = "register"

            st.rerun()