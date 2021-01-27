# movie reviews part 2
# load dataset into pandas dataframe
import numpy as np
import pandas as pd

df = pd.read_csv('material/UPDATED_NLP_COURSE/TextFiles/moviereviews2.tsv', sep='\t')

# Check for missing values:
df.isnull().sum()

# Check for whitespace strings and Remove NaN values too
blanks = []
for i, label, review in df.itertuples():
    if type(review) == str:
        if review.isspace():
            blanks.append(i)

df.drop(blanks, inplace=True)

# Remove NaN values
df.dropna(inplace=True)
# Peek at the label column
print(df['label'].value_counts())
# Split data into train and test sets
from sklearn.model_selection import train_test_split

X = df['review']
y = df['label']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

# Build pipeline to vectorize the data, train and fit a model
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import LinearSVC

text_clf_nb = Pipeline([('tfidf', TfidfVectorizer()),
                        ('clf', MultinomialNB()),
                        ])

text_clf_lsvc = Pipeline([('tfidf', TfidfVectorizer()),
                          ('clf', LinearSVC()),
                          ])

# run predictions and analyze the results
text_clf_nb.fit(X_train, y_train)
# form a prediction set
predictions = text_clf_nb.predict(X_test)
# report the confusion matrix
from sklearn import metrics
print(metrics.confusion_matrix(y_test,predictions))
# print a classification report
print(metrics.classification_report(y_test,predictions))
# print the overall accuracy
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