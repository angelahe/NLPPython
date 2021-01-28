# Word2vec is two layer neural net to process text
# input is text corpus and output is set of vectors
# group vectors of similar words together in vectorspace
# ie detect similarities mathematically

# 2 approaches - CBOW and Skip-gram
# CBOW - given context words predict output word
# Skip-gram - input word output contexts

# in spacy vector has 300 dimensions
# use cosine similarity to measure how similar word vectors are to each other

# vector arithmetic
# new_vector = king - man + woman should be closest to queen
# can also do verb tenses

import spacy
nlp = spacy.load('en_core_web_lg')
print(nlp(u'lion').vector)

print(nlp(u'The quick brown fox jumped').vector)


def print_similarity(tokens):
    for token1 in tokens:
        for token2 in tokens:
            print(token1.text, token2.text, token1.similarity(token2))

tokens1 = nlp(u'lion cat pet')
tokens2 = nlp(u'like love hate')
print_similarity(tokens1)
print_similarity(tokens2)

# note that like and love vs love and hate are used in similar contexts so get a similar similarity score

# aggregate 300 dimensions into a euclidian norm

print(f'in this vocab there are (words, dimensions) {nlp.vocab.vectors.shape}')

tokens = nlp(u"dog cat nargle")

#oov = out of vocabulary
template = "{0:8}{1:12}{2:20}{3:12}"
print(template.format("Text", "Has Vector", "Norm", "Not in Vocab"))
for token in tokens:
    print(template.format(token.text, token.has_vector, token.vector_norm, token.is_oov))

from scipy import spatial

cosine_similarity = lambda vec1, vec2: 1 - spatial.distance.cosine(vec1, vec2)
king = nlp.vocab['king'].vector
man = nlp.vocab['man'].vector
woman = nlp.vocab['woman'].vector

# Now we find the closest vector in the vocabulary to the result of "man" - "woman" + "queen"
new_vector = king - man + woman
computed_similarities = []

for word in nlp.vocab:
    # Ignore words without vectors and mixed-case words:
    if word.has_vector:
        if word.is_lower:
            if word.is_alpha:
                similarity = cosine_similarity(new_vector, word.vector)
                computed_similarities.append((word, similarity))

# sort by most similar
computed_similarities = sorted(computed_similarities, key=lambda item: -item[1])

print([w[0].text for w in computed_similarities[:10]])