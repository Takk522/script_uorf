import os
import pandas as pd


folder_path = "pLDDT_1428"
csv_files = [f for f in os.listdir(folder_path) if f.endswith(".csv")]

# 创建一个DataFrame来存储数据
data = {'Filename': [], 'Mean': [], '>90': [], '>70': [], '>50': []}

# 遍历CSV文件并提取数据
for file in csv_files:
    file_path = os.path.join(folder_path, file)
    df = pd.read_csv(file_path)
    
    filename = file.split(".")[0]  
    mean = df['pLDDT'].mean()
    total_count = len(df)
    gt_90_count = len(df[df['pLDDT'] > 90])
    gt_70_count = len(df[df['pLDDT'] > 70])
    gt_50_count = len(df[df['pLDDT'] > 50])
    
    data['Filename'].append(filename)
    data['Mean'].append(mean)
    data['>90'].append(gt_90_count / total_count)
    data['>70'].append(gt_70_count / total_count)
    data['>50'].append(gt_50_count / total_count)

# 创建DataFrame
result_df = pd.DataFrame(data)

# 将数据写入Excel文件
result_df.to_excel("pLDDT_1428_stats.xlsx", index=False)
