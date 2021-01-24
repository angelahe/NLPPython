import spacy
nlp = spacy.load('en_core_web_sm')
from spacy import displacy

with open('material/UPDATED_NLP_COURSE/Textfiles/peterrabbit.txt') as f:
    doc = nlp(f.read())
# for every token in the 3rd sentence print the token text, POS tag, fine grained tag,
    # and description of the fine-grained tag
    for token in list(doc.sents)[2]:
        print(f"{token.text:{10}} {token.pos_:{10}} {token.tag_:{10}} {str(spacy.explain(token.tag_))}")


# frequency list of POS tags

# what percentage of tokens are nouns

# display dependency parse

# 1st 2 named entities

# How many sentences are contained in the Tale of Peter Rabbit

# how many sentences contain named entities

# display named entity visualization for list_of_sents
