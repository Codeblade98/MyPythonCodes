from PyPDF2 import PdfWriter, PdfReader
from pathlib import Path
from sys import argv

input_file = argv[1]
out_dir = argv[2]
wtr_path = argv[3]

try:
    p = Path(out_dir)
    p.mkdir()

except FileExistsError:
    print('Directory already exists, using existing directory')

else:
    print('New directory is being created to save the processed files')


writer = PdfWriter()

file_reader = PdfReader(input_file)
for index in range(0, file_reader.numPages):
    wtr_reader = PdfReader(wtr_path)
    wtr = wtr_reader.getPage(0)
    page = file_reader.getPage(index)
    wtr.merge_page(page)
    writer.addPage(wtr)
    with open(f'{out_dir}\\converted.pdf', mode = 'wb') as myPDF:
        writer.write(myPDF)



