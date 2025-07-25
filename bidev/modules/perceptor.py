# modules/perceptor.py
from bidev.llm_wrappers import DashScopeClient

class Perceptor:
    def __init__(self):
        self.llm = DashScopeClient()

    def detect_latent(self, claim: str) -> str:
        # High-quality prompt aligned with BiDeV's Perceptor definition
        prompt = (
            "You are an expert reasoning assistant.\n"
            "Your task is to determine whether the following claim is a **simple claim** or a **complex claim**, and respond accordingly by either giving a default reply or asking a clarification question as instructed.\n"
            "\n"
            "Definition:\n"
            "- A **simple claim** does **not** contain latent information.\n"
            "- A **complex claim** contains latent information, which includes:\n"
            "  1. **Unresolved Entity**: an entity (person, object, event, etc.) whose referent is not specified or cannot be inferred from the claim (e.g., 'the writer').\n"
            "  2. **Undetermined Attribute**: an attribute of a subject that is not mentioned in the claim (e.g., birth date, nationality, role, etc.).\n"
            "\n"
            "Step 1: First determine whether the claim contains either type of latent information above.\n"
            "  - If it does **not**, classify it as a **simple claim** and output: `no question`\n"
            "  - If it does, classify it as a **complex claim**, and proceed to Step 2.\n"
            "\n"
            "Step 2 (for complex claims only): Identify **one** latent item that requires clarification using the following priority rules:\n"
            "  1. Prioritize **unresolved entities** over **undetermined attributes**.\n"
            "  2. Among entities, choose the one that is central to the claim; the **subject** takes precedence over objects or other components.\n"
            "  3. If no entities are unresolved, pick the most critical missing attribute.\n"
            "\n"
            "Step 3: Based on the chosen latent item, generate **one clear factual question** to make the claim more explicit.\n"
            " DO NOT ask yes/no or ambiguous questions.\n"
            " The question must refer to **only one latent element**, without assuming or combining unrelated attributes.\n"
            " Avoid bundled questions such as: “Who was the developer of the Retro Engine and served as the project lead for Sonic Mania?” Instead, only ask about **one** thing.\n"
            "\n"
            "Examples:\n"
            "1. Claim: The song recorded by Fergie that was produced by Polow da Don and was followed by Life Goes On was M.I.L.F.$.\n"
            "   → Output: no question\n"
            "   Explanation: All named entities are resolved and no attribute is missing. This is a simple claim.\n"
            "\n"
            "2. Claim: Substorm was described in qualitative terms by a scientist nominated for Nobel Prize seven times.\n"
            "   → Output: Who is the scientist nominated for Nobel Prize seven times?\n"
            "   Explanation: The scientist is an unresolved entity.\n"
            "\n"
            "3. Claim: The area renamed Northland in Stone Spring, an area that once connected Great Britain to continental the Grand Canyon, is thought to have been submerged around 6,200 BCE by a massive landslide along 290 km of the continental shelf.\n"
            "   → Output: Where is the area renamed 'Northland' in Stone Spring located?\n"
            "   Explanation: That area is an unresolved entity. Other unresolved entities also exist, but this one has highest priority.\n"
            "\n"
            "4. Claim: The writer of the novel Horizon is American. She was younger than the author of Dubin's Lives.\n"
            "   → Output: Who is the writer of the novel Horizon?\n"
            "   Explanation: There are multiple unresolved entities and an undetermined attribute (birth date), but unresolved entity (subject) takes precedence.Next, you can ask: Who is the author of Dubin's Lives? and What is the birth date of xxx?\n"
            "\n"
            f"Claim: {claim}\n\n"
            "Do not output any explanation.Your output (either `no question` or a single, well-formed question):"
        )
        return self.llm.chat("", prompt)




