import spacy
nlp = spacy.load('en_core_web_sm')
doc = nlp(u'This is the first sentence.  This is another sentence.  This is the last sentence.')

for sent in doc.sents:
    print(sent)

# can't index the sentences unless you put them in a list can only index into the doc by token
sentences = list(doc.sents)
# these are of type spacy.tokens.span.Span
print(f'second sentence: {sentences[1]}')

