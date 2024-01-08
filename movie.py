from pymol.cmd import cmd
import os
import glob


output_folder = "/Users/jianchengluo/Desktop/output_images"

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

folder_path = "/Users/jianchengluo/Desktop/uORF2/AF2_98"
pdb_files = glob.glob(os.path.join(folder_path, "*.pdb"))
pdb_files = [os.path.abspath(file) for file in pdb_files]

cmd.bg_color("white")
cmd.set("ray_trace_mode", 1)
cmd.set("ray_trace_frames", 1)
cmd.mset("1 x" + str(len(pdb_files) * 360))

for i, pdb_file in enumerate(pdb_files):
    cmd.load(pdb_file, f"protein_{i}")
    for j in range(180):
        cmd.rotate("y", 2, f"protein_{i}")  # 逐帧旋转2度
        cmd.frame(j + 1)
        output_image_path = os.path.join(output_folder, f"frame_{j}.png")
        cmd.png(output_image_path, width=800, height=600, dpi=300)

cmd.mdo(1, "mplay")
cmd.delete("all")



#convert -delay 10 -loop 0 frame_*.png movie.mp4
