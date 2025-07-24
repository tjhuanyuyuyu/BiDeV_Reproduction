# test_one_claim_gold.py
from bidev.pipeline import BiDeV

if __name__ == "__main__":
    # 初始化 BiDeV 流程
    bidev = BiDeV(wiki_dir="unused/path", n_iter=3) #传入两个参数，wiki路径和迭代次数

    # 可以换成 HOVER 或 FEVEROUS 中的一条数据
    claim = "The man known as the voice of \"Elgar\" voices the English character in the Manga Love Hina inspired by Keitaro Arima."
    gold_evidence = [
       "Keitar\u014d Urashima (\u6d66\u5cf6 \u666f\u592a\u90ce , Urashima Keitar\u014d ) is a fictional character and the protagonist from Ken Akamatsu's manga and anime \"Love Hina\". He is voiced by Y\u016bji Ueda (Japanese) and Derek Stephen Prince (English). His name is inspired by Keitar\u014d Arima as well as the mythological character Urashima Tar\u014d\nDerek Stephen Prince (born February 5, 1969 in Inglewood, California) is an American voice actor who is most memorable for his various roles in the \"Digimon\" series, as well as the voice of Elgar in the live-action \"Power Rangers Turbo\" and \"Power Rangers in Space\"."
    ]

    print("======== BiDeV: Gold Evidence Test ========")
    print("Claim:", claim)
    print("Gold Evidence:")
    for e in gold_evidence:
        print(" -", e)

    # 执行 pipeline（gold 模式）
    result = bidev.run(claim, gold_evidences=gold_evidence)
    print("\nFinal Verdict:", result)
