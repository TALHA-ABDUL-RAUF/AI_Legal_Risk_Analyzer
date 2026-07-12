import streamlit as st

from database.database import SessionLocal
from database.crud import create_document

from services.document_processor import DocumentProcessor

from utils.file_manager import save_uploaded_file
from components.navigation import show_navigation

def show():

    st.title("📄 Upload Contract")
    show_navigation()
    uploaded_file = st.file_uploader(
        "Choose a contract",
        type=["pdf", "docx", "txt"],
    )

    if uploaded_file is None:
        return

    if st.button("Process Document"):

        with st.spinner("Processing..."):

            # Save file
            file_path = save_uploaded_file(uploaded_file)

            # Database session
            db = SessionLocal()

            try:

                document = create_document(
                    db=db,
                    user_id=st.session_state.user_id,
                    file_name=uploaded_file.name,
                    file_path=file_path,
                )

                processor = DocumentProcessor()

                result = processor.process_document(
                    file_path=file_path,
                    document_id=f"doc_{document.id}",
                )

                if result["success"]:

                    st.success("✅ Document processed successfully!")

                    st.write(f"Document ID: {document.id}")

                    st.write(f"Chunks: {result['chunks']}")

                    st.session_state.selected_document = document.id

                    st.toast("Document indexed successfully.")

                    st.session_state.current_page = "search"

                    st.rerun()
                else:

                    st.error(result["message"])

            finally:

                db.close()