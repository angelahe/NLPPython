import spacy

# load language library
nlp = spacy.load('en_core_web_sm')
nlp_es = spacy.load('es_core_news_sm')

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

# try to open up spanish and tokenize it :D
nlp_es = spacy.load("es_core_news_sm")
doc3 = nlp_es(u"Mi abuela no está en casa")
for token in doc3:
    print(token.text, token.pos, token.pos_, token.dep_)

doc4 = nlp(u'Although commonly attributed to John Lennon from his song "Beautiful Boy", \
the quote "Life is what happens to us while we are making other plans" was written by \
cartoonist Allen Saunders and published in Reader\'s Digest in 1957, when Lennon was 17.')

life_quote = doc4[16:30]
print(life_quote)

print(f'type of life quote is:{type(life_quote)}')
print(f'type of doc4 is:{type(doc4)}')

doc5 = nlp(u"This is the first sentence. This is another sentence. This is the last sentence.")

for sentence in doc5.sents:
    print(sentence)

print(f'the 6th token in the doc is: {doc5[6]}')
print(f'is the 6th token the start of a sentence? {doc5[6].is_sent_start}')
print(f'token 7: {doc5[7]} is start of sentence? {doc5[7].is_sent_start}')