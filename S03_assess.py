import spacy
nlp = spacy.load('en_core_web_sm')

with open('material/UPDATED_NLP_COURSE/TextFiles/owlcreek.txt') as f:
    doc = nlp(f.read())
# create doc object
# verify loading worked
print(f'{doc[:36]}')

# how many tokens are in the file
print(f'tokens in the file: {len(doc)}')

# how many sentences are in the file

# ie make list and check length of list
doc_sentences = [sent for sent in doc.sents]
print(f'sentences in file: {len(doc_sentences)}')
# print the 2nd sentence in the doc
print(f'2nd sentence in file:\n {doc_sentences[1]}')
# alternatively
print(doc_sentences[1].text)
# for each token print its text, POS tag, dep tag and lemma
for token in doc_sentences[1]:
    print(f'{token.text:{15}} {token.pos_:{10}} {token.dep_:{10}} {token.lemma_}')

# write a matcher called Swimming that finds swimming vigorously
# with 'IS_SPACE' pattern between the two words
# import matcher library
# create pattern and add it to matcher
# create a list of matches and print the list
# print the text surrounding each match
# print the sentence that contains each found match
