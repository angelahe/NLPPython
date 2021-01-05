import PyPDF2

# 1. print NLP stands for Natural Language Processing using variables
abbr = 'NLP'
full_text = 'Natural Language Processing'
print(f'{abbr} stands for {full_text}')

# 2. create a file in the current working directory called contacts.txt
f = open('contacts.txt', 'w+')
f.write('First_Name Last_Name, Title, Extension, Email')
# 3. Open the file and use .read() to save the contents of the file to a string called `fields`.  Make sure the file is closed at the end.
fields = f.read()
f.close()
# 4. Use PyPDF2 to open the file `Business_Proposal.pdf`. Extract the text of page 2.
myfile = open('Business_Proposal.pdf', mode='rb')
pdf_reader = PyPDF2.PdfFileReader(myfile)
page2 = pdf_reader.getPage(1)
page2text = page2.extractText()
print(f'page is as follows: {page2text}')
myfile.close()
# 5. Open the file `contacts.txt` in append mode. Add the text of page 2 from above to `contacts.txt`.
#  CHALLENGE: See if you can remove the word \"AUTHORS:\"

# 6. Using the `page_two_text` variable created above, extract any email addresses that were contained in the file `Business_Proposal.pdf`."
