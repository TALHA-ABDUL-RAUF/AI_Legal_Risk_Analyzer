# auth/register.py

from sqlalchemy.orm import Session

from database.models import User
from auth.password import hash_password


def register_user(
    db: Session,
    email: str,
    password: str,
    role: str = "user",
):
    """
    Register a new user.
    """

    # Check if email already exists
    existing_user = db.query(User).filter(User.email == email).first()

    if existing_user:
        return False, "Email already registered."

    # Hash password
    hashed_password = hash_password(password)

    # Create user
    new_user = User(
        email=email,
        password_hash=hashed_password,
        role=role,
    )

    # Save to database
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return True, "User registered successfully."