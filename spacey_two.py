import spacy

# tokenization
# prefix ¿$("
# suffix km ),.!?
# infix - -- / ...
# exceptions let's U.S. L.A.

nlp = spacy.load('en_cor_web_sm')

mystring = '"We\'re moving to L.A.!"'
doc = nlp(mystring)
for token in doc:
    print(token.text)