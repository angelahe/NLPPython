# Import spaCy and load the language library. Remember to use a larger model!
import spacy
nlp = spacy.load('en_core_web_md')

# Choose the words you wish to compare, and obtain their vectors
word1 = nlp.vocab['wolf'].vector
word2 = nlp.vocab['dog'].vector
word3 = nlp.vocab['cat'].vector

# Import spatial and define a cosine_similarity function
from scipy import spatial

cosine_similarity = lambda x, y: 1 - spatial.distance.cosine(x, y)

# Write an expression for vector arithmetic
# For example: new_vector = word1 - word2 + word3
new_vector = word1 - word2 + word3

# List the top ten closest vectors in the vocabulary to the result of the expression above
computed_similarities = []

for word in nlp.vocab:
    if word.has_vector:
        if word.is_lower:
            if word.is_alpha:
                similarity = cosine_similarity(new_vector, word.vector)
                computed_similarities.append((word, similarity))

computed_similarities = sorted(computed_similarities, key=lambda item: -item[1])

print([w[0].text for w in computed_similarities[:10]])

def vector_math(a,b,c):
    new_vector = nlp.vocab[a].vector - nlp.vocab[b].vector + nlp.vocab[c].vector
    computed_similarities = []

    for word in nlp.vocab:
        if word.has_vector:
            if word.is_lower:
                if word.is_alpha:
                    similarity = cosine_similarity(new_vector, word.vector)
                    computed_similarities.append((word, similarity))

    computed_similarities = sorted(computed_similarities, key=lambda item: -item[1])

    return [w[0].text for w in computed_similarities[:10]]

# Test the function on known words:
print('mother - woman + man = father')
vector_result = vector_math('mother','woman','man')
print(vector_result)

print('wolf - dog + cat = wildcat')
vector_result = vector_math('wolf', 'dog', 'cat')
print(vector_result)

# Perform VADER Sentiment on own Review

# Import SentimentIntensityAnalyzer and create an sid object
from nltk.sentiment.vader import SentimentIntensityAnalyzer

sid = SentimentIntensityAnalyzer()

# Write a review as one continuous string (multiple sentences are ok)
review = "This movie made me feel like I was there, with that life, with those limitations, and with that alternate reality like I've never experienced before.  Excellent."

# Obtain the sid scores for your review
print(sid.polarity_scores(review))

def review_rating(string):
    scores = sid.polarity_scores(string)
    if scores['compound'] == 0:
        return 'Neutral'
    elif scores['compound'] > 0:
        return 'Positive'
    else:
        return 'Negative'

# Test the function on your review above:
print(review_rating(review))