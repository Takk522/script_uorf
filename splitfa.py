import os

de = "/"
# 创建一个文件夹用于存放fasta文件
output_folder = "/Users/jianchengluo/Desktop/uORF/fasta_files_1428"
os.makedirs(output_folder, exist_ok=True)

# 打开包含多个序列的文本文件
with open("/Users/jianchengluo/Desktop/uORF/alphafold_predict_add.txt", "r") as input_file:
    sequences = input_file.read().strip().split(">")

# 遍历分割后的序列
for sequence in sequences:
    if sequence:
        # 提取序列名和序列内容
        lines = sequence.split("\n")
        header = lines[0]
        sequence_data = "\n".join(lines[1:])

        # 创建fasta文件名
        fasta_file_name = header.split()[0] + ".fasta"
        
        if "/" in fasta_file_name:
            fasta_file_name = fasta_file_name.replace(de,"_")

        # 创建完整的文件路径
        fasta_file_path = os.path.join(output_folder, fasta_file_name)

        # 写入fasta文件
        with open(fasta_file_path, "w") as fasta_file:
            fasta_file.write(f">{header}\n{sequence_data}")

print("已分割为单独的fasta文件并存放在文件夹", output_folder)

