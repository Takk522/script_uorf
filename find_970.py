import os

# 1. 读取pdb_970里所有pdb文件的名称并保存在集合A中
pdb_folder = 'pdb_1428'
pdb_files = [os.path.splitext(file)[0] for file in os.listdir(pdb_folder) if file.endswith('.pdb')]
A = set(pdb_files)

# 2. 读取mono_output_970里所有子文件夹的名称并保存在集合B中
mono_folder = 'mono_output_1428'
B = set(folder for folder in os.listdir(mono_folder) if os.path.isdir(os.path.join(mono_folder, folder)))


# 3. 找出存在于B但却不存在于A的元素并打印出来
missing_elements = B - A
print("存在于B但却不存在于A的元素:")
for element in missing_elements:
    print(element)
