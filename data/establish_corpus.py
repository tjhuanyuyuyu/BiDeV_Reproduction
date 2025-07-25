import json
from pathlib import Path

# === 设置输入输出文件路径 ===
input_json_path = "feverous-s-dev.json"   
output_txt_path = "feverous_s_evidence_corpus.txt"    # 编号文本库
output_json_path = "feverous_s_evidence_id_map.json"  # 保存编号-ID 对应关系，便于回溯

# === 加载 JSON 数据 ===
with open(input_json_path, "r", encoding="utf-8") as f:
    data = json.load(f)

# === 提取、去重、编号 ===
seen = set()
doc_list = []
id_map = {}

for idx, item in enumerate(data):
    evidence_raw = item["evidence"]
    if isinstance(evidence_raw, str):
        evidence_list = [evidence_raw]
    elif isinstance(evidence_raw, list):
        evidence_list = evidence_raw
    else:
        continue

    for evi in evidence_list:
        clean_evi = evi.strip().replace("\n", " ")
        if clean_evi and clean_evi not in seen:
            seen.add(clean_evi)
            doc_id = f"DOC_{len(doc_list)+1:05d}"  # 格式：DOC_00001
            doc_list.append((doc_id, clean_evi))
            id_map[doc_id] = clean_evi

# === 保存为文本文件（编号 + 内容）===
with open(output_txt_path, "w", encoding="utf-8") as f:
    for doc_id, text in doc_list:
        f.write(f"{doc_id}: {text}\n")

# === 可选：保存 ID->内容 的 JSON 文件 ===
with open(output_json_path, "w", encoding="utf-8") as f:
    json.dump(id_map, f, indent=2, ensure_ascii=False)

print(f"成功写入 {len(doc_list)} 条 evidence 到 {output_txt_path}")