#!/bin/bash

input_folder="output_6764"
output_folder="outdssp"

mkdir -p "$output_folder"

for pdb_file in "$input_folder"/*.pdb; do

    if [ -f "$pdb_file" ]; then
        
        output_dssp="$output_folder/$(basename "$pdb_file" .pdb).dssp"
        mkdssp -i "$pdb_file" -o "$output_dssp"
        
        if [ $? -eq 0 ]; then
            echo "处理文件 $pdb_file 完成，生成 $output_dssp"
        else
            echo "处理文件 $pdb_file 时出错"
        fi
    fi
done
