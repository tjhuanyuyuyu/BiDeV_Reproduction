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
            "Your rewriting task follows strict rules:\n"
            "1. If the question is 'no question' or the answer is 'no answer', do not modify the claim. Just output the original claim as-is.\n"
            "2. Otherwise, identify the specific part of the claim that corresponds to the unresolved entity or undetermined attribute mentioned in the question.\n"
            "3. Replace or update that part with the given answer in a coherent, explicit, and fluent way.\n"
            "4. Do not change or rephrase any other parts of the claim. Do not add new content, new sentences, or new entities.\n"
            "5. Your final output must be a new version of the original claim, modified only in the relevant part, with sentence structure and meaning completely preserved.\n\n"
            "Examples:\n"
            "Example 1:\n"
            "Claim: The former president of Peru, who took office in 2022, was removed from power.\n"
            "Question: Who was the president of Peru in 2022?\n"
            "Answer: Pedro Castillo\n"
            "Rewritten Claim: Pedro Castillo, the former president of Peru who took office in 2022, was removed from power.\n\n"
            "Example 2:\n"
            "Claim: The 2023 Nobel Prize in Literature was awarded to a French author known for their autofictional style.\n"
            "Question: Who won the 2023 Nobel Prize in Literature?\n"
            "Answer: Jon Fosse\n"
            "Rewritten Claim: The 2023 Nobel Prize in Literature was awarded to Jon Fosse, a French author known for their autofictional style.\n\n"
            "Example 3:\n"
            "Claim: The peace treaty signed in 1979 ended decades of conflict between Egypt and a neighboring country.\n"
            "Question: Which neighboring country did Egypt sign the peace treaty with in 1979?\n"
            "Answer: Israel\n"
            "Rewritten Claim: The peace treaty signed in 1979 ended decades of conflict between Egypt and Israel.\n\n"
            "Example 4:\n"
            "Claim: The song recorded by Fergie that was produced by Polow da Don and was followed by Life Goes On was M.I.L.F.\n"
            "Question: no question.\n"
            "Answer: no answer.\n"
            "Rewritten Claim: The song recorded by Fergie that was produced by Polow da Don and was followed by Life Goes On was M.I.L.F.\n\n"
            "Example 5 :\n"
            "Claim: The writer of the novel Horizon is American. She ywas younger than the author of Dubin's Lives.\n"
            "Question: Who is the writer of the novel Horizon?\n"
            "Answer: Lois McMaster Bujold.\n"
            "Rewritten Claim: Lois McMaster Bujold is American. She ywas younger than the author of Dubin's Lives.\n\n"
            "Example 6 :\n"
            "Claim: Substorm was described in qualitative terms by a scientist nominated for Nobel Prize seven times.\n"
            "Question:Who is the scientist nominated for Nobel Prize seven times?\n"
            "Answer: Kristian Birkeland.\n"
            "Rewritten Claim: Substorm was described in qualitative terms by Kristian Birkeland ，a scientist who was nominated for Nobel Prize seven times.\n\n"
            "Example 7 :\n"
            "Claim: The high-performance car that replaced the Ferrari Type F129 was itself replaced by the Ferrari F430. That car competed in the new Australian Nations Cup Championship in 2000.\n"
            "Question:What is the name of the high-performance car that replaced the Ferrari Type F129?\n"
            "Answer: The high-performance car that replaced the Ferrari Type F129 is the Ferrari 360.\n"
            "Rewritten Claim: The high-performance car that replaced the Ferrari Type F129 is the Ferrari 360,and it was replaced by he Ferrari F430. That car competed in the new Australian Nations Cup Championship in 2000.\n\n"
            f"Claim: {claim}\n"
            f"Question: {question}\n"
            f"Answer: {answer}\n"
            "Rewritten Claim:"
        )
        return self.llm.chat("", prompt)

