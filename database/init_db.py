# database/init_db.py

from database.database import Base, engine

# Import models so SQLAlchemy knows about them
from database.models import User, Document, AnalysisResult


def init_database():
    Base.metadata.create_all(bind=engine)
    print("Database initialized successfully!")


if __name__ == "__main__":
    init_database()