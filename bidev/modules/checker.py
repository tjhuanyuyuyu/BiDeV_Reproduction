# modules/checker.py
from typing import List
from bidev.llm_wrappers import DashScopeClient

class Checker:
    def __init__(self):
        self.llm = DashScopeClient()

    def verify(self, sub_claim: str, evidence: List[str]) -> str:
        context = "\n".join(evidence)
        prompt = (
            "You are a fact-checking assistant.\n"
            "Given the following claim and supporting evidence, your task is to determine whether the claim is factually correct based on the evidence.\n\n"
            f"Claim:\n{sub_claim}\n\n"
            f"Evidence:\n{context}\n\n"
            "Please check carefully and output only one of the following labels:\n"
            "- Support: if the evidence confirms that the claim is correct.\n"
            "- Refute: if the evidence shows the claim is false.\n\n"
            "Do not output explanation.\n"
            "Your answer (Support or Refute):"
        )
        result = self.llm.chat("", prompt).strip()
        return result



# 你是一名事实核查助理。\n"
# "给定以下主张及其支持证据，你的任务是根据证据判断该主张是否符合事实。\n\n"
# f"主张:\n{sub_claim}\n\n"
# f"证据:\n{context}\n\n"
# "请仔细检查并输出以下标签之一：\n"
# "- 支持：如果证据证实该主张正确。\n"
# "- 反驳：如果证据表明该主张错误。\n\n"