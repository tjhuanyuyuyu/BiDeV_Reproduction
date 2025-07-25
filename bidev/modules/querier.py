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
            "If the question is 'no question', respond with 'no answer'.\n"
            "Otherwise, answer the question directly and concisely.\n"
            "If the context contains redundant or distracting information, you may ignore it and focus only on the core facts.\n"
            "Do not add any extra information beyond what is necessary to answer the question.\n\n"
            "Answer with a single factual sentence:"
            "Here are some examples:\n"
            "1. Question: no question\n"
            "   Answer: no answer\n"
            "2. Question: Who is the writer of the novel Horizon?\n"
            "   Answer: Lois McMaster Bujold.\n"
            "3. Question: Where is the area renamed 'Northland' in Stone Spring located?\n"
            "   Answer: Doggerland.\n"
            "4. Question: What is the specific location of Norris Dam State Park within Anderson County and Campbell County, Tennessee?\n"
            "   Answer: Along the shores of Norris Lake.\n\n"
            f"Context:\n{context}\n\n"
            f"Question: {question}\n"
            "Answer:"
        )
        return self.llm.chat("", prompt)


# “您是一位能够掌握背景知识的智能助手。\n”
# “您的任务是严格根据提供的证据回答以下问题。\n”
# “请仅使用上下文中明确陈述的信息。请勿进行假设。\n\n”
# f“上下文：\n{context}\n\n”
# f“问题：{question}\n”
# “请用一个事实句子回答：”
