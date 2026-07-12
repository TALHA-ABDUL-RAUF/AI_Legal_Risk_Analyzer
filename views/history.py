import streamlit as st

from auth.session import is_logged_in

from database.database import SessionLocal

from database.crud import get_analysis_by_document

from database.models import Document

from components.navigation import show_navigation
def show():

    if not is_logged_in():

        st.warning("Please login first.")

        st.session_state.current_page = "login"

        st.rerun()
    show_navigation()
    st.title("📜 Analysis History")

    db = SessionLocal()

    documents = (

        db.query(Document)

        .filter(
            Document.user_id == st.session_state.user_id
        )

        .all()

    )

    if len(documents) == 0:

        st.info("No uploaded documents.")

        db.close()

        return

    for doc in documents:

        st.subheader(doc.file_name)

        history = get_analysis_by_document(
            db,
            doc.id,
        )

        if len(history) == 0:

            st.write("No analyses.")

            continue

        for item in history:

            with st.expander(item.question):

                st.markdown(item.answer)

                st.caption(
                    item.created_at.strftime(
                            "%d %b %Y %I:%M %p"
                    )
                )

    db.close()