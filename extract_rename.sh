#!/bin/bash


for folder in mono_output_1428/*; do
    if [ -d "$folder" ]; then
        if [ -f "$folder/ranked_0_pLDDT.csv" ]; then
            base=$(basename "$folder")
            cp "$folder/ranked_0_pLDDT.csv" "pLDDT_1428/$base.csv"
        fi
    fi
done

