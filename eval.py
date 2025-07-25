import json
import random
from bidev.pipeline import BiDeV

def load_data(json_path):
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data

def save_sampled_data(sampled_data, output_path="sample_100.json"):
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(sampled_data, f, ensure_ascii=False, indent=2)
    print(f"\n已保存随机采样的 100 条数据到 {output_path}")

def main():
    json_file = "data/4hop.json"  # 修改路径
    data = load_data(json_file)

    sample_size = 3
    if len(data) < sample_size:
        print(f"文件中只有 {len(data)} 条数据，已全部使用")
        sampled_data = data
    else:
        sampled_data = random.sample(data, sample_size)

    # 保存采样后的数据
    save_sampled_data(sampled_data, output_path="data/sample4_100.json")

    bidev = BiDeV(wiki_dir="unused/path", n_iter=3)  # gold 模式不需要真正的 wiki_dir

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
    print("\n========= EVALUATION SUMMARY =========")
    print(f"Total samples: {total}")
    print(f"Correct predictions: {correct}")
    print(f"Accuracy: {accuracy:.2%}")

if __name__ == "__main__":
    main()