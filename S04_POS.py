# retrieve parts of speech with spacy (POS)
# use named entity recognition with spacy (NER)
# visualize POS and NER
# perform sentence segmentation

# words that look completely different can mean almost the same thing
# same words in different order can mean something completely different

# coarse POS noun verb adj
# fine grained POS plural noun, past tense verb, superlative adj

# see 0 POS basics
import spacy
nlp = spacy.load('en-core-web-sm')
doc = nlp(u"The quick brown fox jumped over the lazy dog's back.")

print(f'the text: {doc.text}')
print(f'the token: {doc[4].text}')
print(f'the part of speech: {doc[4].pos_}')
print(f'the fine grained part of speech: {doc[4].tag_}')

for token in doc:
    print(f"{token.text:{10}} {token.pos_:{10}} {token.tag_:{10}} {spacy.explain(token.tag_)}")