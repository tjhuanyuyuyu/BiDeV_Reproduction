from typing import List
from rank_bm25 import BM25Okapi
import glob, os, json

class BM25Retriever:
    def __init__(self, wiki_dir: str):
        self.docs = []
        if os.path.isdir(wiki_dir):
            for filename in os.listdir(wiki_dir):
                with open(os.path.join(wiki_dir, filename), "r") as f:
                    self.docs.append(f.read())

        self.tokenized = [doc.split() for doc in self.docs]
        if len(self.tokenized) > 0:
            self.bm25 = BM25Okapi(self.tokenized)
        else:
            self.bm25 = None

    def query(self, query: str, k: int = 5) -> List[str]:
        if self.bm25 is None:
            return []  # 没有检索语料就返回空列表
        scores = self.bm25.get_scores(query.split())
        topk_idx = sorted(range(len(scores)), key=lambda i: -scores[i])[:k]
        return [self.docs[i] for i in topk_idx]
