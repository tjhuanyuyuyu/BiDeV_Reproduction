# modules/decomposer.py
from bidev.llm_wrappers import DashScopeClient
from typing import List

class Decomposer:
    def __init__(self):
        self.llm = DashScopeClient()

    def decompose(self, claim: str) -> List[str]:
        prompt = (
            "You are given a complex claim that may involve referential "
            "or comparative relationships. Decompose it into a list of short, "
            "independent sub-claims using simple logic.\n\n"
            f"Claim: {claim}\n"
            "Sub-claims (one per line):"
        )
        response = self.llm.chat("", prompt)
        return [line.strip() for line in response.split("\n") if line.strip()]
