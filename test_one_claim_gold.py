# test_one_claim_gold.py
from bidev.pipeline import BiDeV

if __name__ == "__main__":
    # 初始化 BiDeV 流程，wiki_dir 不再真正用到
    bidev = BiDeV(wiki_dir="unused/path", n_iter=1)

    # 可以换成 HOVER 或 FEVEROUS 中的一条数据
    claim = "Before I Go to Sleep stars an Australian actress, producer and occasional singer."
    gold_evidence = [
        "Before I Go to Sleep is a 2014 mystery psychological thriller film written and directed by Rowan Joff\u00e9 and based on the 2011 novel of the same name by S. J. Watson. An international co-production between the United Kingdom, the United States, France, and Sweden, the film stars Nicole Kidman, Mark Strong, Colin Firth, and Anne-Marie Duff.\nNicole Mary Kidman, AC ( , ; born 20 June 1967) is an Australian actress, producer and occasional singer. She is the recipient of several awards, including an Academy Award, two Primetime Emmy Awards, a BAFTA Award, three Golden Globe Awards, and the Silver Bear for Best Actress."
    ]

    print("======== BiDeV: Gold Evidence Test ========")
    print("Claim:", claim)
    print("Gold Evidence:")
    for e in gold_evidence:
        print(" -", e)

    # 执行 pipeline（gold 模式）
    result = bidev.run(claim, gold_evidences=gold_evidence)
    print("\nFinal Verdict:", result)
