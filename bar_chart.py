# import matplotlib.pyplot as plt
# import numpy as np

# # 数据
# datasets = ['Hover(2-hop)', 'Hover(3-hop)', 'Hover(4-hop)', 'Feverous-s']
# methods = ['BiDeV', 'w/o Mf', 'w/o Mp', 'w/o Mr', 'w/o Md']

# # 每个方法对应的数据值（Macro-F1）
# # 按照每个dataset的5个柱子顺序排列
# scores = [
#     [81, 83, 61, 81, 73],  # Hover(2-hop)
#     [75, 70, 58, 75, 65],  # Hover(3-hop)
#     [69, 72, 60, 70, 66],  # Hover(4-hop)
#     [93, 97, 85, 92, 94]   # Feverous-s
# ]
# # -------------------------------------

# # 颜色
# colors = ['red', 'gold', 'deepskyblue', 'steelblue', 'lightseagreen']

# # 图像参数
# bar_width = 0.15
# x = np.arange(len(datasets))  # [0, 1, 2, 3]

# # 设置图像大小
# plt.figure(figsize=(10, 6))

# # 画每一组柱子
# for i in range(len(methods)):
#     plt.bar(x + i * bar_width, [row[i] for row in scores],
#             width=bar_width, label=methods[i], color=colors[i])

# # 坐标轴与标签设置
# plt.ylabel('Macro-F1', fontsize=14)
# plt.xlabel('Dataset', fontsize=13)
# plt.xticks(x + 2 * bar_width, datasets, fontsize=12)
# plt.yticks(np.arange(0, 101, 20), fontsize=12)
# plt.ylim(0, 100)
# plt.legend(fontsize=12)
# plt.tight_layout()
# plt.grid(axis='y', linestyle='--', alpha=0.4)

# # 显示图像
# plt.show()


import matplotlib.pyplot as plt
import numpy as np

# 数据
datasets = ['Hover(2-hop)', 'Hover(3-hop)', 'Hover(4-hop)', 'Feverous-s']
methods = ['BiDeV', 'w/o Mf', 'w/o Mp', 'w/o Mr', 'w/o Md']
scores = [
    [81, 83, 61, 81, 73],  # Hover(2-hop)
    [75, 70, 58, 75, 65],  # Hover(3-hop)
    [69, 72, 60, 70, 66],  # Hover(4-hop)
    [93, 97, 85, 92, 94]   # Feverous-s
]
colors = ['red', 'gold', 'deepskyblue', 'steelblue', 'lightseagreen']

# 图像参数
bar_width = 0.15
x = np.arange(len(datasets))  # 基础 x 位置

plt.figure(figsize=(10, 6))

# 绘图
for i in range(len(methods)):
    plt.bar(
        x + i * bar_width,
        [row[i] for row in scores],
        width=bar_width,
        label=methods[i],
        color=colors[i],
        edgecolor='black'  
    )

# 坐标轴设置
plt.ylabel('Macro-F1', fontsize=14)
plt.xlabel('Dataset', fontsize=13)
plt.xticks(x + 2 * bar_width, datasets, fontsize=12)
plt.yticks(np.arange(0, 101, 20), fontsize=12)
plt.ylim(0, 100)
plt.legend(fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.4)
plt.tight_layout()
plt.show()
