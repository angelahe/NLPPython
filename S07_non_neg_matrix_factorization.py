# non negative matrix factorization
# unsupervised algorithm that performs dimensionality reduction and clustering
# use with tf-idf to model topics across documents
#
# input: non negative data matrix(A) via tf-idf
# number of basis vectors(k) ie topics
# initial values for factors W (basis vectors) where rows = features
# and H (coefficient matrix) where columns = objects
#
# objective function - some measure of reconstruction error between A and the approximation WH
# then use expectation maximization optimisation to refine W and H to minimise the objective function
# commonly iterate between 2 multiplicative update rules until convergence

# 1. construct vector space model for documents (after stopword filtering) for doc matrix A
# 2. apply tf-idf term weight normalisation to A
# 3. normalize tf-idf vectors to unit length
# 4. initialize factors using NNDSVD on A (non negative double single singular value decomposition
# 5. apply projected gradient NMF to A (non negative matrix factorization)

# will get the basis vectors - topic clusters in the data
# coefficient matrix - the membership weights for documents relative to each topic cluster

# will repeat analysis of npr article data set and discover topics with NMF, (switching out LDA for NMF)

import pandas as pd
npr = pd.read_csv('material/UPDATED_NLP_COURSE/05-Topic-Modeling/npr.csv')

print(npr.head())

from sklearn.feature_extraction.text import TfidfVectorizer

tfidf = TfidfVectorizer(max_df=0.95, min_df=2, stop_words='english')
dtm = tfidf.fit_transform(npr['Article'])
print(f'articles by number of words: {dtm}')

from sklearn.decomposition import NMF

nmf_model = NMF(n_components=7,random_state=42)

# This can take awhile, we're dealing with a large amount of documents!
nmf_model.fit(dtm)

print(f'number of feature names: {len(tfidf.get_feature_names())}')

print(f'get 2300th feature name: {tfidf.get_feature_names()[2300]}')

for index,topic in enumerate(nmf_model.components_):
    print(f'the top 15 words for topic # {index}')
    print([tfidf.get_feature_names()[i] for i in topic.argsort()[-15:]])
    print('\n')

topic_results = nmf_model.transform(dtm)
# first article belongs to topic 1
topic_results[0].argmax()

npr.head()


print(' get index positions that match up to topics printed above ')

topic_results.argmax(axis=1)

npr['Topic'] = topic_results.argmax(axis=1)

print(npr.head(10))
print('articles:')
# create a dictionary to label the topics
mytopic_dict = {0:'health', 1:'election', 2:'legislate', 3:'politics', 4:'election', 5:'music',6:'education'}

npr['Topic Label'] = npr['Topic'].map(mytopic_dict)
print(npr.head())

