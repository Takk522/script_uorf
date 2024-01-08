import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 从Excel文件读取数据
data = pd.read_excel('all_1428.xlsx')

# 获取第一列（标签列），第四列，第六列，第七列的数据
labels = data.iloc[:, 0]
col4 = data.iloc[:, 3]
col6 = data.iloc[:, 5]
col7 = data.iloc[:, 6]

# 创建一个三维图形
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# 打开一个TXT文件来写入标签
with open('3d_filter.txt', 'w') as txt_file:
    # 绘制三维散点图，将坐标值大于0.6的点设为红色，其余点保持蓝色
    for i, label in enumerate(labels):
        x = col6[i]
        y = col7[i]
        z = col4[i]
        if x > 0.45 and y > 0.1 and z > 0.55:
            ax.scatter(x, y, z, c='red', marker='o')
            # 写入符合条件的标签到TXT文件
            txt_file.write(label + '\n')
        else:
            ax.scatter(x, y, z, c='blue', marker='o')

# 添加标签
ax.set_xlabel('secondary_structure')
ax.set_ylabel('LDI')
ax.set_zlabel('pLDDT')

# 标签每隔一定距离显示，以避免重叠
n = 5  # 设置标签显示间隔
for i, label in enumerate(labels):
    if i % n == 0:
        ax.text(col6[i], col7[i], col4[i], label, fontsize=5)

# 显示图形
plt.show()

