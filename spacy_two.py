import spacy
nlp = spacy.load('en_core_web_sm')

# tokenization
# prefix ¿$("
# suffix km ),.!?
# infix - -- / ...
# exceptions let's U.S. L.A.

mystring = '"We\'re moving to L.A.!"'
doc = nlp(mystring)
for token in doc:
    print(token.text)

doc2 = nlp(u"We're here to help! Send snail mail, email support@oursite.com or visit us at http://www.oursite.com")

for t in doc2:
    print(t)

# 10.30 preserved
doc3 = nlp(u"A 5km NYC cab ride costs $10.30")
for t in doc3:
    print(t)

# keeps St. together, U.S together
doc4 = nlp(u"Let's visit St. Louis in the U.S. next year.")

#count num of tokens
print(f'number of tokens: {len(doc4)}')

# count the vocab in the corpus
print(f'number of tokens in the corpus: {len(doc4.vocab)}')

doc5 = nlp(u"It is better to give than receive.")
print(f'first token in {doc5} is {doc5[0]}')
print(f'tokens 3 to 5: {doc5[2:5]}')

doc6 = nlp(u'Apple to build a Hong Kong factor for $6 million')
for token in doc6:
    print(token.text, end=' | ')

# print named entities e.g. organization
for entity in doc6.ents:
    print(entity)
    print(entity.label_)
    print(str(spacy.explain(entity.label_)))
    print('\n')

#noun chunks
doc7 = nlp(u'Autonomous cars shift insurance liability toward manufacturers.')
print(f'sentence: {doc7}')
for chunk in doc7.noun_chunks:
    print(chunk)

from spacy import displacy
#built in visualizer
# from command line will popup dialog, say allow access, then
# open new tab in browser 127.0.0.1:5000
# ctrl C between visualizations

doc = nlp(u"Apple is going to build a U.K. factory for $6 million.")

displacy.serve(doc, style='dep', options={'distance':110})

doc2 = nlp(u"Over the last quarter Apple sold nearly 20 thousand iPods for a profit of $6 million.")

displacy.serve(doc2, style='ent')