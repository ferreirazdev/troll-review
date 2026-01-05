from application.usecases.review_code import ReviewCodeUseCase
from infrastructure.llm.gemini_client import GeminiLLMClient
import os
from pathlib import Path

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass  # python-dotenv not installed, skip


def build_review_code_use_case():
    """Build review code use case using API key or service account."""
    # Try GEMINI_API_KEY environment variable first
    api_key = os.getenv("GEMINI_API_KEY")
    if api_key:
        api_key = api_key.strip()
        # Check if it's a file path pointing to service account JSON
        json_path = Path(api_key)
        if json_path.suffix == ".json" and json_path.exists():
            # Use the JSON file as service account credentials
            llm = GeminiLLMClient(credentials=str(json_path))
            return ReviewCodeUseCase(llm)
        elif api_key:
            # It's an actual API key string
            llm = GeminiLLMClient(api_key=api_key)
            return ReviewCodeUseCase(llm)

    # Try to find service account JSON file in project root
    project_root = Path(__file__).parent
    json_files = list(project_root.glob("*.json"))
    for json_file in json_files:
        # Skip common non-auth JSON files
        if (
            json_file.name.startswith("package")
            or json_file.name.startswith("tsconfig")
        ):
            continue
        try:
            # Try to use this JSON file as service account
            llm = GeminiLLMClient(credentials=str(json_file))
            return ReviewCodeUseCase(llm)
        except Exception:
            continue

    # No valid configuration found
    raise ValueError(
        "Either GEMINI_API_KEY environment variable (API key or JSON path) "
        "or a valid service account JSON file in the project root is required"
    )
