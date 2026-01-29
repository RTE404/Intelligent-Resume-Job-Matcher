import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv(dotenv_path=".env")


class LLMClient:
    """
    Groq LLM client wrapper.
    """

    def __init__(self, model: str = "llama-3.1-8b-instant"):
        self.client = Groq(api_key=os.getenv("GROQ_API_KEY"))
        self.model = model

    def generate(self, prompt: str) -> str:
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "You are a precise technical evaluator."},
                {"role": "user", "content": prompt}
            ],
            temperature=0
        )

        return response.choices[0].message.content
