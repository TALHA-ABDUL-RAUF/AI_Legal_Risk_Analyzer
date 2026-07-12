from sqlalchemy.orm import Session

from database.models import User
from auth.password import verify_password


def login_user(
    db: Session,
    email: str,
    password: str,
):
    """
    Authenticate a user.
    """

    user = db.query(User).filter(User.email == email).first()

    if not user:
        return False, "User not found.", None

    if not verify_password(password, user.password_hash):
        return False, "Invalid password.", None

    return True, "Login successful.", user