from domain.ports import LLMClient
import google.genai as genai
from typing import Optional


class GeminiLLMClient(LLMClient):
    def __init__(
        self,
        api_key: Optional[str] = None,
        credentials: Optional[str] = None,
        model: str = "gemini-2.0-flash",
    ):
        if api_key:
            # Use API key with regular Gemini API
            api_key = api_key.strip()
            if not api_key:
                raise ValueError("API key cannot be empty")
            self.client = genai.Client(api_key=api_key)
        elif credentials:
            # Use service account with Vertex AI
            import json
            from google.oauth2 import service_account

            # Load project ID from JSON file
            with open(credentials) as f:
                service_account_info = json.load(f)
            project_id = service_account_info.get("project_id")

            # Create credentials with required scopes for Vertex AI
            creds = service_account.Credentials.from_service_account_file(
                credentials,
                scopes=["https://www.googleapis.com/auth/cloud-platform"],
            )
            self.client = genai.Client(
                vertexai=True, credentials=creds, project=project_id
            )
        else:
            raise ValueError("Either api_key or credentials must be provided")
        self.model = model

    def review_code(self, prompt: str) -> str:
        response = self.client.models.generate_content(
            model=self.model, contents=prompt
        )
        return response.text
