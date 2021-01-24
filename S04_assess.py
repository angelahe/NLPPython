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
    POS_counts = doc.count_by(spacy.attrs.POS)

    for k,v in sorted(POS_counts.items()):
        print(f"id:{k:{5}} {doc.vocab[k].text:{10}} {v:{5}} instances")

# what percentage of tokens are nouns
    noun_percent = POS_counts[91] / len(doc) * 100
    print(f"percent of doc that are nouns: {noun_percent:.2f}")

# display dependency parse
    displacy.serve(list(doc.sents)[2], style='dep')

# 1st 2 named entities
    for entity in doc.ents[:2]:
        print(f'{entity.text:{30}} {entity.label_:{15}} {str(spacy.explain(entity.label_))}')

# How many sentences are contained in the Tale of Peter Rabbit

# how many sentences contain named entities

# display named entity visualization for list_of_sents
