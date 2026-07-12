from sqlalchemy.orm import Session

from database.models import Document

from database.models import AnalysisResult

from sqlalchemy import func

def create_document(
    db: Session,
    user_id: int,
    file_name: str,
    file_path: str,
):
    """
    Create a new document record.
    """

    document = Document(
        user_id=user_id,
        file_name=file_name,
        file_path=file_path,
    )

    db.add(document)

    db.commit()

    db.refresh(document)

    return document

def create_analysis(
    db,
    document_id,
    question,
    answer,
):

    analysis = AnalysisResult(

        document_id=document_id,

        question=question,

        answer=answer,

    )

    db.add(analysis)

    db.commit()

    db.refresh(analysis)

    return analysis

def get_analysis_by_document(
    db,
    document_id,
):

    return (

        db.query(AnalysisResult)

        .filter(
            AnalysisResult.document_id == document_id
        )

        .order_by(
            AnalysisResult.created_at.desc()
        )

        .all()

    )

def get_document(
    db: Session,
    document_id: int,
):
    """
    Get a document by its ID.
    """

    return (
        db.query(Document)
        .filter(Document.id == document_id)
        .first()
    )


def get_user_documents(
    db: Session,
    user_id: int,
):
    """
    Get all documents uploaded by a user.
    """

    return (
        db.query(Document)
        .filter(Document.user_id == user_id)
        .all()
    )


def delete_document(
    db: Session,
    document_id: int,
):
    """
    Delete a document.
    """

    document = get_document(db, document_id)

    if document is None:
        return False

    db.delete(document)

    db.commit()

    return True


def total_documents(db, user_id):
    return (
        db.query(Document)
        .filter(Document.user_id == user_id)
        .count()
    )


def total_analysis(db, user_id):
    return (
        db.query(AnalysisResult)
        .join(Document)
        .filter(Document.user_id == user_id)
        .count()
    )