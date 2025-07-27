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
            "3. Decompose the final claim into simple declarative sub-claims that are logically independent.\n"
            "4. The combined meaning of all sub-claims should fully reconstruct the original claim.\n\n"
            "Examples:\n"
            "Example 1:\n"
            "Claim: Lois McMaster Bujold is American. She was younger than Bernard Malamud borned in 1914.\n"
            "Sub-claims:\n"
            "Lois McMaster Bujold is American.\n"
            "Lois McMaster Bujold was borned after 1914.\n"
            "Bernard Malamud was borned in 1914.\n\n"
            "Example 2:\n"
            "Claim: Derek Stephen Prince, known as the voice of \"Elgar\", voices Keitarō Urashima, the English character in the Manga Love Hina inspired by Keitaro Arima.\n"
            "Sub-claims:\n"
            "Derek Stephen Prince is known as the voice of \"Elgar\".\n"
            "Derek Stephen Prince voices Keitarō Urashima, an English character in the Manga Love Hina.\n"
            "Keitarō Urashima was inspired by Keitaro Arima.\n\n"
            "Example 3:\n"
            "Claim: Mikhail Gromov is a permanent faculty member at the school of Mathematics, located in New Jersey, where Eric Stark Maskin was a teacher. This mathematician was one of the developers of Systolic geometry.\n"
            "Sub-claims:\n"
            "Mikhail Gromov is a permanent faculty member at the school of Mathematics, located in New Jersey.\n"
            "Eric Stark Maskin was a teacher at the school of Mathematics in New Jersey.\n"
            "Mikhail Gromov was one of the developers of Systolic geometry.\n\n"
            f"Claim: {claim}\n\n"
            "Output each sub-claim on a new line:\n"
        )

        response = self.llm.chat("", prompt)
        return [line.strip() for line in response.split("\n") if line.strip()]
    

    def no_rewrite_decompose(self, claim: str, q_ans: str) -> List[str]:
        prompt = (
            "You are a decomposition agent for complex factual claims.\n"
            "Your task is to split the given claim into multiple short, factual sub-claims.\n"
            "Then simplify the sub-claims using the information provided in q_ans.\n\n"
            "The input claim may contain:\n"
            "- Referential relations (e.g., 'she' refers to a previously mentioned entity).\n"
            "- Comparative relations (e.g., comparing birth dates, heights, or scores).\n\n"
            "Please follow these steps:\n"
            "1. Replace any vague pronouns or references with the actual explicit entities in the original context if possible.\n"
            "2. Resolve comparisons into independent facts using determined attributes.\n"
            "3. Decompose the final claim into simple declarative sub-claims that are logically independent.\n"
            "4. The combined meaning of all sub-claims should fully reconstruct the original claim.\n\n"
            "Examples:\n"
            "Example 1:\n"
            "Claim: Lois McMaster Bujold is American. She was younger than Bernard Malamud borned in 1914.\n"
            "Sub-claims:\n"
            "Lois McMaster Bujold is American.\n"
            "Lois McMaster Bujold was borned after 1914.\n"
            "Bernard Malamud was borned in 1914.\n\n"
            "Example 2:\n"
            "Claim: Derek Stephen Prince, known as the voice of \"Elgar\", voices Keitarō Urashima, the English character in the Manga Love Hina inspired by Keitaro Arima.\n"
            "Sub-claims:\n"
            "Derek Stephen Prince is known as the voice of \"Elgar\".\n"
            "Derek Stephen Prince voices Keitarō Urashima, an English character in the Manga Love Hina.\n"
            "Keitarō Urashima was inspired by Keitaro Arima.\n\n"
            "Example 3:\n"
            "Claim: Mikhail Gromov is a permanent faculty member at the school of Mathematics, located in New Jersey, where Eric Stark Maskin was a teacher. This mathematician was one of the developers of Systolic geometry.\n"
            "Sub-claims:\n"
            "Mikhail Gromov is a permanent faculty member at the school of Mathematics, located in New Jersey.\n"
            "Eric Stark Maskin was a teacher at the school of Mathematics in New Jersey.\n"
            "Mikhail Gromov was one of the developers of Systolic geometry.\n\n"
            "You are also given a string q_ans: str in the format \"Q: <question> A: <answer>\".\n"
            "You may simplify or rewrite the sub-claims using the explicit knowledge in q_ans.If q_ans does not contain any useful information, simply output the sub-claims derived from the original claim without modification.\n\n"
            f"Claim: {claim}\n\n"
            f"q_ans：{q_ans}\n\n"
            "Output each sub-claim on a new line:\n"
        )

        response = self.llm.chat("", prompt)
        return [line.strip() for line in response.split("\n") if line.strip()]

