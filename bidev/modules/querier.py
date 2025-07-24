from bidev.llm_wrappers import DashScopeClient
from typing import List

class Querier:
    def __init__(self):
        self.llm = DashScopeClient()

    def answer(self, question: str, filtered_evidence: List[str]) -> str:
        """
        参数：
        - question: 来自 Perceptor 的 q_i，提出关于 claim 的具体问题
        - filtered_evidence: 由 Filter 模块输出的 e_i*，与 question 相关的上下文信息

        返回：
        - 回答 a_i
        """
        context = "\n".join(filtered_evidence)
        prompt = (
            "You are an intelligent assistant with access to background knowledge.\n"
            "Your task is to answer the following question based strictly on the provided evidence.\n"
            "Only use the information that is clearly stated in the context. Do not make assumptions.\n\n"
            f"Context:\n{context}\n\n"
            f"Question: {question}\n"
            "Answer with a single factual sentence.Do not expand on irrelevant information in your answer:"
        )
        return self.llm.chat("", prompt)


# “您是一位能够掌握背景知识的智能助手。\n”
# “您的任务是严格根据提供的证据回答以下问题。\n”
# “请仅使用上下文中明确陈述的信息。请勿进行假设。\n\n”
# f“上下文：\n{context}\n\n”
# f“问题：{question}\n”
# “请用一个事实句子回答：”
