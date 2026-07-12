import requests


class OllamaClient:

    def __init__(
        self,
        model: str = "llama3:8b",
        host: str = "http://localhost:11434",
    ):
        self.model = model
        self.url = f"{host}/api/generate"

    def generate(
        self,
        prompt: str,
        temperature: float = 0.2,
    ) -> str:

        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": False,
            "options": {
                "temperature": temperature,
            },
        }

        try:

            response = requests.post(
                self.url,
                json=payload,
                timeout=120,
            )

            response.raise_for_status()

            return response.json()["response"]

        except Exception as e:

            return f"Ollama Error: {e}"