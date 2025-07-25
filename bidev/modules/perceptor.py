# modules/perceptor.py
from bidev.llm_wrappers import DashScopeClient

class Perceptor:
    def __init__(self):
        self.llm = DashScopeClient()

    def detect_latent(self, claim: str) -> str:
        # High-quality prompt aligned with BiDeV's Perceptor definition
        prompt = (
            "You are an expert reasoning assistant.\n"
            "Your task is to analyze the following claim and identify any latent information that needs clarification.\n"
            "Latent information falls into one of two types:\n"
            "1. Unresolved Entity: a person, object, or event mentioned without sufficient specificity (e.g., 'the writer').\n"
            "2. Undetermined Attribute: a missing detail about a known entity (e.g., birth date, nationality, or role).\n\n"
            "Please identify these two types of latent information and generate ONE precise and concrete question, the answer to which should make the claim more explicit. \n"
            "When generating questions, avoid using vague or yes/no questions. Focus on factual clarification.\n\n"
            "**If multiple latent pieces of information exist, choose the one with the highest priority.The specific priority determination rules are as follows:**\n"
            "1. First, prefer unresolved entities over undetermined attributes.\n"
            "2. Among entities, prioritize those that are central to the claim,and subjects take precedence over objects and auxiliary components.\n"
            "3. If all entities are resolved, then select the most critical missing attribute.\n\n"
            "Output only one question, not an analysis, involving only one unresolved entity or undetermined attribute.\n"
            f"Claim: {claim}\n\n"
            "Your question:"
        )
        return self.llm.chat("", prompt)



# 你是一位专业的推理助手。\n"
# 你的任务是分析以下断言并找出任何需要澄清的潜在信息。\n"
# 潜在信息分为以下两种类型：\n"
# 1. 未解析实体：提及的人物、物体或事件缺乏足够的特异性（例如，“某本书的作者”）。\n"
# 2. 未确定属性：已知实体缺失的细节（例如，出生日期、国籍或角色）。\n\n"
# 请识别这两种类型的潜在信息，并提出一个精确而具体的问题，该问题的答案应使断言更加明确。\n"
# # 请提出一个精确而具体的问题，如果回答该问题，将使断言更加明确。\n"
# 提出问题时，避免使用模糊或“是/否”问题。专注于事实澄清。\n\n"
# **如果存在多条潜在信息，请选择优先级最高的一条。具体的优先级确定规则如下如下：**\n"
# "1. 首先，优先选择未解析实体，而非未确定的属性。\n"
# "2. 在实体中，优先考虑那些对主张至关重要的实体，主语优先于宾语和辅助成分。\n"
# "3. 如果所有实体均已解析，则选择最关键的缺失属性。\n\n"
