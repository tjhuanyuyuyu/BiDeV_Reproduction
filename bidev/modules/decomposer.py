# modules/decomposer.py
from bidev.llm_wrappers import DashScopeClient
from typing import List

class Decomposer:
    def __init__(self):
        self.llm = DashScopeClient()

    def decompose(self, claim: str) -> List[str]:
        # 高质量 prompt，符合 BiDeV 论文公式 sc = Md(C*)
        prompt = (
            "You are a decomposition agent for complex factual claims.\n"
            "Your task is to split the given claim into multiple short, factual sub-claims.\n\n"
            "The input claim may contain:\n"
            "- Referential relations (e.g., 'she' refers to a previously mentioned entity).\n"
            "- Comparative relations (e.g., comparing birth dates, heights, or scores).\n\n"
            "Please follow these steps:\n"
            "1. Replace any vague pronouns or references with the actual explicit entities in the original context if possible.\n"
            "2. Resolve comparisons into independent facts using determined attributes.\n"
            "3. Decompose the final claim into simple declarative sub-claims that are logically independent.\n\n"
            f"Claim: {claim}\n\n"
            "Output each sub-claim on a new line:\n"
        )

        response = self.llm.chat("", prompt)
        return [line.strip() for line in response.split("\n") if line.strip()]

# 你是一名复杂事实性主张的分解代理。\n"
# "你的任务是将给定的主张拆分为多个简短的事实性子主张。\n\n"
# "输入主张可能包含：\n"
# "- 指称关系（例如，“她”指代先前提到的实体）。\n"
# "- 比较关系（例如，比较出生日期、身高或分数）。\n\n"
# "请遵循以下步骤：\n"
# "1. 用上下文中实际的明确实体替换任何模糊代词或指称。\n"
# "2. 使用确定的属性将比较解析为独立的事实。\n"
# "3. 将最终主张分解为逻辑上独立的简单陈述性子主张。\n\n"
# f"主张：{主张}\n\n"
# "将每个子主张另起一行输出：\n"