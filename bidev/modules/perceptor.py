# modules/perceptor.py
from bidev.llm_wrappers import DashScopeClient
class Perceptor:
    def __init__(self):
        self.llm = DashScopeClient()

    def detect_latent(self, claim: str) -> str:
        prompt = (
            "You are a reasoning assistant. Identify unresolved entities "
            "or missing attributes in the following claim, then output ONE "
            "question that would make the claim explicit.\n\n"
            f"Claim: {claim}\n"
            "Your Question:"
        )
        return self.llm.chat("", prompt)
