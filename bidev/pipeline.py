# pipeline.py
from typing import List
from bidev.modules.perceptor  import Perceptor
from bidev.modules.querier    import Querier
from bidev.modules.rewriter   import Rewriter
from bidev.modules.decomposer import Decomposer
from bidev.modules.checker    import Checker
from bidev.modules.filter     import Filter

class BiDeV:
    def __init__(self, wiki_dir: str, n_iter: int = 3):
        self.perc   = Perceptor()
        self.quer   = Querier(wiki_dir)
        self.rew    = Rewriter()
        self.decom  = Decomposer()
        self.check  = Checker(wiki_dir)
        self.filt   = Filter()
        self.n_iter = n_iter

    def run(self, raw_claim: str, gold_evidences: List[str] = None) -> str:
        claim = raw_claim

        if isinstance(gold_evidences, str):
            gold_evidences = [gold_evidences]


        # ============= Stage 1: Perceive then Rewrite =============
        # for _ in range(self.n_iter):
        #     q    = self.perc.detect_latent(claim)
        #     print(q)
        #     ans  = self.quer.answer(q)
        #     print(ans)
        #     claim = self.rew.rewrite(claim, q, ans)
        #     print(claim)

        for i, _ in enumerate(range(self.n_iter), 1):  # i 从 1 开始
            q = self.perc.detect_latent(claim)
            print(f"感知问题 q{i}：{q}")

            ans = self.quer.answer(q)
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
            if gold_evidences is not None:
                ev = gold_evidences
            else:
                raw_evidence = self.quer.retr.query(sc, k=5)
                ev = self.filt.filter_paragraphs(raw_evidence, sc)
            result = self.check.verify(sc, ev)
            print(f"子句判断结果：{result}")
            verdicts.append(result.strip().lower())

        # ========= Final Decision ==========
        if all(v == "support" for v in verdicts):
            return "Supports"
        else:
            return "Refutes"

    