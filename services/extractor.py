import fitz
from docx import Document
from pathlib import Path


class TextExtractor:

    @staticmethod
    def extract_pdf(file_path: str) -> str:

        text = ""

        pdf = fitz.open(file_path)

        for page in pdf:
            text += page.get_text()

        pdf.close()

        return text.strip()


    @staticmethod
    def extract_docx(file_path: str) -> str:

        document = Document(file_path)

        text = "\n".join(
            paragraph.text
            for paragraph in document.paragraphs
        )

        return text.strip()


    @staticmethod
    def extract_txt(file_path: str) -> str:

        with open(file_path, "r", encoding="utf-8") as file:
            return file.read().strip()


    @staticmethod
    def extract_text(file_path: str) -> str:

        extension = Path(file_path).suffix.lower()

        if extension == ".pdf":
            return TextExtractor.extract_pdf(file_path)

        elif extension == ".docx":
            return TextExtractor.extract_docx(file_path)

        elif extension == ".txt":
            return TextExtractor.extract_txt(file_path)

        else:
            raise ValueError("Unsupported document format.")