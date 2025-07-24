# modules/rewriter.py
from bidev.llm_wrappers import DashScopeClient

class Rewriter:
    def __init__(self):
        self.llm = DashScopeClient()

    def rewrite(self, claim: str, question: str, answer: str) -> str:
        prompt = (
            "You are given a claim, a clarifying question about it, "
            "and an answer to that question. Revise the original claim "
            "to explicitly include the missing information.\n\n"
            f"Claim: {claim}\n"
            f"Question: {question}\n"
            f"Answer: {answer}\n"
            "Rewritten Claim:"
        )
        return self.llm.chat("", prompt)
