from pathlib import Path
import mimetypes

# Allowed MIME types
ALLOWED_MIME_TYPES = {
    "application/pdf",
    "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
    "text/plain",
}

# Allowed extensions
ALLOWED_EXTENSIONS = {
    ".pdf",
    ".docx",
    ".txt",
}

# Maximum upload size (10 MB)
MAX_FILE_SIZE = 10 * 1024 * 1024


def validate_file(file_path: str):
    """
    Validate file existence, extension, MIME type and size.

    Returns:
        (True, "Valid file")
        (False, "Reason")
    """

    path = Path(file_path)

    if not path.exists():
        return False, "File does not exist."

    if path.suffix.lower() not in ALLOWED_EXTENSIONS:
        return False, "Unsupported file extension."

    mime_type, _ = mimetypes.guess_type(path)

    if mime_type not in ALLOWED_MIME_TYPES:
        return False, "Unsupported MIME type."

    if path.stat().st_size > MAX_FILE_SIZE:
        return False, "File exceeds maximum size."

    return True, "File is valid."