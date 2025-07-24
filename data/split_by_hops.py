import json

# 输入文件路径
input_file = "hover-dev.json"

# 输出文件路径
output_files = {
    2: "2hop.json",
    3: "3hop.json",
    4: "4hop.json"
}

# 初始化容器
hop_groups = {2: [], 3: [], 4: []}

# 加载数据
with open(input_file, "r", encoding="utf-8") as f:
    data = json.load(f)

# 分组
for item in data:
    hop = item.get("num_hops")
    if hop in hop_groups:
        hop_groups[hop].append(item)

# 保存结果
for hop, items in hop_groups.items():
    with open(output_files[hop], "w", encoding="utf-8") as f:
        json.dump(items, f, indent=2, ensure_ascii=False)

print("已完成按 num_hops 分割 ✅")