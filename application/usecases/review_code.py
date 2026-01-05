class ReviewCodeUseCase:
    def __init__(self, llm_client):
        self.llm_client = llm_client

    def execute(self, code: str) -> str:
        prompt = f"""
        You are a senior backend engineer.
        Review the following code.
        Provide:
        - Summary
        - Issues
        - Suggestions

        Code:
        {code}
        """
        return self.llm_client.review_code(prompt)
