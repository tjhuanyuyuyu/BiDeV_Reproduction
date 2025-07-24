# eval.py
import json
from sklearn.metrics import accuracy_score
from bidev.pipeline import BiDeV

def load_and_group_by_hop(path, max_samples=None):
    hop2, hop3, hop4 = [], [], []
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f) if path.endswith(".json") else [json.loads(line) for line in f]
        for i, item in enumerate(data):
            if max_samples and i >= max_samples:
                break
            if item["label"] not in ["supports", "refutes"]:
                continue
            sample = {
                "claim": item["claim"],
                "label": "Supports" if item["label"] == "supports" else "Refutes",
                "evidence": item.get("evidence", [])
            }
            hop = item.get("num_hops", 0)
            if hop == 2:
                hop2.append(sample)
            elif hop == 3:
                hop3.append(sample)
            elif hop >= 4:
                hop4.append(sample)
    return hop2, hop3, hop4

def load_feverous(path, max_samples=None):
    data = []
    with open(path, 'r', encoding='utf-8') as f:
        for i, line in enumerate(f):
            if max_samples and i >= max_samples:
                break
            item = json.loads(line)
            if item["label"] not in ["supports", "refutes"]:
                continue
            data.append({
                "claim": item["claim"],
                "label": "Supports" if item["label"] == "supports" else "Refutes",
                "evidence": item.get("evidence", [])
            })
    return data

def evaluate(dataset, bidev: BiDeV, use_gold=True):
    y_true, y_pred = [], []
    for i, sample in enumerate(dataset):
        pred = bidev.run(sample["claim"], gold_evidences=sample["evidence"] if use_gold else None)
        y_true.append(sample["label"])
        y_pred.append(pred)
        print(f"[{i+1}] Gold: {sample['label']} | Pred: {pred}")
    acc = accuracy_score(y_true, y_pred)
    return acc

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--hover_path", type=str, default="data/hover/hover_dev_release_v1.1.json")
    parser.add_argument("--fever_path", type=str, default="data/feverous_s.jsonl")
    parser.add_argument("--wiki_dir", type=str, default="data/wiki_docs/")
    parser.add_argument("--use_gold", action="store_true")
    parser.add_argument("--max_samples", type=int, default=None)
    parser.add_argument("--n_iter", type=int, default=3)
    args = parser.parse_args()

    bidev = BiDeV(wiki_dir=args.wiki_dir, n_iter=args.n_iter)

    print("\nLoading HOVER...")
    hop2, hop3, hop4 = load_and_group_by_hop(args.hover_path, args.max_samples)

    print("\nEvaluating HOVER-hop2")
    acc2 = evaluate(hop2, bidev, use_gold=args.use_gold)

    print("\nEvaluating HOVER-hop3")
    acc3 = evaluate(hop3, bidev, use_gold=args.use_gold)

    print("\nEvaluating HOVER-hop4+")
    acc4 = evaluate(hop4, bidev, use_gold=args.use_gold)

    print("\nEvaluating FEVEROUS-s")
    fever_data = load_feverous(args.fever_path, args.max_samples)
    acc_fever = evaluate(fever_data, bidev, use_gold=args.use_gold)

    print("\n======= Final Accuracy Summary =======")
    print(f"HOVER-hop2   Accuracy: {acc2:.3f}")
    print(f"HOVER-hop3   Accuracy: {acc3:.3f}")
    print(f"HOVER-hop4+  Accuracy: {acc4:.3f}")
    print(f"FEVEROUS-s   Accuracy: {acc_fever:.3f}")
