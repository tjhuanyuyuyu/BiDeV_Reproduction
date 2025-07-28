# modules/filter.py
from typing import List
from bidev.llm_wrappers import DashScopeClient

class Filter:
    def __init__(self):
        self.llm = DashScopeClient()

    def filter_paragraphs(self, evidences: List[str], question_or_claim: str) -> List[str]:
        final_paragraphs = []

        for doc in evidences:
            prompt = (
                "You are a domain expert. Given a question or a factual claim and a long retrieved piece of evidence text, "
                "your task is to filter out only those parts of the evidence that are absolutely and definitively unrelated to the given question or claim. "
                "Please follow the instructions below with extreme caution:\n\n"
                "1. Carefully read the question or claim and identify parts of the evidence that are similar or potentially relevant in meaning. Retain these parts.\n"
                "2. For any part of the evidence that appears potentially relevant, or whose relevance you are uncertain about, retain it.\n"
                "3. Only remove a part of the evidence if you are absolutely certain that it is completely unrelated and dissimilar to the question or claim.\n"
                "4. Be extremely cautious in filtering — do not remove anything that might possibly contribute to understanding or verifying the question or claim.\n\n"               
                "Return the final filtered evidence text only.  \n\n"               
                f"Question or Claim:\n{question_or_claim}\n\n"
                f"Evidence:\n{doc}\n\n"
            )

            # 优化版
            # prompt = (
            #     "You are a domain expert. Given a question or a factual claim and a long piece of retrieved evidence text, "
            #     "your task is to split the evidence into complete paragraphs, and reorder them based on their semantic relevance to the given question or claim.\n\n"
            #     "Instructions:\n"
            #     "1. Split the evidence text into coherent, self-contained paragraphs. A paragraph should not be broken across sentences that contain pronouns or require previous context.\n"
            #     "2. Carefully assess each paragraph’s relevance to the question or claim. Rank them as:\n"
            #     "   - High Relevance: Directly supports answering the question or closely discusses the entities or facts involved.\n"
            #     "   - Medium Relevance: Provides some contextual or background information related to the question.\n"
            #     "   - Low Relevance: Unrelated or tangential content, included only as general background.\n"
            #     "3. Return the paragraphs in a new order:\n"
            #     "   - Place all High Relevance paragraphs first,\n"
            #     "   - followed by Medium Relevance,\n"
            #     "   - and then Low Relevance paragraphs at the end.\n"
            #     "4. Do NOT alter the content of any paragraph. Only rearrange them.\n\n"
            #     "5. If the final reordered evidence text exceeds 300 English words, truncate from the end by full sentences (split by '.') until the total word count is below 300.\n\n"
            #     "Example:\n\n"
            #     "Question:\n"
            #     "Who is the man who first published August Frederik Beutler?\n\n"
            #     "Evidence:\n"
            #     "George McCall Theal (11 April 1837, Saint John, New Brunswick – 17 April 1919, Wynberg, Cape Town), was the most prolific and influential South African historian, archivist and genealogist of the late nineteenth and early twentieth century.\n\n"
            #     "August Frederik Beutler (c. 1728 in Dinkelsbühl – ? in Cape Town) was an ensign (sergeant 1747–49, ensign 1749–54) in the employ of the Dutch East India Company who headed an epic 1752 reconnaissance expedition lasting 8 months from 29 February to November, eastward from Cape Town as far as the present-day site of Butterworth. Beutler wrote a comprehensive account of his pioneering expedition which was first published in 1896 by the historian George McCall Theal and in 1922 by the Dutch historian Everhardus Cornelis Godée Molsbergen (1875–1940). The mandate of the expedition was to report on the tribes living along the route, the possibility of trade and on anything else that might be profitable to the Dutch East India Company.\n\n"
            #     "Saint John is the port city of the Bay of Fundy in the Canadian province of New Brunswick. The port is Canada’s third largest port by tonnage with a cargo base that includes dry and liquid bulk, break bulk, containers, and cruise. In 2016, after a decades long decline, the city fell from being the most populous city in New Brunswick to the second most populous city in the province for the first time, with a population of 67,575 over an area of 315.82 sqkm. The Saint John metropolitan area covers a land area of 3,362.95 sqkm across the Caledonia Highlands, with a population (as of 2016) of 126,202. After the partitioning of the colony of Nova Scotia in 1784, the new colony of New Brunswick was thought to be named 'New Ireland' with the capital to be in Saint John before being vetoed by Britain's King George III. Saint John is the oldest incorporated city in Canada. During the reign of George III, the municipality was created by royal charter in 1785.\n\n"
            #     "Reordered Evidence:\n"
            #     "1. August Frederik Beutler (c. 1728 in Dinkelsbühl – ? in Cape Town) was an ensign (sergeant 1747–49, ensign 1749–54) in the employ of the Dutch East India Company who headed an epic 1752 reconnaissance expedition lasting 8 months from 29 February to November, eastward from Cape Town as far as the present-day site of Butterworth. Beutler wrote a comprehensive account of his pioneering expedition which was first published in 1896 by the historian George McCall Theal and in 1922 by the Dutch historian Everhardus Cornelis Godée Molsbergen (1875–1940). The mandate of the expedition was to report on the tribes living along the route, the possibility of trade and on anything else that might be profitable to the Dutch East India Company.\n\n"
            #     "2. George McCall Theal (11 April 1837, Saint John, New Brunswick – 17 April 1919, Wynberg, Cape Town), was the most prolific and influential South African historian, archivist and genealogist of the late nineteenth and early twentieth century.\n\n"
            #     "3. Saint John is the port city of the Bay of Fundy in the Canadian province of New Brunswick. The port is Canada’s third largest port by tonnage with a cargo base that includes dry and liquid bulk, break bulk, containers, and cruise. In 2016, after a decades long decline, the city fell from being the most populous city in New Brunswick to the second most populous city in the province for the first time, with a population of 67,575 over an area of 315.82 sqkm. The Saint John metropolitan area covers a land area of 3,362.95 sqkm across the Caledonia Highlands, with a population (as of 2016) of 126,202. After the partitioning of the colony of Nova Scotia in 1784, the new colony of New Brunswick was thought to be named 'New Ireland' with the capital to be in Saint John before being vetoed by Britain's King George III. Saint John is the oldest incorporated city in Canada. During the reign of George III, the municipality was created by royal charter in 1785."
            #     "Return the final evidence text only.  \n\n" 
            #     f"Question or Claim:\n{question_or_claim}\n\n"
            #     f"Evidence:\n{doc}\n\n"
            # )

            response = self.llm.chat("", prompt)

            if response.strip():
                final_paragraphs.extend([
                    para.strip() for para in response.strip().split("\n") if para.strip()
                ])

        return final_paragraphs
