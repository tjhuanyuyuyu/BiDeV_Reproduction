import json
import random
from bidev.pipeline import BiDeV

def load_data(json_path):
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data



def main():
    json_file = "data/sample2_100.json"  # 修改路径
    sampled_data = load_data(json_file)


    txt_file = "data/hover_evidence_corpus.txt"

    bidev = BiDeV(wiki_dir=txt_file, n_iter=3)  

    total = 0
    correct = 0

    for item in sampled_data:
        claim = item["claim"]
        gold_evidence = [item["evidence"]] if isinstance(item["evidence"], str) else item["evidence"]
        true_label = item["label"].strip().lower()

        print(f"\n[#{total + 1}] Claim: {claim}")
        result = bidev.run(claim, gold_evidences=gold_evidence)
        print("  → Predicted:", result)
        print("  → Ground Truth:", true_label)

        if result.lower() == true_label:
            correct += 1
        total += 1

    accuracy = correct / total if total > 0 else 0
    print("\n=========EVALUATION SUMMARY =========")
    print(f"Total samples: {total}")
    print(f"Correct predictions: {correct}")
    print(f"Accuracy: {accuracy:.2%}")

if __name__ == "__main__":
    main()