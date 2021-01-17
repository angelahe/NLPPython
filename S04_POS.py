# retrieve parts of speech with spacy (POS)
# use named entity recognition with spacy (NER)
# visualize POS and NER
# perform sentence segmentation

# words that look completely different can mean almost the same thing
# same words in different order can mean something completely different

# coarse POS noun verb adj
# fine grained POS plural noun, past tense verb, superlative adj

# see 0 POS basics

# import spacy
# nlp = spacy.load('en')

import spacy
nlp = spacy.load('en_core_web_sm')

doc = nlp(u"The quick brown fox jumped over the lazy dog's back.")

print(f'the text: {doc.text}')
print(f'the token: {doc[4].text}')
print(f'the part of speech: {doc[4].pos_}')
print(f'the fine grained part of speech: {doc[4].tag_}')

for token in doc:
    print(f"{token.text:{10}} {token.pos_:{10}} {token.tag_:{10}} {spacy.explain(token.tag_)}")

doc = nlp(u"I read books on NLP.")
print(doc.text)
word = doc[1]
print(f'{word.text:{10}} {word.pos_:{8}} {word.tag_:{6}} {spacy.explain(word.tag_)}')

doc2 = nlp(u"I read a book on NLP")
print(doc2.text)
word2 = doc2[1]
print(f'{word2.text:{10}} {word2.pos_:{8}} {word2.tag_:{6}} {spacy.explain(word2.tag_)}')
print(f'{spacy.explain(word2.pos_)}')
print(doc)
POS_counts = doc.count_by(spacy.attrs.POS)
print(POS_counts)
print(f'POS code for quick: {doc[2].pos}')
print(f'lookup POS code text for quick {doc.vocab[83].text}')

# frequency list for POS of entire document
for k,v in sorted(POS_counts.items()):
    print(f'{k}. {doc.vocab[k].text:{5}}: {v}')

# frequency list for fine grained POS of entire document
TAG_counts = doc.count_by(spacy.attrs.TAG)
for k,v in sorted(TAG_counts.items()):
    print(f'{k}. {doc.vocab[k].text:{4}}: {v}')

# dependency counts
DEP_counts = doc.count_by(spacy.attrs.DEP)
for k,v in sorted(DEP_counts.items()):
    print(f'{k}. {doc.vocab[k].text:{4}}: {v}')

# review of visualizing parts of speech
from spacy import displacy
#built in visualizer
# from command line will popup dialog, say allow access, then
# open new tab in browser 127.0.0.1:5000
# ctrl C between visualizations
doc = nlp(u"The quick brown fox jumped over the lazy dog's back.")
displacy.serve(doc, style='dep', options={'distance':110})

# create options dictionary
options = {'distance':110, 'compact': 'True', 'color':'yellow', 'bg': '#09a3d5', 'font': 'Times'}
# Ctrl+C and refresh browser to see the second display
displacy.serve(doc, style='dep', options=options)

# create several displays
doc2 = nlp(u"This is a sentence. This is another, possibly longer sentence.")

# Create spans from Doc.sents:
spans = list(doc2.sents)

displacy.serve(spans, style='dep', options={'distance': 110})