# pipeline.py
from typing import List
from bidev.modules.perceptor  import Perceptor
from bidev.modules.querier    import Querier
from bidev.modules.rewriter   import Rewriter
from bidev.modules.decomposer import Decomposer
from bidev.modules.checker    import Checker
from bidev.modules.filter     import Filter
from bidev.retriever          import BM25Retriever

class BiDeV:
    def __init__(self, wiki_dir: str, n_iter: int = 3):
        # 六个模块
        self.perc   = Perceptor()
        self.quer   = Querier()
        self.rew    = Rewriter()
        self.decom  = Decomposer()
        self.check  = Checker()
        self.filt   = Filter()
        self.retr   = BM25Retriever(wiki_dir)
        self.n_iter = n_iter

    def run(self, raw_claim: str, gold_evidences: List[str] = None) -> str:
        claim = raw_claim

        #如果是字符串(gold setting下)，就转成单元素列表
        # if isinstance(gold_evidences, str):
        #     gold_evidences = [gold_evidences]


        # ============= Stage 1: Perceive then Rewrite =============
        # for _ in range(self.n_iter):
        #     q    = self.perc.detect_latent(claim)
        #     ans  = self.quer.answer(q)
        #     claim = self.rew.rewrite(claim, q, ans)


        for i, _ in enumerate(range(self.n_iter), 1):  # 迭代是感知器、询问器和改写器一起的，i 从 1 开始

            # Step 1: 感知问题
            q = self.perc.detect_latent(claim)
            print(f"感知问题 q{i}：{q}")

            if gold_evidences is None:
                q_evidences = self.retr.query(q, k=10)
                print("query Open!")
            else :
                q_evidences = gold_evidences
                print("query Gold!")
            
            if q == "no question":
                print(f"回答 a{i}：{"no answer"}")
                print(f"第 {i} 次改写后 claim：{claim}")
            else:
                # Step 2: 用过滤器筛选证据
                filtered = self.filt.filter_paragraphs(q_evidences, q)  # 即 e_i* ，gold_evidences是列表格式

                # Step 3: 用 question 和 e_i* 生成答案
                ans = self.quer.answer(q, filtered)
                print(f"回答 a{i}：{ans}")
                
                claim = self.rew.rewrite(claim, q, ans)
                print(f"第 {i} 次改写后 claim：{claim}")


        # ============= Stage 2: Decompose then Check ==============
        sub_claims = self.decom.decompose(claim)
        print(f"拆解为 {len(sub_claims)} 个子句：")
        for i, sc in enumerate(sub_claims):
            print(f"  子句 {i+1}: {sc}")

        verdicts = []
        for sc in sub_claims:
            if gold_evidences is None:
                sc_evidences = self.retr.query(sc, k=10)
                filtered_ev = self.filt.filter_paragraphs(sc_evidences, sc)
                print("check Open!")
            else:
                filtered_ev = self.filt.filter_paragraphs(gold_evidences, sc)
                print("check Gold!")
            result = self.check.verify(sc, filtered_ev)
            print(f"子句判断结果：{result}")
            verdicts.append(result.strip().lower())

        # ========= Final Decision ==========
        if all(v == "support" for v in verdicts):
            return "Supports"
        else:
            return "Refutes"

    