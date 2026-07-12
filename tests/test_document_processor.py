from services.document_processor import DocumentProcessor

processor = DocumentProcessor()

result = processor.process_document(
    file_path="tests/sample.pdf",
    document_id="contract_001",
)

print(result)