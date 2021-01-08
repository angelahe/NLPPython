import PyPDF2
import re

# 1. print NLP stands for Natural Language Processing using variables
abbr = 'NLP'
full_text = 'Natural Language Processing'
print(f'{abbr} stands for {full_text}')

# 2. create a file in the current working directory called contacts.txt
f = open('contacts.txt', 'w+')
f.write('First_Name Last_Name, Title, Extension, Email')

# 3. Open the file and use .read() to save the contents of the file to a string called `fields`.  Make sure the file is closed at the end.
f.close()
with open('contacts.txt') as f:
    fields = f.read()
print(f'in the file so far: {fields}')

# 4. Use PyPDF2 to open the file `Business_Proposal.pdf`. Extract the text of page 2.
myfile = open('Business_Proposal.pdf', mode='rb')
pdf_reader = PyPDF2.PdfFileReader(myfile)
page2text = pdf_reader.getPage(1).extractText()
print(f'page is as follows: {page2text}')
myfile.close()

# 5. Open the file `contacts.txt` in append mode. Add the text of page 2 from above to `contacts.txt`.
#  CHALLENGE: See if you can remove the word \"AUTHORS:\"
with open('contacts.txt', 'a+')as f:
    f.write(page2text[8:])
    f.seek(0)
    print('after append')
    print(f.read())

# 6. Using the `page_two_text` variable created above, extract any email addresses that were contained in the file `Business_Proposal.pdf`."
pattern = r"[\w]+@[\w]+.[\w]+"
addresses = re.findall(pattern, page2text)
print(f'these are the email addresses: {addresses}')