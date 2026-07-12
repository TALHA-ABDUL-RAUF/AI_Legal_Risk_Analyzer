from database.database import SessionLocal

from database.crud import (
    create_document,
    get_document,
    get_user_documents,
)

db = SessionLocal()

document = create_document(
    db=db,
    user_id=1,
    file_name="sample.pdf",
    file_path="uploads/sample.pdf",
)

print("Created")

print(document.id)

doc = get_document(
    db,
    document.id,
)

print(doc.file_name)

docs = get_user_documents(
    db,
    1,
)

print(len(docs))

db.close()