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
from spacy.matcher import Matcher
matcher = Matcher(nlp.vocab)

# with 'IS_SPACE' pattern between the two words
# create pattern and add it to matcher
pattern = [{'LOWER':'swimming'}, {'IS_SPACE':True, 'OP':'*'}, {'LOWER':'vigorously'} ]
matcher.add('Swimming', None, pattern)
# create a list of matches and print the list
found_matches = matcher(doc)
print(found_matches)
# print the text surrounding each match
def surrounding_text(doc, start, end):
    print(doc[start-5:end+5])

surrounding_text(doc, 1274, 1277)
surrounding_text(doc, 3607, 3610)

# print the sentence that contains each found match
for sentence in doc_sentences:
    if found_matches[0][1] < sentence.end:
        print(sentence)
        break

for sentence in doc_sentences:
    if found_matches[1][1] < sentence.end:
        print(sentence)
        break