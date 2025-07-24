# run_demo.py
import json
import argparse
from pipeline import BiDeV  

def load_samples(jsonl_path, max_samples=5, use_gold=False):
    """加载 claim 和对应的 gold evidence（如果使用）"""
    samples = []
    with open(jsonl_path, 'r', encoding='utf-8') as f:
        for i, line in enumerate(f):
            if i >= max_samples:
                break
            data = json.loads(line)
            claim = data["claim"]
            evidence = data.get("evidence", []) if use_gold else None
            if isinstance(evidence, str):
                evidence = [evidence]
            samples.append((claim, evidence))
    return samples

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", type=str, default="data/hover_small.jsonl",
                        help="Path to the jsonl file containing claims and (optionally) evidence")
    parser.add_argument("--wiki", type=str, default="data/wiki_docs/",
                        help="Path to corpus directory for BM25 retrieval")
    parser.add_argument("--n_iter", type=int, default=3,
                        help="Number of Perceive-then-Rewrite iterations")
    parser.add_argument("--max_samples", type=int, default=5,
                        help="How many examples to run")
    parser.add_argument("--use_gold", action="store_true",
                        help="Use gold evidence instead of BM25 + filter")
    args = parser.parse_args()

    print("=========== BiDeV Demo ===========")
    print(f"→ Mode: {'GOLD Evidence' if args.use_gold else 'BM25 Open Setting'}")
    print(f"→ Iterations: {args.n_iter}")
    print(f"→ Data: {args.data}")
    print("==================================")

    bidev = BiDeV(wiki_dir=args.wiki, n_iter=args.n_iter)
    samples = load_samples(args.data, max_samples=args.max_samples, use_gold=args.use_gold)

    for i, (claim, gold_evidence) in enumerate(samples):
        print(f"\n=== [Claim #{i+1}] ===")
        print("Input Claim:", claim)
        verdict = bidev.run(claim, gold_evidences=gold_evidence)
        print("Final Verdict:", verdict)
