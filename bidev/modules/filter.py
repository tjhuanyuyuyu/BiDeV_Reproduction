# modules/filter.py
from typing import List
from bidev.llm_wrappers import DashScopeClient

class Filter:
    def __init__(self):
        self.llm = DashScopeClient()

    def filter_paragraphs(self, evidences: List[str], question_or_claim: str) -> List[str]:
        """
        使用 LLM 对每条 evidence（：
        1. 由模型判断如何划分为多个段落；
        2. 模型判断哪些段落与 question/sub-claim 有关；
        3. 返回所有相关段落组成的列表。
        """
        final_paragraphs = []

        for doc in evidences:
            prompt = (
                "You are a helpful assistant for fact verification. Given a question or a claim and a long piece of retrieved evidence text, your job is to select the most relevant content to help answer the question or judge the claim.Please follow the steps below:\n"
                "Step 1: Carefully segment the evidence into distinct numbered paragraphs. Each paragraph should contain a complete topic or idea.\n"
                "Step 2: For each paragraph, evaluate whether it is relevant to the question or the claim. A paragraph is considered relevant if it either (1) directly supports or challenges the question or the claim, or (2) contains helpful background information that contributes to understanding or verifying the question or judging the claim. "
                "Step 3: Eliminate paragraphs that are not relevant to the question or claim\n"
                "Step 4: Return ONLY the relevant paragraphs as plain text. Do NOT include paragraph numbers or explanations. Keep only the final filtered content.\n"
                f"Question:\n{question_or_claim}\n\n"
                f"Evidence:\n{doc}\n\n"
            )

            response = self.llm.chat("", prompt)

            if response.strip():
                final_paragraphs.extend([
                    para.strip() for para in response.strip().split("\n") if para.strip()
                ])

        return final_paragraphs
