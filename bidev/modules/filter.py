# modules/filter.py
from typing import List
from bidev.llm_wrappers import DashScopeClient

class Filter:
    def __init__(self):
        self.llm = DashScopeClient()

    def filter_paragraphs(self, evidences: List[str], question_or_claim: str) -> List[str]:
        final_paragraphs = []

        for doc in evidences:
            prompt = (
                "You are a domain expert. Given a question or a factual claim and a long retrieved piece of evidence text, "
                "your task is to filter out only those parts of the evidence that are absolutely and definitively unrelated to the given question or claim. "
                "Please follow the instructions below with extreme caution:\n\n"
                "1. Carefully read the question or claim and identify parts of the evidence that are similar or potentially relevant in meaning. Retain these parts.\n"
                "2. For any part of the evidence that appears potentially relevant, or whose relevance you are uncertain about, retain it.\n"
                "3. Only remove a part of the evidence if you are absolutely certain that it is completely unrelated and dissimilar to the question or claim.\n"
                "4. Be extremely cautious in filtering — do not remove anything that might possibly contribute to understanding or verifying the question or claim.\n\n"               
                "Return the final filtered evidence text only.  \n\n"               
                f"Question or Claim:\n{question_or_claim}\n\n"
                f"Evidence:\n{doc}\n\n"
            )

            response = self.llm.chat("", prompt)

            if response.strip():
                final_paragraphs.extend([
                    para.strip() for para in response.strip().split("\n") if para.strip()
                ])

        return final_paragraphs
