"""
PDF Converter - A Python script that converts word documents to PDF format in batch.

Install Dependencies: 
pip install docx2pdf

Open the folder with docs and run the script.

Usage:
python doc_to_pdf.py

This script is open source and available on GitHub at https://github.com/swatishchoudhury/pyscripts.
"""

import os
from docx2pdf import convert

script_dir = os.path.dirname(os.path.abspath(__file__))

newfolder = os.path.join(script_dir, os.path.basename(script_dir) + "-pdf")
if not os.path.exists(newfolder):
    os.makedirs(newfolder)

for filename in os.listdir(script_dir):
    if filename.endswith(".docx"):
        docx_path = os.path.join(script_dir, filename)
        pdf_path = os.path.join(newfolder, filename[:-5] + ".pdf")
        convert(docx_path, pdf_path)
        print(f"{docx_path} ---> {pdf_path}")

print("Conversion complete!")
