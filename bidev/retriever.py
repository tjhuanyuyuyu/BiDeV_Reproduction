# bidev/retriever.py
from typing import List
from rank_bm25 import BM25Okapi
import os

class BM25Retriever:
    def __init__(self, wiki_path: str):
        """
        初始化检索器。
        wiki_path: 文档库路径
        """
        self.docs = []
        # 文件
        if os.path.isfile(wiki_path):
            with open(wiki_path, "r", encoding="utf-8") as f:
                self.docs = [line.strip() for line in f if line.strip()] # 一行算一个文档
        # 文件夹
        elif os.path.isdir(wiki_path):
            for filename in os.listdir(wiki_path):
                with open(os.path.join(wiki_path, filename), "r", encoding="utf-8") as f:
                    self.docs.extend([line.strip() for line in f if line.strip()])
        else:
            raise FileNotFoundError(f"{wiki_path} does not exist.")

        self.tokenized = [doc.split() for doc in self.docs] # 文档分词
        self.bm25 = BM25Okapi(self.tokenized) if self.tokenized else None

    def query(self, query: str, k: int = 10) -> List[str]:
        """
        查询 top-k 检索结果
        """
        if self.bm25 is None:
            return []
        scores = self.bm25.get_scores(query.split()) # 查询分词
        topk_idx = sorted(range(len(scores)), key=lambda i: -scores[i])[:k] # 取前k高分
        return [self.docs[i] for i in topk_idx]
