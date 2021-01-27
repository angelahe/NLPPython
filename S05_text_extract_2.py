# bag of words, stop words and stems, tagging
import numpy as np
import pandas as pd

df = pd.read_csv('material/UPDATED_NLP_COURSE/TextFiles/smsspamcollection.tsv', sep='\t')
print(df.head)

# check for null values
print(df.isnull().sum())

print(df['label'].value_counts())

# split data into data set and training set
from sklearn.model_selection import train_test_split

X = df['message']  # this time we want to look at the text
y = df['label']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

from sklearn.feature_extraction.text import CountVectorizer
count_vect = CountVectorizer()

#fit vectorizer to the data
# count_vect.fit(X_train)
#transform the original text message to vector
# X_train_counts = count_vect.transform(X_train)

# or use the convenience method since you usually do fit then transform
X_train_counts = count_vect.fit_transform(X_train)
# compress using the zeros, is a large matrix, don't print!!
print(X_train.shape)
print(X_train_counts.shape)

# pass into tfidftransformer do downscale words that occur in many docs
# that are less informative

from sklearn.feature_extraction.text import TfidfTransformer
tfidf_transformer = TfidfTransformer()

X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)
print(X_train_tfidf.shape)

# combine 2 steps into 1 with this:
from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer()

X_train_tfidf = vectorizer.fit_transform(X_train) # remember to use the original X_train set
print(X_train_tfidf.shape)

# train a classifier
# import a linear support classifier
from sklearn.svm import LinearSVC
clf = LinearSVC()
print(clf.fit(X_train_tfidf,y_train))

# whole pipeline into 1 object
from sklearn.pipeline import Pipeline
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.svm import LinearSVC

text_clf = Pipeline([('tfidf', TfidfVectorizer()),
                     ('clf', LinearSVC()),
                     ])

# Feed the training data through the pipeline
print(text_clf.fit(X_train, y_train) )
# one step for calling vectorizer, create instance of vectorizer, do fit/transform
# then import the classifier, create instance of classifier, fit on vectorized form
print(text_clf.fit(X_train, y_train))

# form prediction set
predictions = text_clf.predict(X_test)

# Report the confusion matrix
from sklearn import metrics
print(metrics.confusion_matrix(y_test,predictions))

# Print a classification report
print(metrics.classification_report(y_test,predictions))

# Print the overall accuracy
print(f'overall accuracy: {metrics.accuracy_score(y_test,predictions)}')

# make new prediction
print('new prediction for legit message:')
print(text_clf.predict(["Hi how are you doing today?"]))

print('new prediction for spam message:')
print(text_clf.predict(["Congratulations! you've been selected as a winner. text won to 44255. congratulations free entry to contest"]))
