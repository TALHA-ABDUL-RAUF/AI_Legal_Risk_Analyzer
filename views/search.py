import streamlit as st

from auth.session import is_logged_in

from database.database import SessionLocal
from database.models import Document
from utils.pdf_export import export_pdf
from components.navigation import show_navigation
from services.model_manager import get_embedder
from services.vector_store import VectorStore
from services.semantic_search import SemanticSearch
from services.legal_analyzer import LegalAnalyzer
from database.crud import create_analysis

def show():

    # ----------------------------
    # Authentication Check
    # ----------------------------
    if not is_logged_in():
        st.warning("Please login first.")
        st.session_state.current_page = "login"
        st.rerun()

    st.title("🔎 Semantic Contract Search")
    show_navigation()

    # ----------------------------
    # Load User Documents
    # ----------------------------
    db = SessionLocal()

    documents = (
        db.query(Document)
        .filter(Document.user_id == st.session_state.user_id)
        .all()
    )

    if not documents:

        st.info("No uploaded documents found.")

        if st.button("Upload Document"):
            st.session_state.current_page = "upload"
            st.rerun()

        db.close()
        return

    # ----------------------------
    # Build Document Dictionary
    # ----------------------------
    document_names = {
        doc.file_name: doc.id
        for doc in documents
    }

    # ----------------------------
    # Select Document
    # ----------------------------
    document_list = list(document_names.keys())

    if len(document_list) == 0:
        st.warning("No documents found.")
        db.close()
        return

    default_index = 0

    selected_document = st.session_state.get("selected_document")

    if selected_document is not None:

        matching_indexes = [
            i for i, doc in enumerate(documents)
            if doc.id == selected_document
        ]

        if matching_indexes:
            default_index = matching_indexes[0]

    # Safety check
    default_index = min(default_index, len(document_list) - 1)

    selected = st.selectbox(
        "Select Document",
        options=document_list,
        index=default_index,
    )

    document_id = document_names[selected]

    # Remember current selection
    st.session_state.selected_document = document_id

    # ----------------------------
    # User Question
    # ----------------------------
    question = st.text_input(
        "Ask a legal question",
        placeholder="What are the termination conditions?"
    )

    # ----------------------------
    # Initialize AI Components
    # ----------------------------
    embedder = get_embedder()

    vector_store = VectorStore()

    semantic = SemanticSearch(
        embedder,
        vector_store,
    )

    analyzer = LegalAnalyzer(
        semantic,
    )

    # ----------------------------
    # Analyze Button
    # ----------------------------
    if st.button("Analyze Contract"):

        if not question.strip():
            st.warning("Please enter a question.")

        else:

            with st.spinner("Analyzing contract..."):

                # ----------------------------
                # Semantic Search
                # ----------------------------
                results = semantic.search(
                    question=question,
                    document_id=f"doc_{document_id}",
                    top_k=3,
                )

                clauses = results["documents"][0]
                distances = results["distances"][0]

                st.subheader("📑 Retrieved Clauses")

                if len(clauses) == 0:

                    st.error("No relevant clauses found.")

                else:

                    for i, clause in enumerate(clauses):

                        distance = round(distances[i], 4)

                        with st.expander(
                            f"Clause {i+1} | Distance: {distance}"
                        ):
                            st.write(clause)

                    # ----------------------------
                    # AI Legal Analysis
                    # ----------------------------
                    answer = analyzer.analyze(
                        question=question,
                        document_id=f"doc_{document_id}",
                    )

                    st.divider()

                    st.subheader("🤖 AI Legal Analysis")

                    st.markdown(answer)

                    # ----------------------------
                    # Confidence Indicator
                    # ----------------------------
                    if "Confidence: High" in answer:
                        st.success("Confidence : High")
                    elif "Confidence: Medium" in answer:
                        st.warning("Confidence : Medium")
                    else:
                        st.error("Confidence : Low")

                    create_analysis(

                        db=db,

                        document_id=document_id,

                        question=question,

                        answer=answer,

                    )

                    # ----------------------------
                    # Post-Analysis Actions
                    # ----------------------------
                    col1, col2 = st.columns(2)

                    with col1:

                        if st.button("Ask Another Question"):

                            st.rerun()

                    with col2:

                        if st.button("View History"):

                            st.session_state.current_page = "history"

                            st.rerun()

                    # ----------------------------
                    # PDF Export
                    # ----------------------------
                    pdf = export_pdf(
                        answer,
                        "analysis.pdf"
                    )

                    with open(pdf, "rb") as file:

                        st.download_button(
                            "Download Report",
                            file,
                            file_name="Legal_Analysis.pdf",
                            mime="application/pdf",
                        )

    db.close()