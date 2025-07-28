# import json
# import random
# from bidev.pipeline import BiDeV

# def load_data(json_path):
#     with open(json_path, 'r', encoding='utf-8') as f:
#         data = json.load(f)
#     return data



# def main():
#     json_file = "data/sample3_100.json"  # 修改路径
#     sampled_data = load_data(json_file)


#     txt_file = "data/hover_evidence_corpus.txt"

#     bidev = BiDeV(wiki_dir=txt_file, n_iter=3)  

#     total = 0
#     correct = 0

#     for item in sampled_data:
#         claim = item["claim"]
#         gold_evidence = [item["evidence"]] if isinstance(item["evidence"], str) else item["evidence"]
#         true_label = item["label"].strip().lower()

#         print(f"\n[#{total + 1}] Claim: {claim}")
#         result = bidev.run(claim, gold_evidences=gold_evidence)
#         print("  → Predicted:", result)
#         print("  → Ground Truth:", true_label)

#         if result.lower() == true_label:
#             correct += 1
#         total += 1

#     accuracy = correct / total if total > 0 else 0
#     print("\n=========EVALUATION SUMMARY =========")
#     print(f"Total samples: {total}")
#     print(f"Correct predictions: {correct}")
#     print(f"Accuracy: {accuracy:.2%}")

# if __name__ == "__main__":
#     main()

import json
import argparse
import os
from bidev.pipeline import BiDeV

def load_data(json_path):
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data

def main():
    parser = argparse.ArgumentParser(description="Run BiDeV on a dataset")

    # 默认值为文件名，自动补上 data/ 前缀
    parser.add_argument("--data", type=str, default="sample3_100.json",
                        help="Input JSON filename under data/ directory (default: sample3_100.json)")
    parser.add_argument("--wiki", type=str, default="hover_evidence_corpus.txt",
                        help="Wikipedia corpus filename under data/ directory (default: hover_evidence_corpus.txt)")
    parser.add_argument("--mode", type=str, choices=["gold", "open"], default="gold",
                        help="Verification mode: 'gold' or 'open' (default: gold)")
    parser.add_argument("--n_iter", type=int, default=3,
                        help="Number of BiDeV reasoning iterations (default: 3)")

    args = parser.parse_args()

    # 拼接为完整路径
    data_path = os.path.join("data", args.data)
    wiki_path = os.path.join("data", args.wiki)

    sampled_data = load_data(data_path)
    bidev = BiDeV(wiki_dir=wiki_path, n_iter=args.n_iter)

    total = 0
    correct = 0

    for item in sampled_data:
        claim = item["claim"]
        true_label = item["label"].strip().lower()

        if args.mode == "gold":
            gold_evidence = [item["evidence"]] if isinstance(item["evidence"], str) else item["evidence"]
        else:
            gold_evidence = None

        print(f"\n[#{total + 1}] Claim: {claim}")
        result = bidev.run(claim, gold_evidences=gold_evidence)
        print("  → Predicted:", result)
        print("  → Ground Truth:", true_label)

        if result.lower() == true_label:
            correct += 1
        total += 1

    accuracy = correct / total if total > 0 else 0
    print("\n========= EVALUATION SUMMARY =========")
    print(f"Total samples: {total}")
    print(f"Correct predictions: {correct}")
    print(f"Accuracy: {accuracy:.2%}")

if __name__ == "__main__":
    main()
