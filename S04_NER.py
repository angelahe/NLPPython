import spacy
nlp = spacy.load('en_core_web_sm')

# Write a function to display basic entity info:
# see 02NER doc for list of NER tags

def show_ents(doc):
    if doc.ents:
        for ent in doc.ents:
            print(ent.text+' - '+ent.label_+' - '+str(spacy.explain(ent.label_)))
    else:
        print('No named entities found.')

doc = nlp(u'May I go to Washington, DC next May to see the Washington Monument?')

show_ents(doc)

doc2 = nlp(u'Can I please borrow 500 dollars from you to buy some Microsoft stock?')

for ent in doc2.ents:
    print(ent.text, ent.start, ent.end, ent.start_char, ent.end_char, ent.label_)

doc3 = nlp(u'Tesla to build a U.K. factory for $6 million')

# want to add own named entities e.g. person, org, etc
from spacy.tokens import Span

# Get the hash value of the ORG entity label
ORG = doc.vocab.strings[u'ORG']

# Create a Span for the new entity
new_ent = Span(doc, 0, 1, label=ORG)

# Add the entity to the existing Doc object
doc3.ents = list(doc3.ents) + [new_ent]
# or could use append


print(f'entities for {doc3}')
show_ents(doc3)

