# modules/checker.py
from typing import List, Optional
from bidev.llm_wrappers import DashScopeClient
from bidev.retriever import BM25Retriever

class Checker:
    def __init__(self, wiki_dir: str = None):
        self.llm = DashScopeClient()
        self.retr = BM25Retriever(wiki_dir) if wiki_dir else None

    def verify(self, sub_claim: str, evidences: Optional[List[str]] = None) -> str:
        if evidences is None:
            if self.retr is None:
                raise ValueError("No evidence provided and no retriever available.")
            evidences = self.retr.query(sub_claim, k=5)

        joined = "\n".join(evidences)
        prompt = (
            f"Context:\n{joined}\n\n"
            f"Claim: {sub_claim}\n"
            "Is this claim supported or refuted by the context? Answer with 'Support' or 'Refute'."
        )
        return self.llm.chat("", prompt)
