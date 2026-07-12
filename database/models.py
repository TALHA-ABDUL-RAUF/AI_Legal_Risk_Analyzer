from datetime import datetime

from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    ForeignKey,
    JSON,
    Text,
)

from sqlalchemy.orm import relationship

from database.database import Base


# =====================================================
# USER
# =====================================================

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    email = Column(
        String,
        unique=True,
        nullable=False,
    )

    password_hash = Column(
        String,
        nullable=False,
    )

    role = Column(
        String,
        default="user",
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow,
    )

    documents = relationship(
        "Document",
        back_populates="user",
        cascade="all, delete-orphan",
    )


# =====================================================
# DOCUMENT
# =====================================================

class Document(Base):
    __tablename__ = "documents"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False,
    )

    file_name = Column(
        String,
        nullable=False,
    )

    file_path = Column(
        String,
        nullable=False,
    )

    upload_date = Column(
        DateTime,
        default=datetime.utcnow,
    )

    user = relationship(
        "User",
        back_populates="documents",
    )

    analysis_results = relationship(
        "AnalysisResult",
        back_populates="document",
        cascade="all, delete-orphan",
    )


# =====================================================
# ANALYSIS RESULT
# =====================================================

class AnalysisResult(Base):
    __tablename__ = "analysis_results"

    id = Column(Integer, primary_key=True, index=True)

    document_id = Column(
        Integer,
        ForeignKey("documents.id"),
        nullable=False,
    )

    question = Column(
        Text,
        nullable=False,
    )

    answer = Column(
        Text,
        nullable=False,
    )

    contract_type = Column(
        String,
        nullable=True,
    )

    extracted_metadata = Column(
        JSON,
        nullable=True,
    )

    risks_json = Column(
        JSON,
        nullable=True,
    )

    summary_json = Column(
        JSON,
        nullable=True,
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow,
    )

    document = relationship(
        "Document",
        back_populates="analysis_results",
    )