from bidev.llm_wrappers import DashScopeClient
from bidev.retriever import BM25Retriever

class Querier:
    def __init__(self, wiki_dir: str):
        self.llm = DashScopeClient()
        self.retr = BM25Retriever(wiki_dir)

    def answer(self, question: str) -> str:
        evidences = self.retr.query(question, k=5)
        joined = "\n".join(evidences)
        prompt = (
            f"You are a helpful assistant. Use the following context to answer the question.\n\n"
            f"Context:\n{joined}\n\n"
            f"Question: {question}\nAnswer:"
        )
        return self.llm.chat("", prompt)
