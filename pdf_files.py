import PyPDF2

# open in read binary mode
myfile = open('Business_Proposal.pdf', mode='rb')

pdf_reader = PyPDF2.PdfFileReader(myfile)

pages = pdf_reader.numPages
page_one = pdf_reader.getPage(0)
page_string = page_one.extractText()
print(f"{page_string}")

pdf_writer = PyPDF2.PdfFileWriter()

pdf_writer.addPage(page_one)
pdf_output = open('My_Brand_New.pdf', 'wb')
pdf_writer.write(pdf_output)
pdf_output.close()
myfile.close()

f = open('Business_Proposal.pdf', 'rb')
pdf_text = [0]
pdf_reader = PyPDF2.PdfFileReader(f)

# load pages into a list
for p in range(pdf_reader.numPages):
    page = pdf_reader.getPage(p)
    pdf_text.append(page.extractText())

f.close()

for page in pdf_text:
    print(page)
    print('\n\n')