# movie review dataset - determine if positive or negative review
import numpy as np
import pandas as pd

df = pd.read_csv('material/UPDATED_NLP_COURSE/TextFiles/moviereviews.tsv', sep='\t')
print(df.head())

# the first review
print(df['review'][0])

# raw number
print(f'number of reviews before check for empty and null: {len(df)}')
# check for and remove empty reviews
df.isnull().sum()

df.dropna(inplace=True)

mystring = 'hello'
empty = '   '
print(f'mystring empty? {mystring.isspace()}')
print(f'empty is empty? {empty.isspace()}')

# remove empty strings too
blanks = []
# index, label, review text
for i, lb, rv in df.itertuples():
    if type(rv) == str:     # avoid NaN values
        if rv.isspace():
            blanks.append(i)
# now that have index positions of blank reviews can drop them
df.drop(blanks, inplace=True)
print(f'number of valid reviews is now: {len(df)}')

# look at distribution
print(df['label'].value_counts())

# now split data into training set and test set
from sklearn.model_selection import train_test_split

X = df['review']
y = df['label']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import LinearSVC

# Naïve Bayes:
text_clf_nb = Pipeline([('tfidf', TfidfVectorizer()),
                        ('clf', MultinomialNB()),
                        ])

# Linear SVC:
text_clf_lsvc = Pipeline([('tfidf', TfidfVectorizer()),
                          ('clf', LinearSVC()),
                          ])

# try naive bayes first
text_clf_nb.fit(X_train, y_train)
# Form a prediction set
predictions = text_clf_nb.predict(X_test)
# Report the confusion matrix
from sklearn import metrics
print(metrics.confusion_matrix(y_test,predictions))
# Print a classification report
print(metrics.classification_report(y_test,predictions))
# Print the overall accuracy
print(f'overall accuracy naive Bayes: {metrics.accuracy_score(y_test,predictions)}')

# now try Linear SVC
text_clf_lsvc.fit(X_train, y_train)
# Form a prediction set
predictions = text_clf_lsvc.predict(X_test)
# Report the confusion matrix
from sklearn import metrics
print(metrics.confusion_matrix(y_test,predictions))
# Print a classification report
print(metrics.classification_report(y_test,predictions))
# Print the overall accuracy
print(f'overall accuracy Linear SVC: {metrics.accuracy_score(y_test,predictions)}')