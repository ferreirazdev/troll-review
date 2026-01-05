from domain.ports import LLMClient


class OpenAILLMClient(LLMClient):
    def __init__(self, client):
        self.client = client

    def review_code(self, prompt: str) -> str:
        response = self.client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[{"role": "user", "content": prompt}],
        )
        return response.choices[0].message.content
