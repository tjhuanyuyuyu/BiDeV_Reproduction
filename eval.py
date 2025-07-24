import json
from bidev.pipeline import BiDeV

def load_data(json_path):
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data

def main():
    json_file = "data/test.json"  #  修改路径
    data = load_data(json_file)

    bidev = BiDeV(wiki_dir="unused/path", n_iter=3)  # gold 模式不需要真正的 wiki_dir

    total = 0
    correct = 0

    for item in data:
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
    print("\n========= EVALUATION SUMMARY =========")
    print(f"Total samples: {total}")
    print(f"Correct predictions: {correct}")
    print(f"Accuracy: {accuracy:.2%}")

if __name__ == "__main__":
    main()