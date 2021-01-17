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

# add multiple new entities

doc = nlp(u"Our company created a brand new vacuum cleaner."
          u"This new vacuum-cleaner is the best in show.")

show_ents(doc)

from spacy.matcher import PhraseMatcher
# Import PhraseMatcher and create a matcher object:
matcher = PhraseMatcher(nlp.vocab)
# Create the desired phrase patterns:
phrase_list = ['vacuum cleaner', 'vacuum-cleaner']
phrase_patterns = [nlp(text) for text in phrase_list]

# Apply the patterns to our matcher object:
matcher.add('newproduct', None, *phrase_patterns)

# Apply the matcher to our Doc object:
found_matches = matcher(doc)

print(f'these match the patterns {phrase_list} : \n {found_matches}')

# Here we create Spans from each match, and create named entities from them:
from spacy.tokens import Span

PROD = doc.vocab.strings[u'PRODUCT']

new_ents = [Span(doc, match[1],match[2],label=PROD) for match in found_matches]

doc.ents = list(doc.ents) + new_ents

show_ents(doc)

doc = nlp(u'Originally priced at $29.50, the sweater was marked down to five dollars.')

show_ents(doc)

doc = nlp(u"Originally I paid $29.95 for this toy car, but now it is marked down by 10 dollars.")

print(f'number of entities in sentence with money: {len([ent for ent in doc. ents if ent.label_ == "MONEY"])}')
