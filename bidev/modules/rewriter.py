# modules/rewriter.py
from bidev.llm_wrappers import DashScopeClient

class Rewriter:
    def __init__(self):
        self.llm = DashScopeClient()

    def rewrite(self, claim: str, question: str, answer: str) -> str:
        # prompt，BiDeV 论文中的 Mr(c_{i-1}, q_i, a_i)定义
        prompt = (
            "You are an expert rewriting agent.\n"
            "Your goal is to revise a complex claim using external background knowledge.\n"
            "You are provided with:\n"
            "- The original claim that may contain latent information.\n"
            "- A clarifying question identifying one latent information of the claim.\n"
            "- A precise answer that resolves this latent information.\n\n"
            "Step-by-step, please:\n"
            "0. If the question does not contain unresolved entities and undetermined attributes, leave the original sentence unchanged.\n"
            "1. Identify which part(s) of the claim are directly or indirectly related to the question.\n"
            "2. Replace or update that part using the answer in a coherent, explicit, and fluent way.\n"
            "3. Do not alter the original meaning of the claim; preserve its original intent while adding the missing information.\n\n"
            "Write only the final revised claim.Do not \n\n"
            f"Claim: {claim}\n"
            f"Question: {question}\n"
            f"Answer: {answer}\n"
            "Rewritten Claim:"
        )
        return self.llm.chat("", prompt)

# “您是一位专业的改写代理。\n”
# “您的目标是利用外部背景知识修改一项复杂的权利要求。\n”
# “您将获得：\n”
# “- 可能包含潜在信息的原始权利要求。\n”
# “- 一个澄清问题，用于识别权利要求中的一个潜在信息。\n”
# “- 一个能够解决该潜在信息的精确答案。\n\n”
# “请分步说明：\n”
# “1. 确定权利要求中哪些部分与问题直接或间接相关。\n”
# “2. 使用答案，以连贯、明确和流畅的方式替换或更新该部分。\n”
# “3. 不要改变权利要求的原始含义；在添加缺失信息的同时保留其原始意图。\n\n”
# “只写最终修改后的权利要求。\n\n”
# f“权利要求：{claim}\n”
# f“问题：{question}\n”
# f“答案：{answer}\n”
# “改写的权利要求：”