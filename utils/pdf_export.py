from pathlib import Path

from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

REPORT_DIR = Path("reports")
REPORT_DIR.mkdir(exist_ok=True)


def export_pdf(text, filename):

    pdf_path = REPORT_DIR / filename

    doc = SimpleDocTemplate(str(pdf_path))

    styles = getSampleStyleSheet()

    story = []

    for line in text.split("\n"):

        story.append(
            Paragraph(line, styles["BodyText"])
        )

    doc.build(story)

    return str(pdf_path)