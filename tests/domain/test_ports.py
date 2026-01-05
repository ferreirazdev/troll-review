from domain.ports import LLMClient


def test_llm_client_is_abstract():
    assert hasattr(LLMClient, "review_code")
