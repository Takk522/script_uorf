import os
import pandas as pd

folder_path = "/Users/jianchengluo/Desktop/script_uORF/outdssp_1428"  #根据具体路径进行修改

dssp_files = [f for f in os.listdir(folder_path) if f.endswith(".dssp")]

data = pd.DataFrame(columns=["File Name", "Secondary Structure"])

for dssp_file in dssp_files:
    file_name = os.path.splitext(dssp_file)[0]  
    dssp_file_path = os.path.join(folder_path, dssp_file)
    print(f"Processing file: {dssp_file_path}")

    try:
        with open(dssp_file_path, 'r') as f:
            lines = f.readlines()
            secondary_structure = ""
            reading_secondary_structure = False 
            for line in lines:
                if line.startswith("  #  RESIDUE AA"):
                    reading_secondary_structure = True
                    continue

                if reading_secondary_structure:
                    secondary_structure += line[16]
        
            secondary_structure = secondary_structure.replace(" ", "-")
        print(secondary_structure)
        new_row = pd.DataFrame({"File Name": [file_name], "Secondary Structure": [secondary_structure]})
        data = pd.concat([data, new_row], ignore_index=True)
    except Exception as e:
        print(f"Error processing {dssp_file_path}: {str(e)}")


output_excel_file = "dssp_1428.xlsx"   #根据具体路径进行修改
data.to_excel(output_excel_file, index=False)

print(f"数据已保存到 {output_excel_file}")

