
import os
import pymol

# 启动PyMOL
pymol.finish_launching()

from pymol import cmd

# 设置要加载的PDB文件的文件夹路径
folder_path = "/Users/jianchengluo/Desktop/uORF/AF2_98/"
x_spacing = 100
y_spacing = 100

# 创建一个PyMOL会话
cmd.reinitialize()
cmd.set("ray_trace_frames", 1)
cmd.set("label_size", 6)

# 加载初始PDB文件
cmd.load("/Users/jianchengluo/Desktop/uORF/AF2_98/ASNSD1.pdb")
cmd.show("cartoon")
cmd.color("gray", "all")
cmd.orient()

# 初始化位置
x_pos, y_pos = 0, 0
label_x, label_y = 0, -30

# 获取PDB文件列表
pdb_files = [f for f in os.listdir(folder_path) if f.endswith(".pdb")]

# 循环加载PDB文件，设置位置和标签
for pdb_file in pdb_files:
    structure_name = os.path.splitext(pdb_file)[0]
    cmd.load(os.path.join(folder_path, pdb_file), structure_name)
    cmd.translate([x_pos, y_pos, 0], structure_name)

    # 选择每个蛋白质的第一个原子
    cmd.select(f"{structure_name}_first_atom", f"{structure_name} and id 1")

    cmd.set("label_position", [0, 0, 0])  # 重置标签位置
    cmd.label(f"{structure_name}_first_atom", f'"{structure_name}"')
    cmd.delete(f"{structure_name}_first_atom")
    

    x_pos += x_spacing
    if x_pos > 1800:
        x_pos = 0
        y_pos += y_spacing


cmd.spectrum("b", "red_yellow_green_cyan_blue", minimum=50, maximum=90)
cmd.zoom("all")
cmd.center("all")
cmd.refresh()
cmd.viewport(1800, 4000)


# 设置视图和图像参数
cmd.viewport(1800, 4000)
cmd.set("ray_opaque_background", 1)
cmd.ray()

# 保存图像为PNG文件
output_image = "/Users/jianchengluo/Desktop/AF2_431.png"
cmd.png(output_image, width=800, height=600, dpi=300, ray=1)

