import PyPDF2

with open('.\\PDFFiles\\original\\dummy.pdf', mode = 'rb') as my_pdf1:
    # The mode rb helps to read the file in binary mode 

    print(my_pdf1)
    reader = PyPDF2.PdfFileReader(my_pdf1)
    no_of_pages =  reader.numPages

    page1 = reader.getPage(0)
    page1.rotateClockwise(90)

    writer = PyPDF2.PdfFileWriter()
    writer.addPage(page1) 
    
    # now we need to write to a new pdf file(in binary format again)
    with open('.\\PDFFiles\\processed\\rot_dummy.pdf', mode = 'wb') as pro_pdf1:
        writer.write(pro_pdf1)
    


