import os
import pdfplumber

arquivos = os.listdir()
pdf = pdfplumber.open('teste.pdf')
for i in range(len(pdf.pages)):
    page = pdf.pages[i]
    text = page.extract_text()
    text = text.replace('\n', ' ')
    print(text)