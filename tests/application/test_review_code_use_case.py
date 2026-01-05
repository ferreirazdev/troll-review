from domain.ports import LLMClient
from application.usecases.review_code import ReviewCodeUseCase


class FakeLLMClient(LLMClient):
    def review_code(self, prompt: str) -> str:
        return "REVIEW RESULT"


def test_review_code_use_case_calls_llm():
    llm = FakeLLMClient() 
    use_case = ReviewCodeUseCase(llm)

    result = use_case.execute("print('hello')")

    assert result == "REVIEW RESULT"


def test_prompt_contains_code_and_instructions():
    captured_prompt = {}

    class SpyLLMClient(LLMClient):
        def review_code(self, prompt: str) -> str:
            captured_prompt["value"] = prompt
            return "OK"

    use_case = ReviewCodeUseCase(SpyLLMClient())
    use_case.execute("x = 1")

    assert "x = 1" in captured_prompt["value"]
    assert "Review" in captured_prompt["value"]
