import pandas as pd
quora = pd.read_csv('material/UPDATED_NLP_COURSE/05-Topic-Modeling/quora_questions.csv')
print(quora.head())

from sklearn.feature_extraction.text import TfidfVectorizer
tfidf = TfidfVectorizer(max_df=0.95, min_df=2, stop_words='english')

dtm = tfidf.fit_transform(quora['Question'])

print(dtm)

# Non negative matrix factorization
from sklearn.decomposition import NMF

nmf_model = NMF(n_components=20,random_state=42)
print(nmf_model.fit(dtm))

# print top 15 most common words for each of the 20 topics
for index,topic in enumerate(nmf_model.components_):
    print(f'THE TOP 15 WORDS FOR TOPIC #{index}')
    print([tfidf.get_feature_names()[i] for i in topic.argsort()[-15:]])
    print('\n')

# add a new column to the original quora dataframe to label each quesiton into a topic category
print(quora.head())

topic_results = nmf_model.transform(dtm)
topic_results.argmax(axis=1)

quora['Topic'] = topic_results.argmax(axis=1)

print(quora.head(10))