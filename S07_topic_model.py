# Topic Modeling
# analyze large volumes of text by clustering docs into topics
# unlabeled meaning = can't apply supervised learning approaches to create machine learning models for the data
# attempts to discover labels, clusters of docs, grouped together by topic
# hard to evaluate how the clustering did because there is no right answer
#
# Latent Dirichlet Allocation
# assumptions - docs with similar topics use similar groups of words
# latent topics can then be found by searching for groups of words that frequently occur together
# in docs across the corpus
# documents are probability distributions over latent topics
# topics are probability distributions over words

# choose topic miixture for doc e.g. business 60% 20% politics 10% food

# generate each word in doc by picking a topic according to the multinomial distribution identified ie 60 20 10
# randomly assign each word in doc to one of K topics
# then iterate over every word to improve the topics

# user has to decide on number of topics present in the document before starting the process
# user has to interpret what the topics are

import pandas as pd
npr = pd.read_csv('material/UPDATED_NLP_COURSE/05-Topic-Modeling/npr.csv')

print(npr.head())

# preprocessing
from sklearn.feature_extraction.text import CountVectorizer
# can discard words that show up in 95% max and less than twice
cv = CountVectorizer(max_df=0.95, min_df=2, stop_words='english')
dtm = cv.fit_transform(npr['Article'])
print(dtm)

# LDA
from sklearn.decomposition import LatentDirichletAllocation
LDA = LatentDirichletAllocation(n_components=7,random_state=42)
# This can take awhile, we're dealing with a large amount of documents!
print(LDA.fit(dtm))

print(len(cv.get_feature_names()))

import random

for i in range(10):
    random_word_id = random.randint(0,54776)
    print(cv.get_feature_names()[random_word_id])

for i in range(10):
    random_word_id = random.randint(0,54776)
    print(cv.get_feature_names()[random_word_id])

print(len(LDA.components_))

print(LDA.components_)

print(len(LDA.components_[0]))

single_topic = LDA.components_[0]

# Returns the indices that would sort this array.
print(single_topic.argsort())

# Word least representative of this topic
print(single_topic[18302])

# Word most representative of this topic
print(single_topic[42993])

# Top 10 words for this topic:
print(single_topic.argsort()[-10:])

top_word_indices = single_topic.argsort()[-10:]

for index in top_word_indices:
    print(cv.get_feature_names()[index])

for index,topic in enumerate(LDA.components_):
    print(f'THE TOP 15 WORDS FOR TOPIC #{index}')
print([cv.get_feature_names()[i] for i in topic.argsort()[-15:]])
print('\n')

# attaching topic labels to articles
print(dtm)

print(dtm.shape)

print(len(npr))

topic_results = LDA.transform(dtm)

print(topic_results.shape)

print(topic_results[0])

print(topic_results[0].round(2))

# first article belongs to topic 1
print(topic_results[0].argmax())

#combine with original data
npr.head()
topic_results.argmax(axis=1)
npr['Topic'] = topic_results.argmax(axis=1)

print(npr.head(10))