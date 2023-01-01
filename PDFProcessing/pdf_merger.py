import PyPDF2 
from sys import argv
in_files = argv[1:] # makes a list of all the inputs

def pdf_combiner(pdf_li):
    merge = PyPDF2.PdfFileMerger()
    for pdf in pdf_li:
        merge.append(pdf)
    merge.write('D:\\PythonCodes\\PDFProcessing\\PDFFiles\\medical.pdf')

pdf_combiner(in_files)