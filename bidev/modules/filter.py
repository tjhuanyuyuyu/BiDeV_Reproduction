# modules/filter.py
from bidev.llm_wrappers import DashScopeClient
from typing import List

class Filter:
    def __init__(self):
        self.llm = DashScopeClient()

    def filter_paragraphs(self, paragraphs: List[str], question: str) -> List[str]:
        filtered = []
        for para in paragraphs:
            prompt = (
                "You are given a question and a paragraph. Determine whether the paragraph "
                "is relevant for answering the question. If it is, respond 'Yes'. Otherwise, respond 'No'.\n\n"
                f"Question: {question}\n"
                f"Paragraph: {para}\n"
                "Relevant?"
            )
            answer = self.llm.chat("", prompt)
            if "yes" in answer.lower():
                filtered.append(para)
        return filtered
