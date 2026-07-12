from services.semantic_search import SemanticSearch
from services.prompt_builder import PromptBuilder
from services.ollama_client import OllamaClient


class LegalAnalyzer:

    def __init__(
        self,
        semantic_search: SemanticSearch,
    ):

        self.semantic_search = semantic_search

        self.llm = OllamaClient()

    def analyze(
        self,
        question: str,
        document_id: str,
    ):

        results = self.semantic_search.search(
            question,
            document_id,
            top_k=3,
        )

        clauses = results["documents"][0]

        if len(clauses) == 0:

            return "No relevant clauses found."

        prompt = PromptBuilder.build(
            question,
            clauses,
        )

        answer = self.llm.generate(prompt)

        return answer