# auth/password.py

import bcrypt


def hash_password(password: str) -> str:
    """
    Convert a plain text password into a secure bcrypt hash.
    """

    password_bytes = password.encode("utf-8")

    salt = bcrypt.gensalt()

    hashed_password = bcrypt.hashpw(password_bytes, salt)

    return hashed_password.decode("utf-8")


def verify_password(password: str, hashed_password: str) -> bool:
    """
    Verify whether a plain password matches the stored bcrypt hash.
    """

    password_bytes = password.encode("utf-8")

    hash_bytes = hashed_password.encode("utf-8")

    return bcrypt.checkpw(password_bytes, hash_bytes)