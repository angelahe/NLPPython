import spacy

# load language library
nlp = spacy.load('en_core_web_sm')

# create document object
# u = unicode
doc = nlp(u'Tesla is looking at buying U.S. startup for $6 million')

# token.pos - code for part of speech
# token.pos_ - name of the part of speech
# token.dep_ - syntactic dependency
for token in doc:
    print(token.text, token.pos, token.pos_, token.dep_)

# enter processing pipeline, to do tagging parsing and describing the data
# ner - name entity recognizer
print(f'enter the pipeline: {nlp.pipeline}')

doc2 = nlp(u"Tesla isn't looking into startups anymore")
for token in doc2:
    print(token.text, token.pos, token.pos_, token.dep_)

# can use indexing to get tokens (text by default)
print(f'first token is: {doc2[0]}')
print(f'part of speech: {doc2[0].pos_}')