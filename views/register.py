import streamlit as st

from database.database import SessionLocal
from auth.register import register_user

from components.navigation import show_navigation
def show():

    st.title("📝 Register")
    show_navigation()
    email = st.text_input("Email")

    password = st.text_input(
        "Password",
        type="password"
    )

    confirm_password = st.text_input(
        "Confirm Password",
        type="password"
    )

    col1, col2 = st.columns(2)

    with col1:

        if st.button("Create Account"):

            if password != confirm_password:
                st.error("Passwords do not match.")
                return

            db = SessionLocal()

            success, message = register_user(
                db=db,
                email=email,
                password=password,
            )

            db.close()

            if success:
                st.success(message)

                st.session_state.current_page = "login"

                st.rerun()

            else:
                st.error(message)

    with col2:

        if st.button("Back to Login"):

            st.session_state.current_page = "login"

            st.rerun()