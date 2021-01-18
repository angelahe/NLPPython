import spacy
nlp = spacy.load('en_core_web_sm')
doc = nlp(u'This is the first sentence.  This is another sentence.  This is the last sentence.')

for sent in doc.sents:
    print(sent)

# can't index the sentences unless you put them in a list can only index into the doc by token
sentences = list(doc.sents)
# these are of type spacy.tokens.span.Span
print(f'second sentence: {sentences[1]}')

# spacy default behavior
doc3 = nlp(u'"Management is doing things right; leadership is doing the right things." -Peter Drucker')

for sent in doc3.sents:
    print(sent)

# add a new segmentation rule
def set_custom_boundaries(doc):
    for token in doc[:-1]:
        if token.text == ';':
            doc[token.i+1].is_sent_start = True
    return doc

nlp.add_pipe(set_custom_boundaries, before='parser')

print(nlp.pipe_names)

doc4 = nlp(u'"Management is doing things right; leadership is doing the right things." -Peter Drucker')

for sent in doc4.sents:
    print(sent)

# change segmentation rules

nlp = spacy.load('en_core_web_sm')
mystring = u"This is a sentence. This is another.\n\nThis is a \nthird sentence."

# SPACY DEFAULT BEHAVIOR:
doc = nlp(mystring)
print('default behavior of spacy for segmentation')
for sent in doc.sents:
    print([token.text for token in sent])

# change the rules
from spacy.pipeline import SentenceSegmenter

def split_on_newlines(doc):
    start = 0
    seen_newline = False
    for word in doc:
        if seen_newline:
            yield doc[start:word.i]
            start = word.i
            seen_newline = False
        elif word.text.startswith('\n'): # handles multiple occurrences
            seen_newline = True
    yield doc[start:]      # handles the last group of tokens


sbd = SentenceSegmenter(nlp.vocab, strategy=split_on_newlines)
nlp.add_pipe(sbd)

print('now will split on newlines not on periods')
doc = nlp(mystring)
for sent in doc.sents:
    print([token.text for token in sent])


