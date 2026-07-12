# database/database.py

import os

from dotenv import load_dotenv

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


# -------------------------------------------------
# Load environment variables from .env
# -------------------------------------------------

load_dotenv()


# -------------------------------------------------
# Read the database URL
# Example:
# sqlite:///database/app.db
# -------------------------------------------------

DATABASE_URL = os.getenv("DATABASE_URL")


# -------------------------------------------------
# Create the SQLAlchemy Engine
# -------------------------------------------------

engine = create_engine(
    DATABASE_URL,
    echo=False,
)


# -------------------------------------------------
# Create a Session Factory
# -------------------------------------------------

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)


# -------------------------------------------------
# Base class for all ORM models
# -------------------------------------------------

Base = declarative_base()


# -------------------------------------------------
# Database Session Generator
# -------------------------------------------------

def get_db():
    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()